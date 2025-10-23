from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, String
from pydantic import BaseModel, EmailStr, Field as PydanticField

class UserBase(SQLModel):
    email: EmailStr = Field(sa_column=Column(String, unique=True, index=True))

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str

class UserCreate(UserBase):
    password: str = PydanticField(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    message: Optional[str] = None # Added for custom messages in responses

class UserRead(UserBase):
    id: int
