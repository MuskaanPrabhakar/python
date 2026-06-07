#Write a program that takes a string from the user and prints: total characters, total words, total vowels, and the string reversed — all using f-strings for output formatting.
user = input("Enter your name: ")
n= len(user) #len function is used to get the length of the string
tcr=0; tw=1; tv=0; nw=""
for i in range(n-1,-1,-1):
    nw+=user[i]
    if user[i] in "aeiouAEIOU":
        tv+=1
        tcr+=1
    elif user[i] in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
        tcr+=1
    elif user[i]== " " and ((n-1)!=i and i!=0) and (user[i+1]!=" " and user[i-1]!=" "):
        tw+=1
if n!=0 and user in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(f"Total characters: {n}, Total vowels: {tv}, Total alphabets: {tcr}, Total words: {tw}")
    print(f"Reversed name: {nw}")
else:   print("You have entered an empty string.")
    