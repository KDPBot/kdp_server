from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from bs4 import BeautifulSoup

from app.db.session import get_session
from app.schemas.kdp import KDPPayload
from app.models.royalty import RoyaltyRead
from app.crud import royalty_crud

router = APIRouter()

@router.post("/parse", response_model=List[RoyaltyRead])
async def parse_kdp_html(payload: KDPPayload, session: AsyncSession = Depends(get_session)):
    """
    This endpoint receives raw KDP Royalties Estimator HTML,
    parses it, extracts the tabular data, and saves it to the database.
    """
    print(f"Received HTML from account: {payload.accountIdentifier}")
    print("Starting HTML parsing...")
    print(payload.htmlContent[:500])  # Print the first 500 characters for debugging

    soup = BeautifulSoup(payload.htmlContent, 'lxml')

    try:
        extracted_data = []

        table_rows = soup.select("div.ui.items.no-margin.unstackable > div.item")

        for row in table_rows:
            if not row.select_one("img"):
                print("Skipping summary row...")
                continue

            title_element = row.select_one(".truncate-overflow")
            title = title_element.get_text(strip=True) if title_element else "Title Not Found"

            value_elements = row.select(".sixteen.wide.computer.column .row > div")

            if len(value_elements) >= 6:
                ebook_royalties = value_elements[1].get_text(strip=True)
                print_royalties = value_elements[2].get_text(strip=True)
                kenp_royalties = value_elements[3].get_text(strip=True)
                total_royalties = value_elements[4].get_text(strip=True)
                total_royalties_usd = value_elements[5].get_text(strip=True)
            else:
                ebook_royalties, print_royalties, kenp_royalties, total_royalties, total_royalties_usd = ["N/A"] * 5

            extracted_data.append({
                "bookTitle": title,
                "eBookRoyalties": ebook_royalties,
                "printRoyalties": print_royalties,
                "kenpRoyalties": kenp_royalties,
                "totalRoyalties": total_royalties,
                "totalRoyaltiesUSD": total_royalties_usd,
            })

        print("Successfully extracted data:")
        print(extracted_data)

        royalties = await royalty_crud.create_royalty_data(session, payload.accountIdentifier, extracted_data)
        return royalties

    except Exception as e:
        print(f"Error parsing HTML: {e}")
        raise HTTPException(status_code=500, detail=f"Error parsing HTML: {str(e)}")

@router.get("/", response_model=List[RoyaltyRead])
async def get_royalties(session: AsyncSession = Depends(get_session)):
    """
    This endpoint fetches all royalty data from the database.
    """
    try:
        data = await royalty_crud.get_all_royalties(session)
        return data
    except Exception as e:
        print(f"Error fetching royalties: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching royalties: {str(e)}")
