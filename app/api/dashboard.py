import re
from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.session import get_session
from app.crud import portfolio_crud, royalty_crud
from app.schemas.dashboard import DashboardData, LinkedPortfolio
from app.models.portfolio import PortfolioRead

router = APIRouter()

def natural_sort_key(s):
    """
    A key for natural sorting. Extracts numbers from a string and returns them as integers.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

@router.get("/", response_model=DashboardData)
async def get_dashboard_data(session: AsyncSession = Depends(get_session)):
    """
    This endpoint provides a consolidated view of all royalties and portfolios,
    categorized into linked, unlinked royalties, and unlinked portfolios.
    """
    portfolios = await portfolio_crud.get_all_portfolios(session)
    royalties = await royalty_crud.get_all_royalties(session)

    linked_portfolios = sorted(
        [LinkedPortfolio.model_validate(p) for p in portfolios if p.royalties],
        key=lambda p: natural_sort_key(p.portfolio_name)
    )
    unlinked_portfolios = sorted(
        [PortfolioRead.model_validate(p) for p in portfolios if not p.royalties],
        key=lambda p: natural_sort_key(p.portfolio_name)
    )
    unlinked_royalties = sorted(
        [r for r in royalties if r.portfolio_id is None],
        key=lambda r: natural_sort_key(r.book_title)
    )

    return DashboardData(
        linked_portfolios=linked_portfolios,
        unlinked_royalties=unlinked_royalties,
        unlinked_portfolios=unlinked_portfolios,
    )
