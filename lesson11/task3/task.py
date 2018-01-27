# Replace the placeholders with code and run the Python program

# Define class Automobile
class Automobile():
    def __init__(self,ndoors=0,clr=""):
        self._doors = ndoors
        self._colour = clr

    def printDoors(self):
        return "Number of doors is: "+str(self._doors)

    def printColour(self):
        return "Colour is: "+self._colour

    def display(self):
        return "Car is: "+str(self._doors)+" doors,"+self._colour

# Define class SportsCar
class SportsCar(Automobile):
    def Define the constructor:
        Use the constructor in the super class
        Initialize the instance variable 'engine'

    def Define the override method 'display':
        return Specify what to return

# Define class Convertible
class Convertible(SportsCar):
    def Define the constructor:
        Use the constructor from the super class
        Initialize the instance variable 'top'

    def Override the method 'display':
        return Specify what to return

# Create some objects and test the methods
acar=Automobile(4,"green")
print("A car: ",acar.display())

scar = SportsCar(2,"yellow",350)
print(scar.printDoors())
print(scar.printColour())
print("My sports car: ",scar.display())

conv1 = Convertible(2,"red",425,"soft")
print(conv1.printDoors())
print(conv1.printColour())
print("My sports car: ",conv1.display())

