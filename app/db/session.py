from typing import AsyncGenerator
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.core.settings import settings

# Create the async engine
engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL, echo=True, pool_pre_ping=True
)

async def init_db():
    """
    Initializes the database by creating all tables defined in SQLModel metadata.
    """
    async with engine.begin() as conn:
        # Drop all tables and then create them (for development/testing)
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database initialized successfully.")

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency that provides an async database session.
    """
    async with AsyncSession(engine) as session:
        yield session
