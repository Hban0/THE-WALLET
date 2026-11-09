from dataclasses import dataclass
from math import isfinite

@dataclass(frozen=True)
class MarketAssessment:
    odds: float
    estimated_probability: float
    implied_probability: float
    expected_value: float

def assess_market(odds: float, estimated_probability: float) -> MarketAssessment:
    if not isfinite(odds) or odds <= 1.0:
        raise ValueError("La cote décimale doit être supérieure à 1.0")
    if not isfinite(estimated_probability) or not 0 < estimated_probability < 1:
        raise ValueError("La probabilité doit être comprise entre 0 et 1")
    implied = 1.0 / odds
    ev = estimated_probability * odds - 1.0
    return MarketAssessment(
        odds=odds,
        estimated_probability=estimated_probability,
        implied_probability=implied,
        expected_value=ev,
    )
