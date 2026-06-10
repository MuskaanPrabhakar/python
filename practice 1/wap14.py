#Build a password validator using conditions. A valid password must be: at least 8 characters, contain at least one uppercase letter, one digit, and one special character. Print exactly which conditions are failing, not just "invalid".
cap=0; alph=0; n=0; spc=0; valid=False
while(valid!=True):
    password = input("Enter you password without using space or quotation mark or escape sequence : ")
    for i in range(len(password)):
        if password[i] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            cap+=1
            alph+=1
        elif password[i] in "qwertyuiopasdfghjklzxcvbnm":
            alph+=1
        elif password[i] in "1234567890":
            n+=1
        elif password[i] in "!#$%&'()*+,-./:;<=>?@[^_`{|}~":
            spc+=1
        else:
            print("Use characters, digits or special character")
            break
    else: 
        if cap==0:
            print("Enter atleast one CAPITAL letter")
            continue
        if alph<8:
            print(f"Enter atleast {8-alph} more alphabets")
            continue
        if n==0:
            print("Atleast add one digit")
            continue
        if spc==0:
            print("Atleast use one special character excluding quotation mark or escape sequence")
            continue
        valid=True
        print("password successful")
