
# Class এবং Object এর মধ্যে পার্থক্য?
# ✅ 1. Class কি?
# 👉 Class = Blueprint / Template
# মানে এটা একটা structure define করে (data + behavior)

class Person: # Person = Class
      # Data (Attributes)
      name = "Habib Mamun"

      def greet(self):
            # Behavior (Method)
            print(f"Hello, I am {self.name}")

p1 = Person() # p1 = Object (Instance of the class)
p1.greet() # Output: Hello, I am Habib Mamun

# ✅ 2. Object কি?
# 👉 Object = Instance of a Class
# Object হলো class এর একটি instance, যা class এর structure অনুযায়ী তৈরি করা হয়।
p2 = Person() # p2 = Object (Instance of the class)
p2.name = "John Doe" # Object এর attribute পরিবর্তন করা
p2.greet() # Output: Hello, I am John Doe


# ✅ 3. Constructor (__init__ method)
# 👉 object create হওয়ার সময় automatically run হয়
class Person:
      def __init__(self, name, age):
            self.name = name
            self.age = age 
        
p3 = Person("Mamun Bepari", 27) # Object তৈরি করার সময় name এবং age পাস করা
print(p3.name)

# ✅ 4. Multiple Objects
p4 = Person("Alice", 30)
p5 = Person("Bob", 25)
print(p4.name)
print(p5.name)

# ✅ 4. Instance Variable vs Class Variable
class Student:
      school = "ABC School" # Class Variable (সব object এর জন্য common)

      def __init__(self, name):
            self.name = name # Instance Variable (প্রতিটি object এর জন্য আলাদা)

s1 = Student("Mamun")
s2 = Student("Rahim")

print(s1.name)
print(s2.name)

# Class variable access
print(Student.school) # Output: ABC School
print(s1.school) # Output: ABC School
print(s2.school) # Output: ABC School

# Instance Variable Access
class Person:
      def __init__(self, name):
            self.name = name

      def greet(self):
         print("Hello!", self.name)

p6 = Person("chatGPT")
p6.greet()

# ✅ 5. Real Backend Practical Example
class User:
      def __init__(self, username, password):
            self.username = username
            self.password = password

      def check_password(self, input_pass):
            return self.password == input_pass
      
user1 = User("admin", "1234")
print(user1.check_password("1234"))
print(user1.check_password("Wrong_password"))

# ✅ 6. Summary 
# - Class = Blueprint / Template
# - Object = Instance of a Class
# - Constructor (__init__ method) = Object create হওয়ার সময় automatically run হয়
# - Instance Variable = প্রতিটি object এর জন্য আলাদা attribute
# - Class Variable = সব object এর জন্য common attribute

# ✅ 7. Interview Answer
# Class is a blueprint or template for creating objects, and object is an instance of a class. Class defines attributes and methods, while object represents real-world entities using that structure.

      