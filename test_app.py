import pytest
from finance import savings_goal, remaining_income

def test_savings_goal():
    assert savings_goal(5000, 20) == 1000

def test_remaining_income():
    assert remaining_income(5000, 3200) == 1800

def test_invalid_percentage():
    with pytest.raises(ValueError):
        savings_goal(5000, 150)

def test_negative_expenses():
    with pytest.raises(ValueError):
        remaining_income(5000, -100)