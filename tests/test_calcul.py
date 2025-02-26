from src.compute_bmi import compute_bmi
import pytest


def test_bmi_calculation():
    assert compute_bmi(70, 1.75) == "healthy"
    assert compute_bmi(100, 1.75) == "obese"
    assert compute_bmi(50, 1.75) == "underweight"


def test_invalid_inputs():
    with pytest.raises(ValueError):
        compute_bmi(-70, 1.75)
    with pytest.raises(ValueError):
        compute_bmi(70, -1.75)
