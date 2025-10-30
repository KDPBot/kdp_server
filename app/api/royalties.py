from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from bs4 import BeautifulSoup

from app.db.session import get_session
from app.schemas.kdp import KDPPayload
from app.models.royalty import RoyaltyRead
from app.crud import royalty_crud, portfolio_crud

router = APIRouter()

class LinkPortfolioRequest(SQLModel):
    portfolio_id: int

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

            def clean_royalty_value(value):
                return value.replace('$', '').replace(',', '').strip()

            # More specific selectors to target each royalty value individually
            royalty_values = row.select(".sixteen.wide.computer.column .row .right.aligned.column")

            if len(royalty_values) >= 5:
                ebook_royalties = clean_royalty_value(royalty_values[0].get_text(strip=True))
                print_royalties = clean_royalty_value(royalty_values[1].get_text(strip=True))
                kenp_royalties = clean_royalty_value(royalty_values[2].get_text(strip=True))
                total_royalties = clean_royalty_value(royalty_values[3].get_text(strip=True))
                total_royalties_usd = clean_royalty_value(royalty_values[4].get_text(strip=True))
            else:
                ebook_royalties, print_royalties, kenp_royalties, total_royalties, total_royalties_usd = ["0.00"] * 5

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

        # Aggregate data to handle duplicates
        aggregated_data = {}
        for item in extracted_data:
            title = item['bookTitle']
            
            def to_float(value):
                try:
                    return float(value)
                except (ValueError, TypeError):
                    return 0.0

            if title in aggregated_data:
                aggregated_data[title]['eBookRoyalties'] += to_float(item['eBookRoyalties'])
                aggregated_data[title]['printRoyalties'] += to_float(item['printRoyalties'])
                aggregated_data[title]['kenpRoyalties'] += to_float(item['kenpRoyalties'])
                aggregated_data[title]['totalRoyalties'] += to_float(item['totalRoyalties'])
                aggregated_data[title]['totalRoyaltiesUSD'] += to_float(item['totalRoyaltiesUSD'])
            else:
                aggregated_data[title] = {
                    'bookTitle': title,
                    'eBookRoyalties': to_float(item['eBookRoyalties']),
                    'printRoyalties': to_float(item['printRoyalties']),
                    'kenpRoyalties': to_float(item['kenpRoyalties']),
                    'totalRoyalties': to_float(item['totalRoyalties']),
                    'totalRoyaltiesUSD': to_float(item['totalRoyaltiesUSD']),
                }

        final_data = list(aggregated_data.values())
        for item in final_data:
            item['eBookRoyalties'] = f"{item['eBookRoyalties']:.2f}"
            item['printRoyalties'] = f"{item['printRoyalties']:.2f}"
            item['kenpRoyalties'] = f"{item['kenpRoyalties']:.2f}"
            item['totalRoyalties'] = f"{item['totalRoyalties']:.2f}"
            item['totalRoyaltiesUSD'] = f"{item['totalRoyaltiesUSD']:.2f}"

        print("Aggregated royalty data:")
        print(final_data)

        royalties = await royalty_crud.upsert_royalty_data(session, payload.accountIdentifier, final_data)
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

@router.patch("/{royalty_id}/link", response_model=RoyaltyRead)
async def link_royalty_to_portfolio(
    royalty_id: int,
    link_request: LinkPortfolioRequest,
    session: AsyncSession = Depends(get_session),
):
    """
    Links a royalty to a portfolio.
    """
    royalty = await royalty_crud.get_royalty_by_id(session, royalty_id)
    if not royalty:
        raise HTTPException(status_code=404, detail="Royalty not found")

    portfolio = await portfolio_crud.get_portfolio_by_id(session, link_request.portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")

    updated_royalty = await royalty_crud.link_portfolio(session, royalty, portfolio.id)
    return updated_royalty


@router.patch("/{royalty_id}/unlink", response_model=RoyaltyRead)
async def unlink_royalty_from_portfolio(
    royalty_id: int,
    session: AsyncSession = Depends(get_session),
):
    """
    Unlinks a royalty from a portfolio.
    """
    royalty = await royalty_crud.get_royalty_by_id(session, royalty_id)
    if not royalty:
        raise HTTPException(status_code=404, detail="Royalty not found")

    updated_royalty = await royalty_crud.unlink_portfolio(session, royalty)
    return updated_royalty
