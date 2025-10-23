from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class RoyaltyBase(SQLModel):
    account_identifier: str = Field(index=True)
    book_title: str
    ebook_royalties: str
    print_royalties: str
    kenp_royalties: str
    total_royalties: str
    total_royalties_usd: str
    last_month_royalty: Optional[str] = Field(default=None)

class Royalty(RoyaltyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class RoyaltyCreate(RoyaltyBase):
    pass

class RoyaltyRead(RoyaltyBase):
    id: int
    updated_at: datetime
