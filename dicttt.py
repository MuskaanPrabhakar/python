#dict 
name = input("Enter your name: ")
num = input("Enter your ph. no: ")
address = input("Enter your adress: ")
user= {"name": name, "num": num, "address": address}
print(user)
print(user.get("name"))
print(user["num"])
print(user.__getitem__("address"))
for x in user:
    print(x)
    print(user[x])
