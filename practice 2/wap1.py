#Write a program that simulates a simple inventory system using a dictionary. Support operations: add item with quantity, remove item, update quantity, search item, print all items sorted by quantity. Run it in a loop until user types "exit".
erasers= int(input("Enter no. of erasers: "))
sharpeners= int(input("Enter no. of sharpeners: "))
pencils= int(input("Enter no. of pencils: "))
pens= int(input("Enter no. of pens: "))
inv = {"erasers": erasers, "sharpeners": sharpeners , "pencils": pencils , "pens": pens}
exit= False
while exit!=True:
    user= user.split(input("Enter 'all' or 'erasers' or 'sharpeners' or 'pencils' or 'pens' to check their respective inventory: "))
    if(user=="all"):
        print(inv)
    else:
        print(inv.get(user))
    user= user.split(input("Enter 'add' to add item with quantity, 'remove' to remove item, 'update' "))
    