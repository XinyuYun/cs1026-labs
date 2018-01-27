# Replace the placeholders with code and run the Python program

# Define class Fruit
class Fruit():
    def __init__(self,clr="",shp="",tst=""):
        Define attribute 'colour'
        Define attribute 'shape'
        Define attribute 'taste'

    def setColour(self,value):
        self._colour = value

    def setShape(self,value):
        self._shape = value

    def setTaste(self,value):
        self._taste = value

    def Define the header for method 'descriptor':
        return self._colour+","+self._shape+","+self._taste

# Define class Banana
class Banana(Fruit):
    def __init__(Define the header for initializing a Banana):
        super().Invoke the initialize method of the Fruit class

# Define class Apple
class Apple(Fruit):
    def __init__(Define the header for initializing an Apple):
        super().Invoke the initialize method of the Fruit class
        self._type=""

    def setType(self,value):
        self._type = value

    def descriptor(self):
        Define the override 'descriptor' method for the Apple class

# Create some objects and test the methods
afruit=Fruit("green","round","sweet")
print("A fruit: ",afruit.descriptor())
bn = Banana("yellow","long","soft and sweet")
print("A banana: ",bn.descriptor())

app1 = Apple("red","round","sweet and crunchy")
print("An apple: ",app1.descriptor())
app1.setType("Gala")
print("A particular apple: ",app1.descriptor())
