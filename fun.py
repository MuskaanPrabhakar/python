#functions
def hello():
    return "Namaste ji"
#definition of function
print(hello())
def users():
    a=int(input("Enter number: "))
    b=int(input("Enter number: "))
    return a+b
print(users())

def user(*args): #parameters and pass many arguements
    print(args)
user(8,9,7) #gives tuple

def userss(**kwargs): #to pass diff keywords arguements uses dict
    sum=0
    for i in kwargs.values():
        sum+=i
    print(sum)

userss(k=0, n=8, m=27)

def fun_name(*args):
    print(args)
    print(len(args))

list={}
fun_name(*list) # * unpack operators, we could use in kwargs

def fun_na(**kwargs):
    print(kwargs['key1'])

t={"key1": "value1","key2": "value2","key3": "value1"}
fun_na(**t)
