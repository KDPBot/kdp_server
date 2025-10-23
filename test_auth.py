import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.main import app
from app.db.session import get_session
from app.models.user import User, UserCreate, Token
from app.core.security import get_password_hash

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite+aiosqlite:///./test_auth.db"
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def drop_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest_asyncio.fixture(name="session")
async def session_fixture():
    await create_db_and_tables()
    async with AsyncSession(engine) as session:
        yield session
    await drop_db_and_tables()

@pytest_asyncio.fixture(name="client")
async def client_fixture(session: AsyncSession):
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        yield client
    app.dependency_overrides.clear()

@pytest.mark.asyncio
async def test_register_user_success(client: AsyncClient):
    user_data = {"email": "test@example.com", "password": "securepassword"}
    response = await client.post("/auth/register", json=user_data)

    assert response.status_code == 201
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    assert token_data["message"] == "User registered successfully"
    assert "session" in response.cookies

@pytest.mark.asyncio
async def test_register_user_email_exists(client: AsyncClient, session: AsyncSession):
    # Pre-create a user
    hashed_password = get_password_hash("existingpassword")
    existing_user = User(email="existing@example.com", hashed_password=hashed_password)
    session.add(existing_user)
    await session.commit()

    user_data = {"email": "existing@example.com", "password": "newpassword"}
    response = await client.post("/auth/register", json=user_data)

    assert response.status_code == 409
    assert response.json()["detail"] == "Email already registered"

@pytest.mark.asyncio
async def test_login_success(client: AsyncClient, session: AsyncSession):
    # Register a user first
    user_create = UserCreate(email="login@example.com", password="loginpassword")
    hashed_password = get_password_hash(user_create.password)
    user = User(email=user_create.email, hashed_password=hashed_password)
    session.add(user)
    await session.commit()

    login_data = {"email": "login@example.com", "password": "loginpassword"}
    response = await client.post("/auth/login", json=login_data)

    assert response.status_code == 200
    token_data = response.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
    assert token_data["message"] == "Login successful"
    assert "session" in response.cookies

@pytest.mark.asyncio
async def test_login_incorrect_credentials(client: AsyncClient):
    login_data = {"email": "nonexistent@example.com", "password": "wrongpassword"}
    response = await client.post("/auth/login", json=login_data)

    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect email or password"

@pytest.mark.asyncio
async def test_protected_route_no_token(client: AsyncClient):
    response = await client.get("/auth/protected")
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

@pytest.mark.asyncio
async def test_protected_route_with_token(client: AsyncClient, session: AsyncSession):
    # Register and log in a user to get a valid session cookie
    user_create = UserCreate(email="protected@example.com", password="protectedpassword")
    hashed_password = get_password_hash(user_create.password)
    user = User(email=user_create.email, hashed_password=hashed_password)
    session.add(user)
    await session.commit()

    login_data = {"email": "protected@example.com", "password": "protectedpassword"}
    login_response = await client.post("/auth/login", json=login_data)
    session_cookie = login_response.cookies.get("session")

    # Access protected route with the session cookie
    response = await client.get("/auth/protected", cookies={"session": session_cookie})
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome, protected@example.com! You have access to protected data."
