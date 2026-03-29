
# 🟢 Inheritance কি?
# Inheritance হল একটি Object-Oriented Programming (OOP) এর মূল ধারণা যা একটি ক্লাস (যাকে Parent Class বা Base Class বলা হয়) থেকে আরেকটি ক্লাস (যাকে Child Class বা Derived Class বলা হয়) তৈরি করার প্রক্রিয়া। এই প্রক্রিয়ায়, Child Class Parent Class এর বৈশিষ্ট্য এবং আচরণ (properties and methods) উত্তরাধিকারসূত্রে পায়, যার ফলে কোড পুনঃব্যবহার সহজ হয় এবং একটি শ্রেণির বৈশিষ্ট্যগুলি অন্য শ্রেণিতে সহজেই ব্যবহার করা যায়।
# Inheritance এর মাধ্যমে, আমরা একটি নতুন ক্লাস তৈরি করতে পারি যা পূর্ববর্তী ক্লাসের বৈশিষ্ট্য এবং আচরণকে সম্প্রসারিত করে বা পরিবর্তন করে। এটি কোডের পুনঃব্যবহার এবং মেইনটেনেন্স সহজ করে তোলে, কারণ আমরা একই কোড বারবার লিখতে হয় না।
# Inheritance এর ধরন:
# 1. Single Inheritance: একটি Child Class একটি Parent Class থেকে উত্তরাধিকারসূত্রে বৈশিষ্ট্য এবং আচরণ পায়।
# 2. Multiple Inheritance: একটি Child Class একাধিক Parent Class থেকে বৈশিষ্ট্য এবং আচরণ পায়।
# 3. Multilevel Inheritance: একটি Child Class একটি Parent Class থেকে উত্তরাধিকারসূত্রে বৈশিষ্ট্য এবং আচরণ পায়, এবং সেই Parent Class আবার অন্য একটি Parent Class থেকে উত্তরাধিকারসূত্রে বৈশিষ্ট্য এবং আচরণ পায়।
# 4. Hierarchical Inheritance: একটি Parent Class থেকে একাধিক Child Class তৈরি হয়।
# 5. Hybrid Inheritance: এটি একটি কম্বিনেশন যা একাধিক Inheritance এর ধরনকে একত্রিত করে।
# Inheritance এর সুবিধা:
# 1. কোড পুনঃব্যবহার: Inheritance এর মাধ্যমে আমরা Parent Class এর বৈশিষ্ট্য এবং আচরণ Child Class এ ব্যবহার করতে পারি, যা কোড পুনঃব্যবহারকে সহজ করে তোলে।
# 2. সহজ মেইনটেনেন্স: Inheritance এর মাধ্যমে আমরা একটি Parent Class এ পরিবর্তন করলে, সেই পরিবর্তনগুলি সমস্ত Child Class এ প্রভাবিত হয়, যা মেইনটেনেন্সকে সহজ করে তোলে।
# 3. Polymorphism: Inheritance এর মাধ্যমে আমরা Polymorphism অর্জন করতে পারি
# , যা একটি ইন্টারফেসের মাধ্যমে বিভিন্ন ধরনের অবজেক্টকে পরিচালনা করতে সাহায্য করে।
# 4. Code Organization: Inheritance এর মাধ্যমে আমরা কোডকে আরও সংগঠিত এবং পরিষ্কারভাবে সাজাতে পারি, কারণ আমরা সম্পর্কিত বৈশিষ্ট্য এবং আচরণগুলি একত্রে রাখতে পারি।

# 1. Basic Example:
# Parent class
class Animal:
   def speak(self):
      print("Animal speaks")

# Child class inheriting from Animal
class Dog(Animal):
   def bark(self):
      print("Dog barks")

d = Dog()
d.speak() # Output: Animal speaks
d.bark()  # Output: Dog barks

# 2. Constructor Inheritance:
class Person:
   def __init__(self, name):
      self.name = name

class Student(Person):
   def __init__(self, name, student_id):
      super().__init__(name)
      self.student_id = student_id

s = Student("Mamun", "12345")
print(s.name)      # Output: Mamun
print(s.student_id) # Output: 12345
# 👉 super() → parent class method call করার জন্য

# 3. Single Inheritance:
class Vehicle:
   def start(self):
      print("Vehicle starts")

class Car(Vehicle):
   def drive(self):
      print("Car drives")
   
c = Car()
c.start() # Output: Vehicle starts
c.drive() # Output: Car drives

# 4. Multiple Inheritance:
class A:
   def method_a(self):
      print("Method A")

class B:
   def method_b(self):
      print("Method B")

class C(A, B):
   def method_c(self):
      print("Method C")

c = C()
c.method_a() # Output: Method A
c.method_b() # Output: Method B
c.method_c() # Output: Method C

# 5. Multilevel Inheritance:
class Grandparent:
   def method_grandparent(self):
      print("Method Grandparent")

class Parent(Grandparent):
   def method_parent(self):
      print("Method Parent")

class Child(Parent):
   def method_child(self):
      print("Method Child")

c = Child()
c.method_grandparent() # Output: Method Grandparent
c.method_parent() # Output: Method Parent
c.method_child() # Output: Method Child

# 6. Hierarchical Inheritance:
class Parent:
   def method_parent(self):
      print("Method Parent")
   
class Child1(Parent):
   def method_child1(self):
      print("Method Child1")

class Child2(Parent):
   def method_child2(self):
      print("Method Child2")

p = Parent()
c1 = Child1()
c2 = Child2()
p.method_parent() # Output: Method Parent
c1.method_parent() # Output: Method Parent
c1.method_child1() # Output: Method Child1
c2.method_parent() # Output: Method Parent
c2.method_child2() # Output: Method Child2

# 7. Hybrid Inheritance:
class A:
   def method_a(self):
      print("Method A")

class B(A):
   def method_b(self):
      print("Method B")

class C(A):
   def method_c(self):
      print("Method C")

class D(B, C):
   def method_d(self):
      print("Method D")

d = D()
d.method_a() # Output: Method A
d.method_b() # Output: Method B
d.method_c() # Output: Method C
d.method_d() # Output: Method D

# 8. Method Overriding:
class Animal:
   def speak(self):
      print("Animal speaks")

class Dog(Animal):
   def speak(self):
      print("Dog barks")

d = Dog()
d.speak() # Output: Dog barks

# 9. Using super() to call parent class method:
class Parent:
   def greet(self):
      print("Hello from Parent")

class Child(Parent):
   def greet(self):
      super().greet() # Call the parent class method
      print("Hello from Child")

c = Child()
c.greet() # Output:
# Hello from Parent
# Hello from Child

# 10. Django Real World Example:
class User:
   def login(self):
      print("User logged in")

class Admin(User):
   def delete_user(self):
      print("User deleted")

admin = Admin()
admin.login() # Output: User logged in
admin.delete_user() # Output: User deleted

# 10. Python's Built-in Inheritance:
class MyList(list):
   def sum(self):
      return sum(self)

my_list = MyList([1, 2, 3])
print(my_list.sum()) # Output: 6

# Quick Revison:
# Inheritance হল একটি OOP ধারণা যা একটি ক্লাস থেকে আরেকটি ক্লাস তৈরি করার প্রক্রিয়া।
# Child Class Parent Class এর বৈশিষ্ট্য এবং আচরণ উত্তরাধিকারসূত্রে পায়।
# Inheritance এর ধরন: Single, Multiple, Multilevel, Hierarchical, Hybrid।
# Inheritance এর সুবিধা: কোড পুনঃব্যবহার, সহজ মেইনটেনেন্স, Polymorphism, Code Organization।


