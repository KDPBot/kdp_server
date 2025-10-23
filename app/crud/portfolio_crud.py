from typing import List
from sqlmodel import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.portfolio import Portfolio, PortfolioCreate

async def create_portfolio_data(session: AsyncSession, account_identifier: str, portfolio_data: List[dict]) -> List[Portfolio]:
    """
    Adds new portfolio data for a given account identifier to the database.
    It first deletes all existing data for that account identifier and then inserts the new data
    within a single atomic transaction.
    """
    # Step 1: Delete existing data for the given account_identifier.
    # This is part of the same transaction and will be committed with the new data.
    delete_statement = delete(Portfolio).where(Portfolio.account_identifier == account_identifier)
    await session.exec(delete_statement)

    # Step 2: Create new portfolio objects from the payload.
    created_portfolios = []
    for item in portfolio_data:
        portfolio_in = PortfolioCreate(
            account_identifier=account_identifier,
            portfolio_name=item['portfolio_name'],
            spend=item['spend'],
        )
        portfolio = Portfolio.model_validate(portfolio_in)
        session.add(portfolio)
        created_portfolios.append(portfolio)

    # Step 3: Commit the entire transaction (delete and adds).
    await session.commit()

    # Step 4: Refresh each object to get DB-assigned values like IDs.
    for portfolio in created_portfolios:
        await session.refresh(portfolio)

    return created_portfolios

async def get_all_portfolios(session: AsyncSession) -> List[Portfolio]:
    """
    Fetches all portfolio data from the database asynchronously.
    """
    statement = select(Portfolio)
    result = await session.exec(statement)
    portfolios = result.all()
    return list(portfolios)
