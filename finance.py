def savings_goal(monthly_income, percentage):
    return monthly_income * (percentage / 100)

if __name__ == "__main__":
    print("Savings goal:", savings_goal(5000, 20))