us = input("Enter your name: ")
age = int(input("Enter your age: "))
s = int(input("Enter your Grade 0-100: "))
if(s>90 and s<101):
    print(f"Grade A, {us}, don't let the grade define you, but let it motivate you to keep up the good work.")
elif(s>80 and s<91):
    print(f"Grade B, {us}, you are doing good and have a lot of potential.")
elif(s>70 and s<81):
    print(f"Grade C, {us}, you are doing good, but you can do better.")
elif(s>60 and s<71):
    print(f"Grade D, {us}, you need to work hard to improve your grade.")
elif(s>100):
    print(f"Enter a valid grade between 0 and 100, {us}.")
else:
    print(f"Grade F, {us}, you need to work hard to improve your grade.")