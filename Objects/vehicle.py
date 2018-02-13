class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def printInfo(self):
        print(self.make, self.model, self.year)
        

car = Vehicle("BMW","M6","2018")
car.printInfo()