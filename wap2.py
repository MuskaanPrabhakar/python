#Build a unit converter that takes a number and converts it across at least 4 types: km to miles, kg to lbs, Celsius to Fahrenheit, USD to INR (hardcode the rate). Accept type of conversion and value from user input.
user = input("Enter 1 to convert km to miles, 2 to convert kg to lbs, 3 to convert celsius to fahrenheit, 4 to convert USD to INR: ")
val= float(input("Enter the value to convert: "))
if user == "1":
    print(f"{val} km is equal to {val*0.621371} miles")
elif user == "2":
    print(f"{val} kg is equal to {val*2.20462262} lbs")
elif user == "3":
    print(f"{val} celsius is equal to {val*9/5 + 32} fahrenheit")
elif user == "4":
    inr = input("Enter the current exchange rate of USD to INR or write 82.5: ")
    print(f"{val} USD is equal to {val*float(inr)} INR")
else:
    print("Invalid input")
