
# 🟢 Abstraction কি?
# 👉 Abstraction = unnecessary details hide করে only important part দেখানো
# 👉 Abstraction = hiding the implementation details and showing only functionality to the user
# 🟢 Abstraction এর সুবিধা
# 👉 Abstraction code কে more flexible করে তোলে 
# 👉 Abstraction code কে more maintainable করে তোলে
# 👉 Abstraction code কে more secure করে তোলে
# 🟢 Abstraction কিভাবে implement করা হয়?
# 👉 Abstraction implement করার জন্য আমরা abstract class এবং interface ব্যবহার করতে পারি
# 👉 Abstract class = একটি class যা abstract
# 👉 Interface = একটি class যা শুধুমাত্র method declaration থাকে এবং কোন implementation থাকে না

# 1.Example of Abstraction in Python 
from abc import ABC, abstractmethod

class Animal(ABC): # Abstract class 

   @abstractmethod # method declaration
   def sound(self):
      pass

class Dog(Animal): # Subclass of Animal
   def sound(self):
      return "Woof"
   
class Cat(Animal):
   def sound(self):
      return "Meow"
   
d = Dog()
print(d.sound())
c = Cat()
print(c.sound())
# a = Animal() # 👉 Abstract class এর object create করা যায় না

# 2.Exmaple of Mutiple Methods in Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):

   @abstractmethod
   def area(self):
      pass

class Circle(Shape):
   def area(self):
      return 3.14 * 5 * 5
   
class Rectangle(Shape):
   def area(self):
      return 5 * 10
   
c = Circle()
print(c.area())
r = Rectangle()
print(r.area())

# 3.Example of Abstraction with Constructor
from abc import ABC, abstractmethod

class Vehicle(ABC):

   def __init__(self, name):
      self.name = name

   @abstractmethod
   def run(self):
      pass

class Car(Vehicle):
   def run(self):
      return f"{self.name} is running"
   
class Bike(Vehicle):
   def run(self):
      return f"{self.name} is running"
   
c = Car("Toyota")
print(c.run())
b = Bike("Honda")
print(b.run())

# Quick Revision
# Abstraction = hide logic and show only functionality
# abstract class = blueprint of a class
# abstract method = method without implementation
# abstract class এর object create করা যায় না
# abstract class কে subclass করে method implement করতে হয়
# child class কে parent class এর method implement করতে হয়
# abstraction code কে more flexible, maintainable এবং secure করে তোলে
# abstraction implement করার জন্য abstract class এবং interface ব্যবহার করা হয়



