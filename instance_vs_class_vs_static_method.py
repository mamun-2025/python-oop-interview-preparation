
# 1. Instance Method
# 👉 Object এর সাথে related method
# 👉 self ব্যবহার করে

class Person:
   def __init__(self, name):
      self.name = name 
   
   def greet(self): # Instance method
      print("Hello", self.name) 

p = Person("Mamun")
p.greet()
# 👉 Instance data (object variable) access করে


# 2. Class Method
# 👉 Class level method
# 👉 cls ব্যবহার করে
# 👉 @classmethod decorator লাগে

class Person:
   count = 0

   def __init__(self):
      Person.count += 1

   @classmethod
   def total_perosn(cls):
      return cls.count
   
p1 = Person()
p2 = Person()
print(Person.total_perosn())

# 👉 Class variable access/modify করতে use হয়


# 3. Static Method
# 👉 Class এর সাথে logically related কিন্তু
# 👉 class বা object কোনোটাই use করে না
# 👉 @staticmethod ব্যবহার হয়

class Math:
   @staticmethod
   def add(a, b):
      return a + b 
   
print(Math.add(5, 5))
# 👉 Utility function হিসেবে use হয়

# 🔴 Quick Comparison Table
# Feature	      Instance Method	Class Method	Static Method
# First Parameter	self	            cls	         none
# Access	         object data	      class data	   none
# Decorator	      ❌	             @classmethod	 @staticmethod
# Use Case	     object কাজ	    class কাজ	    utility

# Real-Life Example:
class Bank:
   bank_name = "Islamia Bank"

   def __init__(self, balance):
      self.balance = balance

   def deposit(self, amount): # instance
      self.balance += amount

   def withdraw(self, amount):
      if amount <= self.balance:
         self.balance -= amount
         print(f"{amount} tk withdraw successful! Current balance: {self.balance}")
      else: 
         print("Sorry, Your account has not enough balance!")

   @classmethod
   def get_bank_name(cls): # class
      return cls.bank_name
   
   @staticmethod # static
   def add(a, b):
      return a + b 
   
   def __str__(self):
      return f"Account at {self.bank_name} - Balance: {self.balance}"

# Create an account
my_acc = Bank(5000)
# Use the instance method
my_acc.deposit(500)
# Use the class method
print(Bank.get_bank_name())
# Use the static method
print(Bank.add(100, 50))

my_acc.withdraw(1000)
my_acc.withdraw(1000)


# Django Real Exmaple:
# from django.db import models
# class Product(models.Model):
#    name = models.CharField(max_length=100)
#    price = models.IntegerField()

#    def __str__(self): # instance method
#       return self.name 
   
#    @classmethod
#    def get_count(cls):
#       return cls.objects.count()
   
#    @staticmethod
#    def discount(price):
#       return price * 0.9
   
   
# instance method = object related
# class method = queryset/model level
# static method = utility logic

# Instance methods operate on object data using self.Class methods operate on class-level data using cls and are defined with @classmethod.
# Static methods are utility functions that don't access class or instance data and are defined with @staticmethod.
# Object দরকার → instance method
# Class দরকার → class method
# Logic only → static method
