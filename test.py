import pytest
import pytest_asyncio
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.main import app
from app.db.session import get_session
from app.models.royalty import Royalty
from app.schemas.kdp import KDPPayload

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
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
async def test_parse_kdp_html(client: AsyncClient):
    html_content = """
        <div class="ui items no-margin unstackable">
            <div class="item">
                <div class="content">
                    <div class="ui equal width grid">
                        <div class="column">
                            <div class="ui padded equal width grid panel-new">
                                <div class="column">
                                    <div class="ui grid">
                                        <div class="row panel-title-new header-height">
                                            <div><i class="chevron right icon"></i></div>
                                        </div>
                                    </div>
                                </div>
                                <div class="column">
                                    <div class="ui vertically divided grid">
                                        <div class="row panel-title-new header-height">
                                            <div class="panel-title-new">
                                                <div class="ui container padded equal width grid floating-text header-height">
                                                    <div class="middle aligned five wide computer column table-header-text truncate-overflow">All 5 books</div>
                                                </div>
                                            </div>
                                            <div class="ui container padded equal width grid header-height">
                                                <div class="sixteen wide computer column table-header-text">
                                                    <div class="ui equal width grid header-height">
                                                        <div class="row">
                                                            <div class="computer only right aligned middle aligned two wide computer column">$0.00</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$55.86</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$0.79</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$56.65</div>
                                                            <div class="right aligned middle aligned two wide computer eight wide mobile eight wide tablet column">$56.65</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="item">
                <div class="content">
                    <div class="ui equal width grid">
                        <div class="column">
                            <div class="ui padded equal width grid panel-new">
                                <div class="column">
                                    <div class="ui grid">
                                        <div class="row panel-title-new header-height">
                                            <div><i class="chevron right icon"></i></div>
                                        </div>
                                    </div>
                                </div>
                                <div class="column">
                                    <div class="ui vertically divided grid">
                                        <div class="row panel-title-new header-height">
                                            <div class="panel-title-new">
                                                <div class="ui container padded equal width grid floating-text header-height">
                                                    <div class="five wide computer column">
                                                        <div class="ui grid header-height">
                                                            <div class="middle aligned column truncate-overflow">Book Title 1</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="ui container padded equal width grid header-height">
                                                <div class="sixteen wide computer column">
                                                    <div class="ui equal width grid header-height">
                                                        <div class="row">
                                                            <div class="computer only right aligned middle aligned two wide computer column">$1.00</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$2.00</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$3.00</div>
                                                            <div class="computer only right aligned middle aligned two wide computer column">$6.00</div>
                                                            <div class="right aligned middle aligned two wide computer eight wide mobile eight wide tablet column">$6.00</div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """
    payload = KDPPayload(accountIdentifier="test_account", htmlContent=html_content)
    response = await client.post("/api/royalties/parse", json=payload.model_dump())

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1  # Only one book entry, summary is skipped
    assert data[0]["book_title"] == "Book Title 1"
    assert data[0]["total_royalties_usd"] == "$6.00"

@pytest.mark.asyncio
async def test_get_royalties(client: AsyncClient, session: Session):
    royalty_data = [
        Royalty(
            account_identifier="test_account",
            book_title="Test Book 1",
            ebook_royalties="$1.00",
            print_royalties="$2.00",
            kenp_royalties="$3.00",
            total_royalties="$6.00",
            total_royalties_usd="$6.00",
        ),
        Royalty(
            account_identifier="test_account",
            book_title="Test Book 2",
            ebook_royalties="$0.50",
            print_royalties="$1.50",
            kenp_royalties="$2.00",
            total_royalties="$4.00",
            total_royalties_usd="$4.00",
        ),
    ]
    session.add_all(royalty_data)
    await session.commit()

    response = await client.get("/api/royalties/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["book_title"] == "Test Book 1"
    assert data[1]["book_title"] == "Test Book 2"
