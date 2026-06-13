try: 
    age=input("Enter your age: ")
    if(int(age)<18):
        raise Exception("you are too young to vote")
    elif(int(age)>=110):
        raise Exception("Invalid")
    print("Voter card is applied")

except ValueError:
    print("Invalid characters are use instead of digit")

except Exception as e: 
    print(e)

# try:
#     a = int(input('Enter age'))
# except :
#     print(e)

# int(input("Enter")) ctrl+/ for comments