#calculator inifinite time using if elif or else statements
a=input("Enter operation you want to perform +, -, *, /, % :" ) #input function is used to take input from the user and it returns a string
while a!="quit":
    b=int(input("Enter first number: "))
    c=int(input("Enter second number: "))
    if(c==0 and (a=="/" or a=="divide" or a=="division")):
        print("Division by zero is not allowed")
    elif a=="+" or a=="add" or a=="addition":
        print(f"Sum of {b} and {c} is: {b+c}")
    elif a=="-" or a=="subtract" or a=="subtraction":
        print(f"Difference of {b} and {c} is: {b-c}")
    elif a=="*" or a=="multiply" or a=="multiplication":
        print(f"Product of {b} and {c} is: {b*c}")
    elif a=="/" or a=="divide" or a=="division":
        print(f"Quotient of {b} and {c} is: {b/c}")
    elif a=="%" or a=="modulus" or a=="mod":
        print(f"Remainder of {b} and {c} is: {b%c}")
    else:
        print("Invalid operation, enter +, -, *, /, %, add, subtract, multiply or divide or quit to exit")
    a=input("Enter operation you want to perform or enter 'quit' to exit:" )

