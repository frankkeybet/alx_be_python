
income = input("Enter your monthly income: ")
expenses = input("Enter your monthly expenses: ")
monthly_savings = int(income) - int(expenses)
projected_savings = int(monthly_savings * 12 +(monthly_savings * 0.05 * 12))

print("Your Monthly savings are:", monthly_savings)
print("Your Projected savings for the year are:", projected_savings) 