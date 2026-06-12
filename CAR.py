#parent class= vehicle, properties:- no.of tyres, fuel type
#child class car, model, update properties
class Vehicle:
    def __init__(self):
        self.tyres = [2, 3, 4]
        self.fuel_types = ["petrol", "diesel", "electric"]

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.tyres = 4

class Swift(Car):
    def __init__(self):
        super().__init__()
        self.model = "Maruti Suzuki Swift ZXi Plus AMT DT"
        self.fuel_type = "petrol"

    def display(self):
        print("No. of tyres:", self.tyres)
        print("Fuel type:", self.fuel_type)
        print("Model:", self.model)

obj = Swift()
obj.display()

class Last(Swift, Car, Vehicle): #follow class heirarchy MRO-> METHOD RESOLTUION ORDER, child preceding with their parents
    pass
l= Last()
l.display()