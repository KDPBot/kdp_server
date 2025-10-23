from typing import Optional
from sqlmodel import Session, select
from app.models.user import User, UserCreate
from app.core.security import get_password_hash

async def get_user_by_email(session: Session, email: str) -> Optional[User]:
    """
    Retrieves a user by their email address.
    """
    statement = select(User).where(User.email == email)
    result = await session.exec(statement)
    return result.first()

async def create_user(session: Session, user_create: UserCreate) -> User:
    """
    Creates a new user in the database.
    """
    hashed_password = get_password_hash(user_create.password)
    user = User(email=user_create.email, hashed_password=hashed_password)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
