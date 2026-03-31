
# 🟢 Iterable কি?
# 👉 Iterable = যেটাকে loop করা যায় (for loop)
# Example
# list
# tuple
# string
# set
# dictionary

nums = [1, 2, 3]
for n in nums:
   print(n)

# Actually internally
it = iter(nums)
while True:
   try:
      n = next(it)
      print(n)
   except StopIteration:
      break


# 🔵 Iterator কি?
# 👉 Iterator = object যা next() দিয়ে এক এক করে value দেয়
nums = [1, 2, 3]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

# 🔥 Core Difference (VERY IMPORTANT)
# Feature	      Iterable	          Iterator
# Definition	   loopable object	 next() দিয়ে value দেয়
# Function     	iter()	         next()
# Example	      list, tuple	      generator, iter()
# Memory	         full data	      one by one

# 1. Custom Iterator
class MyIterator:
   def __init__(self, max):
      self.max = max
      self.current = 0

   def __iter__(self):
      return self 
   
   def __next__(self):
      if self.current < self.max:
         self.current += 1
         return self.current
      else:
         raise StopIteration
      
obj = MyIterator(5)

for i in obj:
   print(i)

# 🔥 Iterable vs Iterator Relationship
# Iterable → iter() দিলে iterator পাওয়া যায়
# Iterator → next() দিয়ে value পাওয়া যায়

# 2. 🟣 Generator = Iterator (IMPORTANT)
def gen():
   yield 1
   yield 2

g = gen()
print(next(g))
print(next(g))
# 🟣 Generator = Iterator (IMPORTANT)

# ⚠️ Tricky Interview Questions
# ❓ Q1: List কি iterator?
# 👉 ❌ No
# 👉 ✅ List = iterable

# ❓ Q2: iter() কি return করে?
# 👉 ✅ Iterator

# ❓ Q3: next() কোথায় কাজ করে?
# 👉 ✅ Iterator only

# ❓ Q4: Generator কি?
# 👉 ✅ Iterator

# Trick Code:
nums = [1, 2, 3]

it1 = iter(nums)
it2 = iter(nums)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it2))
print(next(it2))
# 👉 আলাদা iterator → আলাদা state

# 🎯 Interview Smart Answer
# Iterable is an object that can be looped over, while an iterator is an object that produces values one at a time using next(). Iterators are crated from iterables using iter().

# 🚀 Final Level Understanding
# for loop = iterator internally
# generator = memory efficient iterator
# iterator = stateful