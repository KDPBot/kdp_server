from typing import List
from sqlmodel import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from app.models.portfolio import Portfolio, PortfolioCreate
from app.models.royalty import Royalty

async def upsert_portfolio_data(session: AsyncSession, account_identifier: str, portfolio_data: List[dict]) -> List[Portfolio]:
    """
    Upserts portfolio data for a given account identifier.
    It updates existing portfolios, creates new ones, and deletes any that are no longer present.
    """
    # Step 1: Fetch existing portfolios for the account
    existing_portfolios_statement = select(Portfolio).where(Portfolio.account_identifier == account_identifier)
    result = await session.exec(existing_portfolios_statement)
    existing_portfolios_map = {p.portfolio_name: p for p in result.all()}

    # Step 2: Process incoming data
    incoming_portfolio_names = {item['portfolio_name'] for item in portfolio_data}
    processed_portfolios = []

    for item in portfolio_data:
        portfolio_name = item['portfolio_name']
        spend = item['spend']

        if portfolio_name in existing_portfolios_map:
            # Update existing portfolio
            portfolio = existing_portfolios_map[portfolio_name]
            portfolio.spend = spend
            session.add(portfolio)
            processed_portfolios.append(portfolio)
        else:
            # Create new portfolio
            new_portfolio = Portfolio(
                account_identifier=account_identifier,
                portfolio_name=portfolio_name,
                spend=spend
            )
            session.add(new_portfolio)
            processed_portfolios.append(new_portfolio)

    # Step 3: Delete portfolios that are no longer present
    portfolios_to_delete = [p for name, p in existing_portfolios_map.items() if name not in incoming_portfolio_names]
    for portfolio in portfolios_to_delete:
        await session.delete(portfolio)

    # Step 4: Commit the transaction
    await session.commit()

    # Step 5: Refresh objects to get DB-assigned values
    for portfolio in processed_portfolios:
        await session.refresh(portfolio)

    return processed_portfolios

async def get_all_portfolios(session: AsyncSession) -> List[Portfolio]:
    """
    Fetches all portfolio data from the database asynchronously,
    eagerly loading the related royalties.
    """
    statement = select(Portfolio).options(selectinload(Portfolio.royalties))
    result = await session.exec(statement)
    portfolios = result.all()
    return list(portfolios)

async def get_portfolio_by_id(session: AsyncSession, portfolio_id: int) -> Portfolio | None:
    """
    Fetches a portfolio by its ID.
    """
    statement = select(Portfolio).where(Portfolio.id == portfolio_id)
    result = await session.exec(statement)
    return result.first()

async def delete_portfolio_by_account_id(session: AsyncSession, account_identifier: str):
    """
    Deletes all portfolio data for a given account identifier.
    """
    statement = delete(Portfolio).where(Portfolio.account_identifier == account_identifier)
    await session.exec(statement)
    await session.commit()
    return {"message": f"All portfolio data for account {account_identifier} has been deleted."}
