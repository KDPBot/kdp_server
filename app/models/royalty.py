from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from .portfolio import Portfolio

class RoyaltyBase(SQLModel):
    account_identifier: str = Field(index=True)
    book_title: str
    ebook_royalties: str
    print_royalties: str
    kenp_royalties: str
    total_royalties: str
    total_royalties_usd: str
    last_month_royalty: Optional[str] = Field(default=None)
    portfolio_id: Optional[int] = Field(default=None, foreign_key="portfolio.id", index=True)

class Royalty(RoyaltyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})
    portfolio: Optional["Portfolio"] = Relationship(back_populates="royalties")

class RoyaltyCreate(RoyaltyBase):
    pass

class RoyaltyRead(RoyaltyBase):
    id: int
    updated_at: datetime
