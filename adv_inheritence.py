# # single or basic inheritence

# class Parent:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing")

# child = Child("Alice")
# child.greet()
# child.play()


# # Multilevel

# class Grandparent:
#     def __init__(self, name):
#         self.name = name
    
#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# class parent(Grandparent):
#     def work(self):
#         print(f"{self.name} is working")

# class Child(parent):
#     def play(self):
#         print(f"{self.name} is playing")

# child = Child("Charlie")
# child.tell_story()
# child.work()
# child.play()


# #Hierarchical Inheritence

# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# class Child1(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# class Child2(Parent):
#     def study(self):
#         print(f"{self.name} is studying.")

# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()
# child1.play()


# child2.greet()
# child2.study()

# Multiple Inheritence <Diamond Problem>

class A:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello from A, {self.name}.")

class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()

class C(A):
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()

class D(B, C):
    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet()

d = D("Frank")
d.greet()