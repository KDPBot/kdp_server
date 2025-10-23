from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from bs4 import BeautifulSoup

from app.db.session import get_session
from app.schemas.kdp import KDPPayload
from app.models.portfolio import PortfolioRead
from app.crud import portfolio_crud

router = APIRouter()

@router.post("/parse_portfolios", response_model=List[PortfolioRead])
async def parse_portfolio_html(payload: KDPPayload, session: AsyncSession = Depends(get_session)):
    """
    This endpoint receives raw Advertising Portfolio HTML,
    parses it, extracts a list of portfolio names and their spend, and saves it to the database.
    """
    print(f"Received Portfolio HTML from account: {payload.accountIdentifier}")
    print("Starting Portfolio HTML parsing...")

    soup = BeautifulSoup(payload.htmlContent, 'lxml')

    try:
        extracted_data = []

        name_elements = soup.select('a[data-e2e-id="entityNameRenderer"]')
        spend_elements = soup.select('div[data-e2e-id="tableCell_cell_spend"] div[data-e2e-id="currencyRenderer"]')

        if not name_elements:
            print("Warning: No portfolio names found with selector 'a[data-e2e-id=\"entityNameRenderer\"]'")
        if not spend_elements:
             print("Warning: No spend values found with selector 'div[data-e2e-id=\"tableCell_cell_spend\"] div[data-e2e-id=\"currencyRenderer\"]'")

        for name_tag, spend_tag in zip(name_elements, spend_elements):
            name = name_tag.get_text(strip=True)
            spend = spend_tag.get_text(strip=True)

            extracted_data.append({
                "portfolio_name": name,
                "spend": spend
            })

        print("Successfully extracted portfolio data:")
        print(extracted_data)

        portfolios = await portfolio_crud.create_portfolio_data(session, payload.accountIdentifier, extracted_data)
        return portfolios

    except Exception as e:
        print(f"Error parsing Portfolio HTML: {e}")
        raise HTTPException(status_code=500, detail=f"Error parsing Portfolio HTML: {str(e)}")

@router.get("/portfolios", response_model=List[PortfolioRead])
async def get_portfolios(session: AsyncSession = Depends(get_session)):
    """
    This endpoint fetches all portfolio data from the database.
    """
    try:
        data = await portfolio_crud.get_all_portfolios(session)
        return data
    except Exception as e:
        print(f"Error fetching portfolios: {e}")
        raise HTTPException(status_code=500, detail=f"Error fetching portfolios: {str(e)}")
