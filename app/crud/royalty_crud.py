from typing import List
from sqlmodel import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import selectinload
from app.models.royalty import Royalty, RoyaltyCreate
from datetime import date, timedelta

async def upsert_royalty_data(session: AsyncSession, account_identifier: str, royalty_data: List[dict]) -> List[Royalty]:
    """
    Upserts royalty data for a given account identifier.
    It updates existing royalties, creates new ones, and deletes any that are no longer present.
    """
    # Step 1: Fetch existing royalties for the account
    existing_royalties_statement = select(Royalty).where(Royalty.account_identifier == account_identifier)
    result = await session.exec(existing_royalties_statement)
    existing_royalties_map = {r.book_title: r for r in result.all()}

    # Step 2: Process incoming data
    incoming_book_titles = {item['bookTitle'] for item in royalty_data}
    processed_royalties = []
    today = date.today()
    is_last_day_of_month = (today + timedelta(days=1)).day == 1

    for item in royalty_data:
        book_title = item['bookTitle']
        if book_title in existing_royalties_map:
            # Update existing royalty
            royalty = existing_royalties_map[book_title]
            royalty.ebook_royalties = item['eBookRoyalties']
            royalty.print_royalties = item['printRoyalties']
            royalty.kenp_royalties = item['kenpRoyalties']
            royalty.total_royalties = item['totalRoyalties']
            royalty.total_royalties_usd = item['totalRoyaltiesUSD']
            if is_last_day_of_month:
                royalty.last_month_royalty = item['totalRoyaltiesUSD']
            session.add(royalty)
            processed_royalties.append(royalty)
        else:
            # Create new royalty
            new_royalty = Royalty(
                account_identifier=account_identifier,
                book_title=item['bookTitle'],
                ebook_royalties=item['eBookRoyalties'],
                print_royalties=item['printRoyalties'],
                kenp_royalties=item['kenpRoyalties'],
                total_royalties=item['totalRoyalties'],
                total_royalties_usd=item['totalRoyaltiesUSD'],
                last_month_royalty=item['totalRoyaltiesUSD'] if is_last_day_of_month else None,
            )
            session.add(new_royalty)
            processed_royalties.append(new_royalty)

    # Step 3: Delete royalties that are no longer present
    royalties_to_delete = [r for title, r in existing_royalties_map.items() if title not in incoming_book_titles]
    for royalty in royalties_to_delete:
        await session.delete(royalty)

    # Step 4: Commit the transaction
    await session.commit()

    # Step 5: Refresh objects to get DB-assigned values
    for royalty in processed_royalties:
        await session.refresh(royalty)

    return processed_royalties

async def get_all_royalties(session: AsyncSession) -> List[Royalty]:
    """
    Fetches all royalty data from the database asynchronously.
    """
    statement = select(Royalty).options(selectinload(Royalty.portfolio))
    result = await session.exec(statement)
    royalties = result.all()
    return list(royalties)

async def get_royalty_by_id(session: AsyncSession, royalty_id: int) -> Royalty | None:
    """
    Fetches a royalty by its ID.
    """
    statement = select(Royalty).where(Royalty.id == royalty_id).options(selectinload(Royalty.portfolio))
    result = await session.exec(statement)
    return result.first()

async def link_portfolio(session: AsyncSession, royalty: Royalty, portfolio_id: int) -> Royalty:
    """
    Links a royalty to a portfolio.
    """
    royalty.portfolio_id = portfolio_id
    session.add(royalty)
    await session.commit()
    await session.refresh(royalty)
    return royalty

async def unlink_portfolio(session: AsyncSession, royalty: Royalty) -> Royalty:
    """
    Unlinks a royalty from a portfolio.
    """
    royalty.portfolio_id = None
    session.add(royalty)
    await session.commit()
    await session.refresh(royalty)
    return royalty

async def delete_royalty_by_account_id(session: AsyncSession, account_identifier: str):
    """
    Deletes all royalty data for a given account identifier.
    """
    statement = delete(Royalty).where(Royalty.account_identifier == account_identifier)
    await session.exec(statement)
    await session.commit()
    return {"message": f"All royalty data for account {account_identifier} has been deleted."}
