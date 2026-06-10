#set is unordered, unchangeable, {} this would be dict by default
a={1.2,3,4,5}
b={7,9}
a.clear()
print(a)
a={1.2,3,4,5}
k=a.__contains__(3)
a.add(6)
print(a)
print(k)
val = a.intersection(b)
a= list(a)
a ={"key":"value"}
k= a.get("key")
print(k)
#immutuable can be use ; immutuable = can't be changed
#what is the use of empty tuple
