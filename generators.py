
# 🟢 Generator কি?
# 👉 Generator = special function যা yield ব্যবহার করে value এক এক করে return করে
# 👉 একবারে সব data না দিয়ে lazy ভাবে (on demand) value দেয়

# A generator is a function that yields values one at a time using yield, making it memory efficient.

# 1. Basic Example
def my_generator():
   yield 1
   yield 2
   yield 3

g = my_generator()

for i in g:
   print(i)

# 💡 How it Works (VERY IMPORTANT)
# 👉 return → function end করে
# 👉 yield → pause করে, next time আবার resume করে  

# 2. Internal Working
def test():
   print("Start")
   yield 1
   print("Middle")
   yield 2
   print("End")

g = test()

print(next(g))
print(next(g))
# 👉 দেখো function pause-resume করছে

# 3. Generator vs List
# list (memory heavy)
nums = [x for x in range(100000)]

# Generator (memory efficient)
nums = (x for x in range(100000))
# 👉 Generator → memory save করে

# 4. Generator Expression:
gen = (x*2 for x in range(5))

for i in gen:
   print(i)

# 5. Real-Life Example
def read_file(file):
   for line in file:
      yield line
# 👉 একবারে পুরো file memory তে নেয় না

# 6. Infinite Generator
def infinite():
   i = 0
   while True:
      yield i
      i += 1

# 🧠 Generator vs Function
# Feature	   Function    	Generator
# Keyword	   return	      yield
# Execution	   একবারে শেষ	   pause-resume
# Memory	      বেশি	         কম

# 🧠 Deep Concept
# 👉 Generator internally iterator
# 👉 state remember করে

# 🧠 Deep Concept
# 👉 Generator internally iterator
# 👉 state remember করে

# 7. Send() method
def gen():
   x = yield
   yield x * 2

g = gen()
next(g)
print(g.send(5))

# 🔥 Quick Revision
# 👉 yield → pause
# 👉 memory efficient
# 👉 lazy evaluation