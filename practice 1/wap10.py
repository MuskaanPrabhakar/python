#Build a number guessing game. Generate a random number between 1 and 100. Give the user unlimited attempts. After each wrong guess, say "Too high" or "Too low". Count attempts and print them when the user wins.
import random 
win =0
k=" "
num1 = input("Enter your guess: ")
attempt=1
while num1!="quit":
    num = str(random.randint(1, 100))
    print(num)
    while num!=num1 and  num1!="quit":
        if(num1<num):
            print("TOO LOW")
        else: 
            print("TOO HIGH")
        print(f"Your attempts: {attempt}, win: {win}, lose: {attempt-win}")
        num1=input("enter 'quit' to leave or else enter your guess between 0 and 100: ")
        if(num1=="quit"):
            break
        attempt+=1
    if(num1!="quit"): 
        win+=1
        print(f"Your attempts: {attempt}, win: {win}, lose: {attempt-win}")
        num1 = input("Oh, ho, you won, Enter your new guess or 'quit' to quit: ")