def savings_goal(monthly_income, percentage):
    return monthly_income * (percentage / 100)

if __name__ == "__main__":
    print("The Savings target::", savings_goal(5000, 20))
    