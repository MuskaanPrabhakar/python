#inheritance in python
#inheritance in python
class Parents:
    def __init__(self):
        print("Parent class constructor")
class Children(Parents):
    pass
obj = Children()

class Parent:
    def __init__(self):
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        print("Child class constructor") #overrides therefore parent is not called, instead child is called
obj = Child()

class Pparent:
    def __init__(self):
        print("Parent class constructor")
class Cchild(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor") #user super(). to avoid override 
obj = Cchild()

class ABC():
    def __init__(self):
        self._a=0

    @property #python treating it as a variable
    def a(self):
        return self._a

val = ABC()
print(val.a) #we don't call property as val.a()

class ABCD():
    def __init__(self):
        self._value=0
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self._value= value
        
obj = ABCD()
obj._value =19
print(obj.value)

#polymorphism and encapsulation