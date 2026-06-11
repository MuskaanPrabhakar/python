class ABC:
    a=10
print(ABC.a)

#CONSTRUCTOR 
class ABCD: #class ABCD()
    def __init__(self): #self or u could write name of class i.e. ABCD is ref of class and also 1 positonal arguement would be of class by default
    #self uses instance of class
        self.a=10
        print(self.a)

y = ABCD()

class calc:
    def addd(self,a,b):
        return a+b
    def subb(self,a,b):
        return a-b
a= calc()
print(a.addd(1,2))
print(a.subb(2,1))

#without self -> static methods -> not instance so use refer of class calc.a
class calc:
    @staticmethod
    def addd(a,b):
        return a+b
    @staticmethod
    def subb(a,b):
        return a-b
a= calc()
print(a.addd(1,2))
print(a.subb(2,1))
