#Write a program that takes a string and uses a dictionary to count the frequency of each character (ignore spaces). Then use that dictionary to print a horizontal bar chart in terminal using * characters. More frequent = longer bar.
strr = input("Enter words: ")
strr= strr.split()
ch= {}
for word in strr:
    for char in word:
        ch[char]=ch.get(char,0)+1
for char, count in ch.items():
    print(f"{char}: {'*' * count}")