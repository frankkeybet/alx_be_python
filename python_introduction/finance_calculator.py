# This is a simple finance calculator that computes monthly savings and projected annual savings with a 5% interest rate.

monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = float(monthly_income) - float(monthly_expenses)
projected_savings = float(monthly_savings * 12 +(monthly_savings * 0.05 * 12))

print("Your Monthly savings are:", monthly_savings)
print("Your Projected savings for the year are:", projected_savings)
