monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
interest = monthly_savings * interest_rate
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)
print(f"Monthly Savings: ${monthly_savings:.2f}")
print(f"Projected Savings (after interest): ${projected_savings:.2f}")
