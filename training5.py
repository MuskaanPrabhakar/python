a = lambda x:x+1
print(a(5))

def abc():
    a = lambda a,b,c:a+b+c
    return a
a= abc()
print(a(1,2,3))

def abcs():
    a= lambda x:x+1
    b= lambda y:y*2
    return a,b

ay = abcs()
print(ay[0](1),ay[1](2))
