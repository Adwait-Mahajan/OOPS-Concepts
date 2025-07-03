# # Simple Inheritence

# # Base class
# class Animal:

#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Derived Class
# class Dog(Animal):
#     def __init__(self):
#         self.behavior = "Friendly"

#     def speak(self):
#         print(f"{self.name} barks. He is very {self.behavior}")

# # animal = Animal("Generic Animal")
# # animal.speak() #output would be "Generic Animal makes a sound"

# dog = Dog()
# dog.speak() #output would be "Buddy barks"


# Super Keyword

class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, breed):
        super().__init__() #we inherit this method __init()__ from the parent class
        self.breed = breed

    def speak(self):
        super().speak() #call the Parent class method
        print(f"{self.name} barks. It is a {self.breed}")

dog = Dog("Golden Retriever")
dog.speak()