from typing import List
from sqlmodel import SQLModel
from app.models.royalty import RoyaltyRead
from app.models.portfolio import PortfolioRead

class LinkedPortfolio(PortfolioRead):
    royalties: List[RoyaltyRead] = []

class DashboardData(SQLModel):
    linked_portfolios: List[LinkedPortfolio]
    unlinked_royalties: List[RoyaltyRead]
    unlinked_portfolios: List[PortfolioRead]
