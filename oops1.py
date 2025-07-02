# initialize a class
class Employee:
    #special method/ magic method/ dunder method - constructor
    def __init__(self):
        print("Started executing attributes/ data") #gets called all by itself as soon as an ovject is made.
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/ data have been initiated")

    def travel(self, destination):
        print("This travel method was called manually") #requires us to call this method after we make the object.
        print(f"Employee is now travelling to {destination}")

# Creating an Object/ Instance of the class
sam = Employee()

# print(sam.id,sam.salary,sam.designation, "\n")
sam.travel("New York")

print(type(sam))