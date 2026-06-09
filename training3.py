#str =8
#print(help(str)) #help function is used to get the documentation of the object passed as an argument 
str=8
#print(help(str)) #help function is used to get the documentation of the object passed as an argument but it points to memery address of the variable str which is an integer now and it is not a string anymore
str="muskaan Prabhakar"
print(str)
string= str.capitalize() #capitalize is used to convert the first character of the string to uppercase and the rest of the characters to lowercase
print(string)
string="MUSKAAN PRABHAKAR"
string= string.lower() #lower is used to convert all the characters of the string to lowercase
print(string)
string= string.split() #split is used to split the string into a list of substrings based on the specified separator and it returns a list of substrings
print(string)
string="MUSKAAN PRABHAKAR"
string= string.split(" ")   #split is used to split the string into a list of substrings based on the specified separator and it returns a list of substring
print(string)
string= "  msuaka oarnf "
print(string.strip()) #strip is used to remove the leading and trailing whitespace characters from the string and it returns a new string with the whitespace characters removed
print(list(string)) #list is used to convert the string into a list of characters and it returns a list of characters
string="MUSKAAN PRABHAKAR"
for ch in string:
    print(ch) #for loop is used to iterate over a sequence of characters in the string and it prints each character in the string
for ch in enumerate(string):
    print(ch) #enumerate is used to get the index and the value of each character in the string and it returns a tuple containing the index and the value of each character in the string
for key, value in enumerate(string):
    print(f"Index: {key}, Character: {value}") #f string is used to format the string and it is available in python 3.6 and above
#string(start,stop, step) is used to slice the string and it returns a new string that is a substring of the original string based on the specified start, stop, and step values by default step is 1
print(string[0:5]) #string slicing is used to get a substring of the original string based on the specified start and stop values and it returns a new string that is a substring of the original string
print(string[0:10:2]) #string slicing is used to get a substring of the original string based on the specified start, stop, and step values and it returns a new string that is a substring of the original string
abc= "abcdefgh"
print(abc[::-1]) #reverse
a= [1,2,3,4]
a[-4]=5
print(a)
a.append(6)
print(a)
a.insert(0, 0) #insert is used to add an element at a specific index in the list and it takes two arguments the first argument is the index and the second argument is the element to be added
print(a)
print(a.reverse()) #reverse is used to reverse the order of the elements in the list and it returns None because it modifies the original list
print(a.pop()) #pop is used to remove and return the last element from the list
a.sort() #sort is used to sort the elements in the list in ascending order and it returns None because it modifies the original list
print(a)
print(a.sort(reverse=True)) #sort is used to sort the elements in the list in descending order and it returns None because it modifies the original list
print(a[0:3]) #list slicing is used to get a sublist of the original list based on the specified start and stop values and it returns a new list that is a sublist of the original list
print(a.count(4)) #count is used to count the number of occurrences of a specific element in the list and it returns the count of the specified element in the list
a.index(4) #index is used to get the index of the first occurrence of a specific element in the list and it returns the index of the specified element in the list
print(a.index(4)) #index is used to get the index of the first occurrence of a specific element in the list and it returns the index of the specified element in the list
#string.replace(old, new, count)