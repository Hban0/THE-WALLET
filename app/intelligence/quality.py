from dataclasses import dataclass
from app.data.contracts import DataCoverage

@dataclass(frozen=True)
class QualityDecision:
    eligible_for_model: bool
    reasons: tuple[str, ...]

def assess_data_quality(coverage: DataCoverage) -> QualityDecision:
    reasons: list[str] = []
    if not coverage.has_schedule:
        reasons.append("Calendrier manquant")
    if not coverage.has_recent_stats:
        reasons.append("Statistiques récentes manquantes")
    if not coverage.has_odds:
        reasons.append("Cote vérifiable manquante")
    return QualityDecision(not reasons, tuple(reasons))
