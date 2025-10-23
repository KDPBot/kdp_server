from pydantic_settings import BaseSettings, SettingsConfigDict
from datetime import timedelta

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:quHgWyGZsgCTcehtsmsaZxsvMMayECdV@caboose.proxy.rlwy.net:15764/railway"
    SECRET_KEY: str = "YOUR_SUPER_SECRET_KEY"  # Change this!
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
