def savings_goal(monthly_income, percentage):
    return monthly_income * (percentage / 100)

if __name__ == "__main__":
    print("Savings target amount:", savings_goal(5000, 20))

def remaining_income(income, expenses):
    return income - expenses
print("Remaining income:", remaining_income(5000, 3200))