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
from app.models.portfolio import Portfolio
from app.schemas.kdp import KDPPayload

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite+aiosqlite:///./test_portfolio.db"
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
async def test_parse_portfolio_html(client: AsyncClient):
    html_content = """
    <div style="height: 50px; overflow: visible; position: relative; width: 1203px;">
        <div class="BottomLeftGrid_ScrollWrapper" style="left: 0px; overflow: hidden; position: absolute; height: 50px; width: 472px;">
            <div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid" role="grid" style="box-sizing: border-box; direction: ltr; height: 50px; position: absolute; width: 472px; will-change: transform; overflow: hidden auto; left: 0px;">
                <div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: 472px; height: 50px; max-width: 472px; max-height: 50px; overflow: hidden; position: relative;">
                    <div style="height: 50px; left: 0px; position: absolute; top: 0px; width: 472px;" data-e2e-id="tableCell_cell_name" data-e2e-index="cellIndex_0_0" data-udt-column-id="name-cell" class="sc-jxllNA iqzjfr">
                        <div class="styles-module__baseCellStyles_VxPntQ0I6YzClYStXxBm styles-module__hideOverflow_C16MGsAZ31g11z4fc3a6 styles-module__baseCellPadding_Dnk1Q6U3xO4ozhbHZk6p">
                            <div>
                                <a data-e2e-id="entityNameRenderer" title="01 - National Registry Paramedic Study Guide" id="A262GKTNS7B93Y" intl="[object Object]" class="sc-qPNpY gUSggg" href="/cm/portfolios/A262GKTNS7B93Y">Portfolio 1 Name</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid styles-module__bottomRightGridStyle_J1OWmZwvRdQwPXyG9a7_" role="grid" style="box-sizing: border-box; direction: ltr; height: 50px; position: absolute; will-change: transform; overflow: auto hidden; left: 472px; width: 731px;" tabindex="0">
            <div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: 1150px; height: 50px; max-width: 1150px; max-height: 50px; overflow: hidden; position: relative;">
                <div style="height: 50px; left: 540px; position: absolute; top: 0px; width: 105px;" data-e2e-id="tableCell_cell_spend" data-e2e-index="cellIndex_0_5" data-udt-column-id="spend-cell" class="sc-jxllNA iqzjfr">
                    <div class="styles-module__baseCellStyles_VxPntQ0I6YzClYStXxBm styles-module__hideOverflow_C16MGsAZ31g11z4fc3a6 styles-module__baseCellPadding_Dnk1Q6U3xO4ozhbHZk6p">
                        <div data-e2e-id="currencyRenderer" class="sc-pYOYC fXMHSK">$61.66<br></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div style="height: 50px; overflow: visible; position: relative; width: 1203px;">
        <div class="BottomLeftGrid_ScrollWrapper" style="left: 0px; overflow: hidden; position: absolute; height: 50px; width: 472px;">
            <div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid" role="grid" style="box-sizing: border-box; direction: ltr; height: 50px; position: absolute; width: 472px; will-change: transform; overflow: hidden auto; left: 0px;">
                <div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: 472px; height: 50px; max-width: 472px; max-height: 50px; overflow: hidden; position: relative;">
                    <div style="height: 50px; left: 0px; position: absolute; top: 0px; width: 472px;" data-e2e-id="tableCell_cell_name" data-e2e-index="cellIndex_0_0" data-udt-column-id="name-cell" class="sc-jxllNA iqzjfr">
                        <div class="styles-module__baseCellStyles_VxPntQ0I6YzClYStXxBm styles-module__hideOverflow_C16MGsAZ31g11z4fc3a6 styles-module__baseCellPadding_Dnk1Q6U3xO4ozhbHZk6p">
                            <div>
                                <a data-e2e-id="entityNameRenderer" title="02 - Another Portfolio" id="B123C456D789E012F345" intl="[object Object]" class="sc-qPNpY gUSggg" href="/cm/portfolios/B123C456D789E012F345">Portfolio 2 Name</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div aria-label="grid" aria-readonly="true" class="ReactVirtualized__Grid styles-module__bottomRightGridStyle_J1OWmZwvRdQwPXyG9a7_" role="grid" style="box-sizing: border-box; direction: ltr; height: 50px; position: absolute; will-change: transform; overflow: auto hidden; left: 472px; width: 731px;" tabindex="0">
            <div class="ReactVirtualized__Grid__innerScrollContainer" role="rowgroup" style="width: 1150px; height: 50px; max-width: 1150px; max-height: 50px; overflow: hidden; position: relative;">
                <div style="height: 50px; left: 540px; position: absolute; top: 0px; width: 105px;" data-e2e-id="tableCell_cell_spend" data-e2e-index="cellIndex_0_5" data-udt-column-id="spend-cell" class="sc-jxllNA iqzjfr">
                    <div class="styles-module__baseCellStyles_VxPntQ0I6YzClYStXxBm styles-module__hideOverflow_C16MGsAZ31g11z4fc3a6 styles-module__baseCellPadding_Dnk1Q6U3xO4ozhbHZk6p">
                        <div data-e2e-id="currencyRenderer" class="sc-pYOYC fXMHSK">$123.45<br></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """
    payload = KDPPayload(accountIdentifier="test_account_portfolio", htmlContent=html_content)
    response = await client.post("/api/portfolios/parse_portfolios", json=payload.model_dump())

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["portfolio_name"] == "Portfolio 1 Name"
    assert data[0]["spend"] == "$61.66"
    assert data[1]["portfolio_name"] == "Portfolio 2 Name"
    assert data[1]["spend"] == "$123.45"

@pytest.mark.asyncio
async def test_get_portfolios(client: AsyncClient, session: AsyncSession):
    portfolio_data = [
        Portfolio(
            account_identifier="test_account_portfolio",
            portfolio_name="Existing Portfolio 1",
            spend="$100.00",
        ),
        Portfolio(
            account_identifier="test_account_portfolio",
            portfolio_name="Existing Portfolio 2",
            spend="$200.00",
        ),
    ]
    session.add_all(portfolio_data)
    await session.commit()

    response = await client.get("/api/portfolios/portfolios")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["portfolio_name"] == "Existing Portfolio 1"
    assert data[1]["portfolio_name"] == "Existing Portfolio 2"
