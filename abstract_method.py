

# Abstract Method কি?
# 👉 Abstract Method = এমন method যার body থাকে না (implementation থাকে না)
# 👉 শুধু declare করা হয়, implement করতে হবে child class এ

# 1. Basic Example:
from abc import ABC, abstractmethod

class Animal(ABC):

   @abstractmethod
   def sound(self):
      pass 

class Dog(Animal):
   def sound(self):
      print("Dog barks")

class Cat(Animal):
   def sound(self):
      print("Cat meows")

class Bird(Animal):
   pass

d = Dog()
d.sound()
c = Cat()
c.sound()
# b = Bird()
# b.sound()
# 👉 যদি abstract method implement না করো → object create করা যাবে না

# 2. Multiple Abstract Methods
from abc import ABC, abstractmethod

class Shape(ABC):
   @abstractmethod
   def area(self):
      pass 

   @abstractmethod
   def parameter(self):
      pass 

# child implementation
class Rectangle(Shape):
   def area(self):
      return 10 * 5
   
   def parameter(self):
      return 2 * (10 + 5)
   
r = Rectangle()
print(r.area())
print(r.parameter())

# Real-Life Example:
class Payment(ABC):

   @abstractmethod
   def pay(self):
      pass 

class Cash(Payment):
   def pay(self):
      print("Pay with cash")

class Card(Payment):
   def pay(self):
      print("Pay with card.")

# 👉 সব payment method-এ pay() implement করতেই হবে
# ⚠️ Common Interview Mistakes
# ❌ abstract method এ code লিখা
# ❌ child class এ implement না করা

# 🧠 Deep Concept
# 👉 Abstract class = rule book
# 👉 Abstract method = rule
# 👉 Child class = rule follow করে implementation দেয়

# 🔥 Quick Revision
# 👉 @abstractmethod ব্যবহার হয়
# 👉 body থাকে না
# 👉 child class must implement

# 🚀 Golden Rule
# Abstract method defines WHAT to do, child class defines HOW to do.

