#Write a program that takes a user's name, age, and monthly salary as input. Calculate and print: annual salary, salary after 30% tax deduction, and how many years until they turn 60.
nm= input("Enter your name: ") 
age= int(input("Enter your age: "))
salary= int(input("Enter your salary: "))
print("Your annual salary is: ", salary*12)
print("Your salary after 30% tax deduction [per month] is: ", salary*0.7)
print("Your salary after 30% tax deduction [per year] is: ", salary*0.7*12)
if age < 60:
    print("Total salary till age 60:", salary * (60 - age) * 12)
else:
    print("You have already reached age 60.")
