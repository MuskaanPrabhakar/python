#Write a type inference program. Ask the user to enter any value. Your program must detect and print whether it looks like an int, float, bool, or string — and then convert it to all other types, printing each result.
us = input("Enter int, string, float or boolean: ")
if us.isdigit():
    print(f"You have entered an integer: {int(us)}")
    print(f"The float of the integer you entered is: {float(us)}")
    print("The string of the integer you entered is: ", str(int(us)))
    if int(us)==1:
        print("The boolean of the integer you entered is: True")
    elif int(us)==0:
        print("The boolean of the integer you entered is: False")
    else:
        print("The boolean of the integer you entered is: None")
elif us.replace('.','',1).isdigit() and us.count('.') < 2:
    print(f"You have entered a float: {float(us)}")
    print(f"The integer of the float you entered is: {int(float(us))}")
    print("The string of the float you entered is: ", us)
    if int(float(us))==1:
        print("The boolean of the float you entered is: True")
    elif int(float(us))==0:
        print("The boolean of the float you entered is: False")
    else:
        print("The boolean of the float you entered is: None")
elif us.lower() in ["true", "false"]:
    print(f"You have entered a boolean: {us}")
    print(f"The integer of the boolean you entered is: {int(us.lower() == 'true')}")
    print(f"The float of the boolean you entered is: {float(us.lower() == 'true')}")
    print("The string of the boolean you entered is: ", us)
else:
    print(f"You have entered a string: {us}")
    print("The integer of the string you entered is: None")
    print("The float of the string you entered is: None")
    