#Build a simple bill splitter. Take total bill amount, tax percentage, tip percentage, and number of people. Print each person's share with clean formatted output using f-strings with 2 decimal precision.
bill= float(input("Enter bill: "))
tax= float(input("Enter tax percentage: "))
tax= bill*tax/100
tip= float(input("Enter tip percentage: "))
tip= bill*tip/100
n = int(input("Enter no. of people: "))
bill+= tax+tip
print("Total bill ", bill)
bill/=n
print(f"Everyone give atleast {bill:.2f}")

