from typing import List
from sqlmodel import select, delete
from sqlmodel.ext.asyncio.session import AsyncSession
from app.models.royalty import Royalty, RoyaltyCreate
from datetime import date, timedelta

async def create_royalty_data(session: AsyncSession, account_identifier: str, royalty_data: List[dict]) -> List[Royalty]:
    """
    Adds new royalty data for a given account identifier to the database.
    It first deletes all existing data for that account identifier and then inserts the new data
    within a single atomic transaction.
    """
    # Step 1: Delete existing data for the given account_identifier.
    delete_statement = delete(Royalty).where(Royalty.account_identifier == account_identifier)
    await session.exec(delete_statement)

    # Step 2: Create new royalty objects from the payload.
    created_royalties = []
    today = date.today()
    is_last_day_of_month = (today + timedelta(days=1)).day == 1

    for item in royalty_data:
        royalty_in = RoyaltyCreate(
            account_identifier=account_identifier,
            book_title=item['bookTitle'],
            ebook_royalties=item['eBookRoyalties'],
            print_royalties=item['printRoyalties'],
            kenp_royalties=item['kenpRoyalties'],
            total_royalties=item['totalRoyalties'],
            total_royalties_usd=item['totalRoyaltiesUSD'],
            last_month_royalty=item['totalRoyaltiesUSD'] if is_last_day_of_month else None,
        )
        royalty = Royalty.model_validate(royalty_in)
        session.add(royalty)
        created_royalties.append(royalty)

    # Step 3: Commit the entire transaction (delete and adds).
    await session.commit()

    # Step 4: Refresh each object to get DB-assigned values like IDs.
    for royalty in created_royalties:
        await session.refresh(royalty)

    return created_royalties

async def get_all_royalties(session: AsyncSession) -> List[Royalty]:
    """
    Fetches all royalty data from the database asynchronously.
    """
    statement = select(Royalty)
    result = await session.exec(statement)
    royalties = result.all()
    return list(royalties)
