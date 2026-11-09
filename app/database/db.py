import sqlite3
from pathlib import Path
from app.config import settings

SCHEMA = """
CREATE TABLE IF NOT EXISTS cycles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at TEXT NOT NULL,
    status TEXT NOT NULL,
    details TEXT
);
CREATE TABLE IF NOT EXISTS fixtures (
    id TEXT PRIMARY KEY,
    sport TEXT NOT NULL,
    competition TEXT,
    home_name TEXT,
    away_name TEXT,
    start_time TEXT NOT NULL,
    source TEXT NOT NULL,
    fetched_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fixture_id TEXT NOT NULL,
    market TEXT NOT NULL,
    selection TEXT NOT NULL,
    odds REAL,
    estimated_probability REAL,
    implied_probability REAL,
    expected_value REAL,
    confidence_label TEXT,
    data_quality TEXT NOT NULL,
    model_version TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'candidate',
    FOREIGN KEY(fixture_id) REFERENCES fixtures(id)
);
CREATE TABLE IF NOT EXISTS results (
    prediction_id INTEGER PRIMARY KEY,
    outcome TEXT NOT NULL,
    settled_at TEXT NOT NULL,
    closing_odds REAL,
    FOREIGN KEY(prediction_id) REFERENCES predictions(id)
);
"""

def connect() -> sqlite3.Connection:
    path: Path = settings.database_path
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    con.executescript(SCHEMA)
    return con
