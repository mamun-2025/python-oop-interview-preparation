
# 🟢 Python Decorator কি?
# 👉 Decorator = এমন function যা অন্য function কে modify/extend করে without changing its original code
# A decorator is a function that wraps another function to extend its behavior without modifying its original it's original implementation.

# 1. Basic example
def decorator_func(original_func):
   def wrapper():
      print("Before")
      original_func()
      print("After")
   return wrapper

@decorator_func
def hey():
   print("Hi")

hey()


# 2. Simple Decorator
def my_decorator(func):
   def wrapper():
      print("Before function")
      func()
      print("After function")
   return wrapper

@my_decorator
def say_hello():
   print("Hello")

say_hello()

# 3. With Arguments
def my_decorator(func):
   def wrapper(name):
      print("Before")
      func(name)
      print("After")
   return wrapper

@my_decorator
def greet(name):
   print("Hello", name)

greet("Mamun")

# 4. Using *args **args
def my_decorator(func):
   def wrapper(*args, **kwargs):
      print("Before")
      result = func(*args, **kwargs)
      print("After")
      return result
   return wrapper

# 5. Return Value Handle
def my_decorator(func):
   def wrapper(*args, **kwargs):
      result = func(*args, **kwargs)
      return result * 2
   return wrapper

@my_decorator
def add(a, b):
   return a + b 

print(add(2, 3))

# 6. Login Required(Django Style)
def login_required(func):
   def wrapper(user):
      if not user.get("is_logged_in"):
         print("Login required!")
         return 
      return func(user)
   return wrapper

@login_required
def dashboard(user):
   print("Welcome to dashboard")

user = {"is_logged_in": True}
dashboard(user)

# Built-in Decorator
class Test:
   @staticmethod
   def add(a, b):
      return a + b
   

# 🧠 Deep Understanding
# 👉 Decorator = wrapper pattern
# 👉 original function change না করে behavior add করা

# 🧠 Deep Understanding
# 👉 Decorator = wrapper pattern
# 👉 original function change না করে behavior add করা

# 🔥 Quick Revision
# 👉 decorator = wrapper
# 👉 @ syntax = shortcut
# 👉 flexible = *args, **kwargs