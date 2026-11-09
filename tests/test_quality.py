from app.data.contracts import DataCoverage
from app.intelligence.quality import assess_data_quality

def test_missing_odds_blocks_candidate():
    coverage = DataCoverage("hockey", "NHL", True, True, True, True, False)
    decision = assess_data_quality(coverage)
    assert not decision.eligible_for_model
    assert "Cote vérifiable manquante" in decision.reasons

def test_complete_minimum_coverage_passes_gate():
    coverage = DataCoverage("football", "test", True, True, False, False, True)
    assert assess_data_quality(coverage).eligible_for_model
