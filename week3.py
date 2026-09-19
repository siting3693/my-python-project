#IF...ELSE
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

'''
Zero (0), empty strings (""), None, and empty collections = False.
Everything else is treated as True. (includes positive, negative numbers, and any non-empty string (even "False" is treated as True because it's a non-empty string))
'''

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#Shorthand
if a > b: print("a is greater than b")

print("A") if a > b else print("B")  #conditional expression

print("A") if a > b else print("=") if a == b else print("B")

bigger = a if a > b else b

#Logical Operators (and, or, not)

if b > a:
  pass       #put pass to avoid error cause by empty if statement

#pass also used in loops, functions, classes


#MATCH (like switch case in java) it selects one to execute only
month = 5
day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6 | 7 if month==4:    #use if to add extra condition
    print("Weekends in April")
  case 6 | 7 if month==5:    #use | (or) if more than one value match in one case
    print("Weekends in May")
  case _:                    #default
    print("No match")


#WHILE
i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break           #break: can stop the loop even if the while condition is true
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue        #continue: stop current iteration and continue with the next
  print(i)
else:               #run once the condition is no longer true (but wont be executed if it's stopped by break)
  print("i is no longer less than 6")


#FOR   used for iterating over a sequence(list, tuple, dictionary, set, or string only) or range [no need indexing variable]
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

for x in "banana":
  if x == "n":
    continue
  print(x)


for x in range(2, 30, 3):         #range(start, stop(not included), increment)   default:start=0, increment=1
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")     #wont be executed if break

#Nested Loops
adj = ["red", "big", "tasty"]
for x in adj:
  for y in fruits:
    print(x, y)



#FUNCTION
def fahrenheit_to_celsius(fahrenheit):       #fahrenheit is parameter (can send any data type including list, dictionary, etc.)
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))             #77 is an argument


def my_function(name = "friend"):       #default value is friend
  print("Hello", name)

my_function()


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")        #using key=value (called keyword arguments), order doesn't matter (if just value is positional argument)


def my_function():
  return ["apple", "banana", "cherry"]

print(my_function()[0])


def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)


def my_function(name, /):            #,/ positional-only argument only
  print("Hello", name)

my_function("Emil")


def my_function(*, name):            #*, keyword-only arguments
  print("Hello", name)

my_function(name = "Emil")


def my_function(a, b, /, *, c, d):  #Arguments before / are positional-only, and arguments after * are keyword-only
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)


#*args (arbitrary arguments-> tuple) and **kwargs (arbitrary keyword arguments-> dictionary)
#*args (can receive any number of arguments)
def my_function(*kids):
  print("The youngest child is " + kids[2])     #tuple

my_function("Emil", "Tobias", "Linus")


def my_function(greeting, *names):       #Regular parameters must come before *args
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


def sum(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(sum(1, 2, 3))

#no need * also can
def sum(numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(sum((1, 2, 3)))    #send tuple (1 argument only)


#**kwargs (can have any number of keys)
def my_function(**kid):           #dictionary
  print("His last name is " + kid["lname"])     #dict[key]

my_function(fname = "Tobias", lname = "Refsnes")      #key=value


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():    #Regular parameters must come before **kwargs
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

'''
The order must be:
1.regular parameters
2.*args
3.**kwargs
'''

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)      #* before argument unpack the list, Same as: my_function(1, 2, 3)
print(result)


def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)              #** before argument unpack dictionary, Same as: my_function(fname="Emil", lname="Refsnes")


#local scope and global scope
x=50          #global scope
y=50
def myfunc():
  x = 300      #local scope
  global y     #to change global variable
  y=100
  print(x)

myfunc()
print(x, y)


def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x        #outside the funtion but not global
    x = "hello"
  myfunc2()
  return x

print(myfunc1())







#Decorator
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


#add wrapper level
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)           #because here the decorator need argument also
def myfunction():
  return "Hello Linus"

print(myfunction())


#two decorators
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())




#.__name__ and .__doc__
def calculate_square(number):
    '''Takes a number and returns its square value.'''
    #Hi
    return number ** 2

# Accessing the documentation string
print(calculate_square.__doc__)        #.__doc__ (docstring only, no comment #)

print(calculate_square.__name__)       #.__name__ function name




import functools               #import functools to use @functools.wraps()

def changecase(func):
  @functools.wraps(func)       #to preserce the function name and docstring (if not, output would be myinner)
  def myinner():
    '''docstring in myinner'''
    return func().upper()
  return myinner

@changecase
def myfunction():
  '''docstring in myfunction'''
  return "Have a great day!"

print(myfunction.__name__)
print(myfunction.__doc__)





#Recusion      (Recursion is when a function calls itself.)
def countdown(n):
  if n <= 0:
    print("Done!")    #***A base case*** - A condition that stops the recursion
  else:
    print(n)
    countdown(n - 1)  #A recursive case - The function calling itself with a ***modified argument***

countdown(5)


def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))


def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))


def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))


def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))


import sys
print(sys.getrecursionlimit())   #default recursion depth limit 




#Generator      (functions that can pause and resume their execution)
#only executes when you iterate over the generator
def my_generator():
  yield 1              #use yield instead of return, form iterator together
  yield 2
  yield 3

for value in my_generator():   #iterates over the generator
  print(value)
#same as
gen = my_generator()     #gen is iterator, my_generator is generator
print(next(gen))
print(next(gen))
print(next(gen))
#or print it as list
print(list(my_generator()))


#
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)


#
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))


#
# List comprehension - creates a list
list_comp = [x * x for x in range(5)]    #square bracket
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))      #bracker ()    #gen_exp is iterator, not generator
print(gen_exp)
print(list(gen_exp))


#
# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)


#
def fibonacci():         #only generate result needed when it is called
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 10 Fibonacci numbers
gen = fibonacci()
for _ in range(10):
  print(next(gen))


#
def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen)         #It starts the execution of the generator function from the beginning until it hits the first yield statement. yield pauses the function and waits to receive a value.
gen.send("Hello")
gen.send("World")


#
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:            #run code in finally: after exhausting the generator(next(gen) but no item dy), closing it, Python's Garbage Collector deletes it(overwrite the gen variable), error occur in try:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()




#RANGE data type: range    range(start(inclusive), stop(exclusive), step(integer only))
x = range(3, 10)
print(x)
print(list(x))
print(x[:3])      #slicing
print(6 in x)
print(len(x))
for i in range(10):
  print(i)




#ITERATOR
#iterable objects: Lists, tuples, dictionaries, sets, and strings
#we get iterator from iterable objects using iter() method (every iterable object has this method)
mytuple = ("apple", "banana", "cherry")    #iterable object

myit = iter(mytuple)                       #iterator
print(next(myit))
print(next(myit))
print(next(myit))
#same as
for x in mytuple:
  print(x)



#MODULE
import mymodule     #import everything (functions, all types of variables) in mymodule.py file
mymodule.greeting("Jonathan")   #use function in that file called greeting()

import mymodule as mx      #use mx instead of mymodule
mydict = mx.person1["age"] #use dictionary person1 in mymodule file

print(dir(mymodule))     #List all the defined names belonging to the module


from mymodule import person1    #can choose to import person1 only from mymodule
print (person1["age"])          #no need to write module name (mymodule.person1), just call it like normal enough



#DATE
import datetime
x = datetime.datetime.now()
print(x)

y = datetime.datetime(2007,9,30)     #year, month, day, hour(optional), minute(o), second(o), microsecond(o), tzone(o)
print(y)
print(y.strftime("%c"))
print(y.strftime("%Y"))
print(y.strftime("%B"))
print(y.strftime("%A"))            #more refer to python dates in w3schools



#MATH
x = min(my_list)        #min(iterable object)
y = max(5, 10, 25)
print(x)
print(y)

x = abs(-802.8)         #absolute
print(x)

x = pow(2,3)            #x to the power of y
print(x)

import math
x = math.sqrt(64)
print(x)

x = math.ceil(1.4)         #rounds a number upwards
y = math.floor(1.4)        #rounds a number downwards
print(x)
print(y)

x = math.pi
print(x)


#JSON (JavaScript Object Notation) a common 'language' for different languages to talk to each other
import json

j =  '{ "name":"John", "age":30, "city":"New York"}'
p = json.loads(j)       #json.loads() change json to python
print(p["age"])

p = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
j = json.dumps(p)      #json.dumps() change python to json
print(j)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, separators=("."," = "), sort_keys=True))    #indent and separators(between objects and between key and value) and sort_keys (alphabetically) are optional parameters



#RegEx (Regular Expression)  search
import re
txt = "The rain in Spain"

#findall(): findall() returns a list containing all matches
x = re.findall("[a-j]", txt)         #Find all lower case characters alphabetically between "a" and "j" (that are a, b, c, d, e, f, g, h, i) from txt
print(x)

#search(): search() return one MATCH OBJECT only if there is a match
x = re.search("^The.*Spain$", txt)   #starts with "The" and ends with "Spain"
x = re.search(r"\bS\w+", txt)        #an upper case "S" character in the beginning of a word
print(x)
print(x.span)                        #print its position
print(x.string)                      #where x come from (txt)
print(x.group())                     #print what satisfy the condition
if x:
  print("YES! We have a match!")
else:
  print("No match")


#split(): split() returns a list where the string has been split at each match
x = re.split("\s", txt)        #\s is white-space
print(x)

x = re.split("\s", txt, 1)     #maxsplit parameter control the number of occurences of spliting
print(x)

#sub(): sub() replaces the matches with the text of your choice
x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)  #count parameter control the number of replacements
print(x)



#PIP
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))



#TRY...EXCEPT ELSE FINALLY
#try: test a block of code for errors
#except: handle the error
#else: execute when there is no error
#finally: execute code regardless of the result of the try and except blocks
try:
  print(z)
except:
  print("An exception occurred")

try:
  print(x)
except NameError:                   #execute a special block of code for a special kind of error
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#more error types on python try...except website

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

'''
x = -1
if x < 0:
  raise Exception("Sorry, invalid")   #raise an error

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")     #can define the type of error
'''



#STRING FORMATTING
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"      #can perform if else statements inside placeholders
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"   #can execute function also
print(txt)
#.2f 2 decimal places, other formatting types in python string formatting website

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))




#NONE
x = None
print(x)
print(type(x))
print(bool(None))

if result is None:
  print("No result yet")
else:
  print("Result is ready")

if result is not None:
  print("Result is ready")
else:
  print("No result yet")

def myfunc():
  x = 5

x = myfunc()  #no return function return None by default
print(x)




#INPUT
print("Enter your name:")
name = input()
print(f"Hello {name}")
#or
name = input("Enter your name:")
print(f"Hello {name}")

x = input("Enter a number:")
y = math.sqrt(float(x))          #convert input into float**
print(f"The square root of {x} is {y}")


#validate input, avoid error
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x);             #error will occur here if not a number
    y = False
  except:
    print("Wrong input, please try again.")





'''VIRTUAL ENVIRONMENT (use command prompt)
Imagine you are building with LEGOs.

The Problem: The "Mixed-Up Bin"
Imagine you have one big bin of LEGOs in your room.
- You decide to build a Space Station. You need special blue and silver pieces.
- Then, your friend comes over and says, "Let's build a Castle!" But the Castle needs red and grey pieces, and they keep getting mixed in with your Space Station pieces.
- To make it worse, maybe your Space Station needs a "Super-Fast Engine" piece, but the Castle set needs a "Standard Engine" piece. You can't have both in the same set, or the pieces start to break or don't fit right.
Your "Global Python" (the normal one on your computer) is like that one big, messy bin. If you install a tool for one project, it might mess up another.

The Solution: The "Separate Trays"
A Virtual Environment is like getting a separate, small tray for every single project.
1. The Tray (The Folder): When you run that venv command, you are essentially buying a new, clean plastic tray and giving it a name (like myfirstproject).
2. The Tools (The Libraries): When you "activate" your tray, you are saying, "I am only working with the pieces in this specific tray." If you install a tool like cowsay, it goes only into that tray.
3. The Safety: Because the cowsay tool is sitting inside the myfirstproject tray, it is hidden away from your other projects. Your "Global" computer bin stays clean and organized.

Why do you have to use the Command Prompt?
Think of the Command Prompt as your Robot Assistant.
- Usually, you use your mouse to click on things (that's the "Visual" way).
- But to tell your Robot Assistant exactly which tray to use, you have to talk to it. You type activate (or the folder path), and the Robot Assistant says, "Understood! From now on, whenever you ask for a tool, I will only look inside the myfirstproject tray."

Why your code didn't work before:
When you ran python test.py normally, you were asking your computer:
"Hey, computer! Run this code using the tools in the giant, messy global bin." But the "cowsay" tool wasn't in the global bin—it was hiding inside your myfirstproject tray! The computer couldn't find it, so it got confused and gave you an error.

In short:
- Virtual Environment: A clean, private sandbox for one project's tools.
- Command Prompt: The way you tell your computer which sandbox you want to play in today.
'''


