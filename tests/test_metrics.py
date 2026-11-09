import pytest
from app.intelligence.metrics import assess_market

def test_market_assessment():
    result = assess_market(2.0, 0.55)
    assert result.implied_probability == 0.5
    assert result.expected_value == pytest.approx(0.10)

def test_invalid_odds_rejected():
    with pytest.raises(ValueError):
        assess_market(1.0, 0.5)

def test_invalid_probability_rejected():
    with pytest.raises(ValueError):
        assess_market(2.0, 1.0)
