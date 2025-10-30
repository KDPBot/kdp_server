from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from bs4 import BeautifulSoup

from app.db.session import get_session
from app.schemas.kdp import KDPPayload
from app.models.portfolio import PortfolioRead
from app.crud import portfolio_crud, royalty_crud

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

        # Aggregate data to handle duplicates
        aggregated_data = {}
        for item in extracted_data:
            name = item['portfolio_name']
            spend_str = item['spend'].replace('$', '').replace(',', '').strip()
            try:
                spend = float(spend_str)
            except ValueError:
                spend = 0.0
            
            if name in aggregated_data:
                aggregated_data[name]['spend'] += spend
            else:
                aggregated_data[name] = {'portfolio_name': name, 'spend': spend}
        
        final_data = list(aggregated_data.values())
        for item in final_data:
            item['spend'] = f"${item['spend']:,.2f}"

        print("Aggregated portfolio data:")
        print(final_data)

        portfolios = await portfolio_crud.upsert_portfolio_data(session, payload.accountIdentifier, final_data)
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


@router.delete("/portfolios/{account_identifier}")
async def delete_all_data_by_account_identifier(account_identifier: str, session: AsyncSession = Depends(get_session)):
    """
    Deletes all portfolio and royalty data for a given account identifier.
    """
    try:
        await royalty_crud.delete_royalty_by_account_id(session, account_identifier)
        await portfolio_crud.delete_portfolio_by_account_id(session, account_identifier)
        return {"message": f"All data for account {account_identifier} has been deleted."}
    except Exception as e:
        print(f"Error deleting data for account {account_identifier}: {e}")
        raise HTTPException(status_code=500, detail=f"Error deleting data for account {account_identifier}: {str(e)}")
