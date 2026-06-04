import dis
def test():
    a =5
    print(a)

dis.dis(test)
#converting it to byte code using "dis" module

a=-0
#print(help(a))
#help function is used to get the documentation of the object passed as an argument
#print is not a keyword but a built in function in python no print(print)
#type to check the type of the variable or class 
print(type(a))
print(a)

set={True, "abc", "abc", 5, 5.989} #no duplicacy and unordered collection of items in python is called set and it is defined using curly braces
print(set)

list1=[1,2,3,4.789,4,4, 5,"abc"] #list square brackets are used to define a list in python
print(list1)
list1.append(6) #append is used to add an element at the end of the list
print(list1)

list=(1,2,3,4.789,4,4, 5,"abc") #tuple round brackets are used to define a tuple in python values can't be changed in tuple but can be changed in list and tuple is faster than list because of immutability
#tuple is mutable and list is immutable
print(list)

a={"name":"abc", "age":25, "city":"xyz"} #dictionary curly braces are used to define a dictionary in python
print(a)