from finance import savings_goal, remaining_income

def test_savings_goal():
    assert savings_goal(5000, 20) == 1000

def test_remaining_income():
    assert remaining_income(5000, 3200) == 1800