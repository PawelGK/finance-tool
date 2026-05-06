def savings_goal(monthly_income, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")
    return monthly_income * (percentage / 100)

def remaining_income(income, expenses):
    if expenses < 0:
        raise ValueError("Expenses cannot be negative")
    return income - expenses

if __name__ == "__main__":
    print("Savings target amount:", savings_goal(5000, 20))
    print("Remaining income:", remaining_income(5000, 3200))