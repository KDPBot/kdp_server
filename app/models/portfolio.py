from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime

class PortfolioBase(SQLModel):
    account_identifier: str = Field(index=True)
    portfolio_name: str
    spend: str

class Portfolio(PortfolioBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class PortfolioCreate(PortfolioBase):
    pass

class PortfolioRead(PortfolioBase):
    id: int
    created_at: datetime
    updated_at: datetime
