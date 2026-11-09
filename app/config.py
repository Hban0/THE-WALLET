import os
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    timezone: str = os.getenv("APP_TIMEZONE", "Europe/Brussels")
    database_path: Path = Path(os.getenv("DATABASE_PATH", "data/the_wallet.sqlite3"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    telegram_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")

settings = Settings()
