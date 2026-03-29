
# 🟢 Encapsulation কি?
# Encapsulation হল একটি Object-Oriented Programming (OOP) এর মূল ধারণা যা ডেটা এবং ফাংশনকে একত্রে একটি ইউনিটে (অবজেক্ট) সংরক্ষণ করে। এটি ডেটা হাইডিং বা ডেটা লুকানোর মাধ্যমে ডেটাকে নিরাপদ রাখে এবং অবজেক্টের অভ্যন্তরীণ স্টেটকে বাইরের কোড থেকে সরাসরি অ্যাক্সেস থেকে রক্ষা করে।
# Encapsulation এর মাধ্যমে, আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে প্রাইভেট (private) বা প্রোটেক্টেড (protected) করতে পারি, যা বাইরের কোড থেকে সরাসরি অ্যাক্সেস করা যায় না। এর ফলে, আমরা ডেটার নিরাপত্তা নিশ্চিত করতে পারি এবং অবজেক্টের স্টেটকে অবাঞ্ছিত পরিবর্তন থেকে রক্ষা করতে পারি।
# Encapsulation এর সুবিধা:
# 1. ডেটা নিরাপত্তা: Encapsulation এর মাধ্যমে আমরা ডেটাকে প্রাইভেট বা প্রোটেক্টেড করতে পারি, যা বাইরের কোড থেকে সরাসরি অ্যাক্সেস করা যায় না, ফলে ডেটার নিরাপত্তা নিশ্চিত হয়।
# 2. সহজ মেইনটেনেন্স: Encapsulation এর মাধ্যমে আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা কোডের মেইনটেনেন্সকে সহজ করে তোলে।
# 3. কোড রিইউজ: Encapsulation এর মাধ্যমে আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা কোড রিইউজকে সহজ করে তোলে।
# 4. Abstraction: Encapsulation এর মাধ্যমে আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা Abstraction অর্জন করতে সাহায্য করে, অর্থাৎ আমরা একটি ইন্টারফেসের মাধ্যমে অবজেক্টের স্টেট এবং আচরণকে পরিচালনা করতে পারি।

# 1. Basic Example:
class Person:
   def __init__(self, name, age):
      self.name = name # Public attribute
      self._age = age # Protected attribute
      self.__salary = 50000 # Private attribute

p = Person("Mamun", 26)

print(p.name) # Output: Mamun
print(p._age) # Possible but not recommended to access protected attribute
# print(p.__salary) # This will raise an AttributeError because __salary is private

# 2. Private Variable Access:
class BankAccount:
   def __init__(self, balance):
      self.__balance = balance # Private attribute

   def get_balance(self):
      return self.__balance
   
account = BankAccount(1000)
# print(account.__balance) # This will raise an AttributeError because __balance is private
print(account.get_balance()) # Output: 1000

# 3. Getter and Setter Methods:
class Person:
   def __init__(self):
      self.__age = 18

   def get_age(self):
      return self.__age
   
   def set_age(self, age):
      if age >= 0:
         self.__age = age
      else:
         print("Age cannot be negative")

p = Person()

print(p.get_age()) # Output: 18
p.set_age(25)
print(p.get_age()) # Output: 25
p.set_age(-5) # Output: Age cannot be negative

# 4. Pythonic Way(Property Decorator)
class Person:
   def __init__(self):
      self.__age = 18

   @property
   def age(self):
      return self.__age
   
   @age.setter
   def age(self, value):
      if value > 0:
         self.__age = value

p = Person()

print(p.age)
p.age = 30
print(p.age)

# Real-Life Example
class Bank:
   def __init__(self):
      self.__balance = 0

   def deposit(self, amount):
      self.__balance += amount

   def get_balance(self):
      return self.__balance
   
b = Bank()
b.deposit(10000)
print(b.get_balance())

# Quick Revision
# 1. Encapsulation হল একটি Object-Oriented Programming (OOP) এর মূল ধারণা যা ডেটা এবং ফাংশনকে একত্রে একটি ইউনিটে (অবজেক্ট) সংরক্ষণ করে।
# 2. Encapsulation এর মাধ্যমে, আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা কোডের মেইনটেনেন্সকে সহজ করে তোলে।
# __variable → private variable
# _variable → protected variable
# variable → public variable
# 3. Encapsulation এর মাধ্যমে, আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা Abstraction অর্জন করতে সাহায্য করে, অর্থাৎ আমরা একটি ইন্টারফেসের মাধ্যমে অবজেক্টের স্টেট এবং আচরণকে পরিচালনা করতে পারি।
# 4. Encapsulation এর মাধ্যমে, আমরা একটি ক্লাসের ডেটা এবং ফাংশনকে একত্রে রাখতে পারি, যা কোড রিইউজকে সহজ করে তোলে।
# 5. Encapsulation এর মাধ্যমে, আমরা ডেটাকে প্রাইভেট বা প্রোটেক্টেড করতে পারি, যা বাইরের কোড থেকে সরাসরি অ্যাক্সেস করা যায় না, ফলে ডেটার নিরাপত্তা নিশ্চিত হয়।
# getter and setter method → get_variable() and set_variable()
# property decorator → @property and @variable.setter


