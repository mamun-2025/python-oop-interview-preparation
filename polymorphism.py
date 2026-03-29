
# 🟢 Polymorphism কি?
# Polymorphism হল একটি অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং ধারণা যা একটি ইন্টারফেসের মাধ্যমে বিভিন্ন ধরনের অবজেক্টকে পরিচালনা করতে সাহায্য করে। এটি একটি ফাংশন বা মেথডকে বিভিন্ন ধরনের ডেটা বা অবজেক্টের সাথে কাজ করার ক্ষমতা প্রদান করে। Polymorphism এর মাধ্যমে আমরা একই ফাংশন বা মেথডকে বিভিন্ন ধরনের অবজেক্টের জন্য ব্যবহার করতে পারি, যা কোডকে আরও নমনীয় এবং পুনঃব্যবহারযোগ্য করে তোলে।
# 1. Method Overriding: Polymorphism এর একটি সাধারণ উদাহরণ হল মেথড ওভাররাইডিং, যেখানে একটি চাইল্ড ক্লাস প্যারেন্ট ক্লাসের মেথডকে ওভাররাইড করে তার নিজস্ব ইমপ্লিমেন্টেশন প্রদান করে।
# 2. Duck Typing: Python এ, Polymorphism এর আরেকটি উদাহরণ হল ডাক টাইপিং, যেখানে একটি অবজেক্টের টাইপ তার আচরণের উপর ভিত্তি করে নির্ধারিত হয়, এবং এটি একটি নির্দিষ্ট ইন্টারফেস অনুসরণ করে।
# 3. Operator Overloading: Polymorphism এর আরেকটি উদাহরণ হল অপারেটর ওভারলোডিং, যেখানে আমরা একটি ক্লাসের জন্য অপারেটরগুলিকে ওভারলোড করতে পারি, যেমন +, -, *, ইত্যাদি, যা আমাদের ক্লাসের অবজেক্টগুলির সাথে কাজ করার জন্য ব্যবহার করা যেতে পারে।
# 4. Real-Life Example: Polymorphism এর একটি বাস্তব জীবনের উদাহরণ হল একটি পেইন্টিং অ্যাপ্লিকেশন, যেখানে বিভিন্ন ধরনের শেপ (যেমন সার্কেল, স্কোয়ার, ট্রায়াঙ্গল) আঁকার জন্য একই ফাংশন ব্যবহার করা হয়, কিন্তু প্রতিটি শেপের জন্য আলাদা ইমপ্লিমেন্টেশন থাকে।

# 👉 Polymorphism = same method/function different behavior
# 1. Same Function, Different Data Type:

print(len("Hello")) # String
print(len([1, 2, 3, 4, 5])) # List
print(len({'a': 1, 'b': 2, 'c': 3})) # Dictionary

# 2. Method Overriding:
class Animal:
   def speak(self):
      return "Animal speaks"

class Dog(Animal):
   def speak(self):
      return "Woof!"
   
class Cat(Animal):
   def speak(self):
      return "Meow!"
   
class Cow(Animal):
   def speak(self):
      return "Moo!"
   
animals = [Dog(), Cat(), Cow()]
# print(animals[0].speak())
# print(animals[1].speak())
# print(animals[2].speak())
for animal in animals:
   print(animal.speak())

# 3. Operator Overloading:
class Point:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __add__(self, other):
      return Point(self.x + other.x, self.y + other.y)
   
p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(f"Point 1: ({p1.x}, {p1.y})")
print(f"Point 2: ({p2.x}, {p2.y})")
print(f"Point 3: ({p3.x}, {p3.y})")

# 4. Duck Typing:
class Bird:
   def fly(self):
      return "Bird can fly"

class Airplane:
   def fly(self):
      return "Airplane can fly"
   
class Fish:
   def swim(self):
      return "Fish can swim"
   
def start_flying(object):
   object.fly()

start_flying(Bird())
start_flying(Airplane())
# start_flying(Fish()) # Error: 'Fish' object has no attribute 'fly'
# Python check করে না class, শুধু method থাকলেই কাজ করবে

# Real-Life Example:
class Payment:
   def pay(self):
      pass 

class Card(Payment):
   def pay(self):
      print("Payment made using Card")

class Cash(Payment):
   def pay(self):
      print("Payment made using Cash")

def process(Payment):
   Payment.pay()

process(Card())
process(Cash())

# Types of Polymorphism:
# 1. Compile-Time Polymorphism: এটি একটি ধরনের Polymorphism যা কম্পাইল টাইমে নির্ধারিত হয়, যেমন ফাংশন ওভারলোডিং এবং অপারেটর ওভারলোডিং।
# 2. Run-Time Polymorphism: এটি একটি ধরনের Polymorphism যা রান টাইমে নির্ধারিত হয়, যেমন মেথড ওভাররাইডিং এবং ডাক টাইপিং।

# Quick Revision:
# 1. Polymorphism হল একটি অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং ধারণা যা একটি ইন্টারফেসের মাধ্যমে বিভিন্ন ধরনের অবজেক্টকে পরিচালনা করতে সাহায্য করে।
# 2. Polymorphism এর মাধ্যমে আমরা একই ফাংশন বা মেথডকে বিভিন্ন ধরনের অবজেক্টের জন্য ব্যবহার করতে পারি, যা কোডকে আরও নমনীয় এবং পুনঃব্যবহারযোগ্য করে তোলে।
# 3. Polymorphism এর উদাহরণগুলির মধ্যে রয়েছে মেথড ওভাররাইডিং, ডাক টাইপিং, এবং অপারেটর ওভারলোডিং।
# 4. Polymorphism এর ধরনগুলির মধ্যে রয়েছে Compile-Time Polymorphism এবং Run-Time Polymorphism।
# same method/function different behavior → Polymorphism
# Overloading → Compile-Time Polymorphism
# Overriding → Run-Time Polymorphism
# Duck Typing → Run-Time Polymorphism
