from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

@dataclass(frozen=True)
class Fixture:
    fixture_id: str
    sport: str
    competition: str
    home_name: str
    away_name: str
    start_time: datetime
    source: str

@dataclass(frozen=True)
class DataCoverage:
    sport: str
    competition: str
    has_schedule: bool
    has_recent_stats: bool
    has_lineups: bool
    has_injuries: bool
    has_odds: bool
    notes: str = ""

    @property
    def prediction_ready(self) -> bool:
        return self.has_schedule and self.has_recent_stats and self.has_odds

class SportsDataProvider(Protocol):
    name: str
    async def get_fixtures(self, start: datetime, end: datetime) -> list[Fixture]: ...
    async def get_coverage(self, fixture: Fixture) -> DataCoverage: ...
