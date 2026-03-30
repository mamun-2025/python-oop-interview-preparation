
# 1. Method Overriding
# 👉 Child class parent class এর method redefine করে
class Parent:
   def show(self):
      print("Parent class method")

class Child(Parent):
   def show(self):
      print("Child class method")

obj = Child()
obj.show() # Output: Child class method

# Child class এর show method parent class এর show method কে override করেছে।
# Runtime a decide হয় কোন method call হবে = Runtime Polymorphism

# 2. Method Overloading
# 👉 একই নামের method but different parameters
# Pythonic way:
class Calculator:
   def add(self, a, b):
      return a + b

   def add(self, a, b, c):
      return a + b + c
   
calc = Calculator()
# calc.add(2, 3) # This will raise an error because the first add method is overridden by the second one.
print(calc.add(2, 3, 4)) # Output: 9
# Python does not support method overloading in the traditional sense.

# Another way:
class Calculator:
   def add(self, *args):
      return sum(args)
   
calc = Calculator()
print(calc.add(2, 3))
print(calc.add(2, 3, 4))
print(calc.add(1, 2, 3, 4, 5))

# 3. Real-Life Example Overriding
class Payment:
   def pay(self):
      print("Pay by cash")

class Card(Payment):
   def pay(self):
      print("Pay by card")

obj1 = Payment()
obj1.pay() # Output: Pay by cash
obj2 = Card()
obj2.pay() # Output: Pay by card

# 4. Real-Life Example Overloading
def multiply(a, b, c=1):
   return a * b * c

print(multiply(2, 3))
print(multiply(2, 3, 5))

# Python supports method overloading directly (Wrong x)
# Python uses default args/*args
# Method Overriding is when a child class provides a specific implementation of a parent class method. Method Overloading refers to having multiple methods with the same but different parameters, which Python simulates using default arguments or args.
# Overriding = inheritance required
# Overloading = flexible arguments

