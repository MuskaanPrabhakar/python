#Write a program that takes a list of numbers from the user (comma-separated input), then uses a while loop to keep removing the largest number until the list is empty, printing the list state after each removal.
listt = input("Enter your list of numbers separating them by comma: ")
items = [item.strip() for item in listt.split(",")]
print(items)
while len(items)!=0:
    maxi= max(items)
    items.remove(maxi)
    print(items)