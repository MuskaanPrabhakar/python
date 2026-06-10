#wap to take input as sentence capitalized, lower, upper, split, etc
user = input("Enter a line of text: ")
print(f"Capitalized: {user.capitalize()}")
print(f"lowercase : {user.lower()}")
print(f"Uppercase : {user.upper()}")
print(f"Striped : {user.strip()}")
print(f"Split : {user.split()}")
for ch in user:
    print(ch)
for ch in enumerate(user):
    print(ch)
for key, value in enumerate(user):
    print(f"Index: {key}, Character: {value}")
userr=""
for word in user.split():
    userr+= word.capitalize()+ " "
print(userr)