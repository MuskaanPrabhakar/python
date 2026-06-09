a=45.5
b=9
#arithmetic operators
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication     
print(a/b) #division
print(a//b) #floor division
print(a%b) #modulus
print(a**b) #exponentiation
a=input("Enter a number: ") #input function is used to take input from the user and it returns a string
b=int(input("Enter another number: ")) #int function is used to convert the string input to an integer
print(f"Sum of {a} and {b} is: {int(a)+b}") #f string is used to format the string and it is available in python 3.6 and above
if int(a)>int(b): #True =1 and False =0 in python
    print(f"{a} is greater than {b}")       
elif int(a)<int(b):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")   
for i in range(5): #for loop is used to iterate over a sequence of numbers and it is defined using the range function range uses tuple to generate a sequence of numbers and it is defined using the range function
    print(i)

pass #pass is used as a placeholder for code that is not yet implemented and it does nothing when executed
#continue is used to skip the current iteration of the loop and move to the next iteration
#break is used to exit the loop when a certain condition is met
#None for undefined behaviour in python and it is a special constant that represents the absence of a value or a null value
#id memory address of the object in python and it is a built in function that returns the memory address of the object passed as an argument
print(id(a))