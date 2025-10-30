from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import init_db
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.session import init_db
from app.api import royalties, portfolios, auth, dashboard

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    FastAPI lifespan event handler to initialize the database on startup.
    """
    await init_db()
    yield

app = FastAPI(
    title="KDP Backend API",
    description="API for parsing KDP royalty and portfolio data.",
    version="1.0.0",
    lifespan=lifespan,
)

origins = [
    "http://localhost:3000",  # Your Next.js frontend URL
    "*" # Allow all origins for now, refine in production
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(royalties.router, prefix="/api/royalties", tags=["royalties"])
app.include_router(portfolios.router, prefix="/api/portfolios", tags=["portfolios"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
