#Write a program that simulates a simple inventory system using a dictionary. Support operations: add item with quantity, remove item, update quantity, search item, print all items sorted by quantity. Run it in a loop until user types "exit".
d= {}
user=""
for i in range(int(input("To begin, enter number of items you want to add to your inventory: "))):
        key=input("Enter the item name: ")
        value=int(input(f"Enter {key}'s quantity: "))
        d[key]=value
while(user!="exit"):
    user=input("Enter 'add' to add item with quantity, 'remove' to remove an item from inventory, 'update' to update the quantity, 'search' to search an item, 'PRINT' to print sorted list of item or 'exit'to exit: ")
    if(user=="add"):
        key=input("Enter the new item name: ")
        value=int(input(f"Enter {key}'s quantity: "))
        d[key]=value
    elif(user=="remove"):
        del d[input("Enter the item you want to remove: ")]
    elif(user=="update"):
         key=input("Enter the item name to update it's quantity: ")
         value=int(input(f"Enter {key}'s quantity: "))
         d[key]=value
    elif(user=="search"):
         print(d.get(input("Enter the item you want to search: ")))
    elif(user=="PRINT"):
        print(dict(sorted(d.items(), key=lambda x: x[1])))