#comment
'docstring1'
"docstring2"
"""
multiline
docstring
"""


import sys

print(sys.version)
print("hello", end=" ")
print('hiiii')
print("i am",35,"years old.")
multiline="""This is the first line.
This is the second line.
This is the third line.

"""
print(multiline)
print(multiline[6])        # index starts from 0
print(len(multiline))      # length



x=220
print(isinstance(x,int))   # check data type of variable



#SLICING
print(multiline[3:25])     # get characters from index 3 to 25 (25 is not included)
print(multiline[:3],multiline[60:])  # from 0 to 3 and from 60 to the end
print(multiline[-5:-2])              # negative 1 starts from the right (-2 is not included)


for x in "banana":
  print(x)              # like an array

print("This" in multiline)      # check if XXX is present in a string (result is a boolean)
print("This" not in multiline)  # not!
if "This" in multiline:
  print("Yes, 'This' is present.")


x = 4       # x is of type int
x = "    Sally     " # x is now of type str
print(x)
print(type(x))       #print data type

print(x.upper())      #upper case
print(x.lower())      #lower case
print(x.strip())      #removes whitespace from the beginning or the end
print(x.replace("S","Hi"))    #replace S with Hi
print(x.split("a"))           #"a" gone, both ends are split








#CASTING
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
z = 3-6j      # datatype=complex, complex number 6 as the imaginary part

a = float(y)    #convert from int to float
b = complex(z)  #convert from float to complex

x = int(1)   # x will be 1
y = int(2.8) # y will be 2 (remove all decimals)
z = int("3") # z will be 3

x, y, z = "Orange", "Banana", "Cherry"

print(y)

x = y = z = "Orange"

print(y)






#LIST
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(y)

print(x,y,z)
print(x+y+z)   #cannot use + for string and numbers


if 5>2:
    print("5>2")   #MUST have indentation







#FUNCTION
def myFunction():
  print("Python is " + x)   #x is global variable because it is created outside of a function


myFunction()

def urFunction():
    x = "fun"    #x = "fun" in this function only
    print("Python is",x)

urFunction()
print(x)

def globalInLocal():
    global x
    x= "good"     #MUST declare and give value seperately!!!
    print("Python is",x)

globalInLocal()
print(x)

x = 35e3    #e is: times 10 to the power of blablabla  (if got e datatype is float)
print(x)


import random
print(random.randrange(1, 10))    #from 1 to 9, not 10!!
print(random.randint(1, 10))      #from 1 to 10






price=10

#FORMAT STRING
txt = f"The price is {price:.2f} dollars"    #inside {} is Python code, .2f means 2 decimal places
print(txt)
txt = f"salary is rm{11*10.5*6*3:.2f}"
print(txt)

#//print format
price=7.986
print(f"price is rm {price:.2f}")


#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

#can = f"XXX" or "XXX".format()






#ESCAPE CHARACTERS
txt= 'That\'s great.'      #use \ before ' if open with single quote
print(txt)
txt="It's hard to pronounce \"sixth\"."    #use \ before " if open with double quote
print(txt)
txt="want \nto print \t one \bbackslash \\."      #\n is next line, \t is tab, \b is backspace (WHY CANNOT FUNCTIONNN!!!!), \\ to print one backslash
print(txt)
txt="\110\145\154\154\157\x48\x65\x6c\x6c\x6f"        #\ followed by three octal value, \ followed by x followed by two hex value
print(txt)

txt="Tan Si Ting"
print(txt.capitalize())
#OR print("Tan Si Ting".capitalize())
print(txt.casefold())
print(txt.lower())

print(txt.center(50,"-"))

txt="I love to eat apples, an apple a day......"
print(txt.count("apple",17,35))                   # count HOW MANY TIMES "apple" appear from position 17 to 35

print(txt.find("apples",10,35))                   # find the position of "apple" from position 10 to 37 (count from first position, print 0 if at position 1), if not found print -1




#OPERATOR
print(15//2)         # floor divition
print(3**2)          # exponentiation







#ASSIGNMENT OPERATORS
x=1
x+=2
x**=3
print (x)


#& is BITWISE AND
x=7         # x= 0111 (7)
x&=5  # x=x&5  & 0101 (5)
print (x)   # =  0101 (5)
print(7&5)

#Checking if a Number is Odd or Even
x = 7
if x & 1:
    print("Odd")  # 7 in binary is 0111. 0111 & 0001 = 0001 (which is True)

x = 42
if (x & 1) == 0:
    print(f"{x} is Even")       #print format
    
# | is BITWISE OR
x=5          # 0101(5)
x|=3         # 0011(3)
print(x)     # 0111(7)
print(5|3)

#Combining sets (set union)
my_permissions = {"read", "write"}
new_permissions = {"write", "execute"}

my_permissions |= new_permissions    # Combine them using |=

print(my_permissions)

#Merging Dictionaries
user_profile = {"name": "Alice", "role": "User"}
dark_mode_setting = {"theme": "dark", "role": "Admin"}

user_profile |= dark_mode_setting
#'role' was overwritten by the new dictionary's value
print(user_profile)


# ^ is BITWISE XOR
x = 5
x ^= 3
print(x)
print(5^3)

#Simple Encryption
pwd = 467
key = 27
pwd^=key
print(pwd)
pwd^=key
print(pwd)


# >> is BITWISE RIGHT SHIFT
x = 5        # 000101 (5)
x >>= 2      #shift all the bits of x to the right by 2 positions
print(x)     #equivalent to floor division by 2 power n (5//2power2)
print(5>>2)

# << is BITWISE LEFT SHIFT
x = 5        # 000101 (5)
x <<= 2      #shift all the bits of x to the right by 2 positions
print(x)     #times 2 power n
print(5<<2)

# := save that value into a variable while printing it
print(x:=3)  #same as  x=3    print(x)



#BITWISE OPERATOR
"""
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
"""

#TERNARY OPERATOR
num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "Workday"
print(x)

#COMPARISON OPERATOR
print(not(num<10 and num>5))    # use (and,or,not) not (&&,||,!)

#####&|^ is bitwise operator but not, and, or is logical(between true and false)

#IDENTITY OPERATOR   (not if they are equal, BUT same object same memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)



#MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)












#LISTS
thislist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(len(thislist))

list1 = ["abc", 34, True, 40, "male", 40]          #can contain different data types
print(list1.count(40))
print(list1.index("male", 4))                 # return the index of the first item, error if not exist (list.index(element, startIndex, endIndex(not included) ) )
print(type(list1))                            # data type is list, does not depend on its content
print(list1[-4:-1])            # -1 is not included

if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist[1] = "blackcurrant"
thislist[1:3] = ["banana", "watermelon"]
thislist[1:2] = ["blackcurrant", "watermelon"]             #can replace old item(s) with more or less item(s)
print(thislist)
thislist.insert(2, "watermelon")                    #watermelon is inserted as the item with index 2
print(thislist)
thislist.append("orange")                 # add item to the end of the list

tropical = ["mango", "pineapple", "papaya"]        #add element from another list/ tuples/ sets/ distionaries
thislist.extend(tropical)
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist.remove("orange")          #remove the first 'orange' only
print(thislist)
thislist.pop(1)                    #remove index 1 item
thislist.pop()                     #remove last item
del thislist[3]                    #remove index 3 item
del thislist                       #delete the list completely
thislist = ["apple", "banana", "cherry"]
thislist.clear()                   #delete content only, the list still remains
print(thislist)



#Loop List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

for x in ["apple", "banana", "cherry"]:
  print(x)


for i in range(len(thislist)):           #range is a range from a number to a number, range(startNumber, stopNumber, incrementation) for n in range(): //// x=range()   for n in x:
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#List Comprehension
newlist = []
for x in thislist:
  if "a" in x:
    newlist.append(x)

newlist = [x for x in thislist if "a" in x]               #newlist = [expression for item in iterable if condition == True]

print(newlist)

newlist = [x for x in thislist if x != "apple"]
newlist = [x.upper() for x in thislist]
newlist = [x for x in range(10) if x < 5]
newlist = ['hello' for x in newlist]
newlist = [x if x != "banana" else "orange" for x in fruits]          # replace banana with orange (Return the item if it is not banana, if it is banana return orange)

print(newlist)


#Sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()        #.sort() is procedure, not function
thislist.sort(reverse = True)      #descending
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


def myfunc(n):
  return abs(n - 50)                #how close the number is to 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()                                        #by default, it is case sensitive, capital letters first then lower case
print(thislist)

thislist.sort(key = str.lower)                          #if want case-insensitive sort, add key = str.lower
print(thislist)

thislist.reverse()                                      #reverse them
print(thislist)


#Copy List
#"list2 = list1" is not creating a new list. It is simply creating a second label that points to the exact same memory address
list1=["omo",":)",":(","^v^"]
list2 = list1.copy()
# OR
list2 = list(list1)
# OR
list2 = list1[:]
print(list2)


#Join
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#OR
for x in list2:
  list1.append(x)
#OR
list1.extend(list2)








#TUPLE     < cannot change, add or remove items after the tuple has been created>
#tuple.count() and .index() only
thistuple = ("apple", "banana", "cherry")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(len(thistuple))
print(thistuple[-2:])
tuple1 = ("apple",)        #need to add comma to be a tuple, or else is a string
print(type(tuple1))

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change tuple value by converting it into a list and then convert it back into a tuple
#list can change value, use list.append() or + to add item, use .remove() to remove item
x = ("apple", "banana", "cherry")
x = list(x)
x[1] = "kiwi"
x+=("orange",)
x = tuple(x)
print(x)

#tuple can delete the whole tuple
del thistuple

#unpacked a tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits   #* is used when variables are less than items
print(green)
print(yellow)
print(red)                     #the items left are in one list

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


#Loop Tuple (same as list)
for x in fruits:
  print(x)


#Join Tuples
#can use + and *
mytuple = fruits * 2
print(mytuple)














#SET         < unordered, x duplicates (True==1, False==0), unchangeable but can add and remove items >
thisset = {"apple", "banana", "cherry"}
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)            #unordered!
print(len(thisset))
print(type(thisset))

thisset1 = thisset.copy()

for x in thisset:
  print(x)

print("banana" in thisset)
print("banana" not in thisset)

#Add
thisset.add("orange")

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)

mylist = ["kiwi", "strawberry"]         #can add any iterable object using set.update()
thisset.update(mylist)             #|=

#Remove
thisset.remove("banana")           #error if the item does not exist
thisset.discard("orange")          #no error if the item does not exist

x = thisset.pop()                  #random remove item cuz unordered
print(x)

print(thisset)

thisset.clear()                    #clear items only
del thisset                        #delete the set completely

#Join Set
set1 = {"a", "b", "c", 1, 2, 3}
set2 = {3, 4, 5}
list2 = (3, 4, 5)

#∪
set3 = set1 | set2               #join sets only, can more than two
#or
set3 = set1.union(list2)         #can join sets, lists and tuples to get sets, can more than two
print(set3)
#or use set.update() to join sets, lists, tuples to get sets
#but update is procedure not function

#∩
set3 = set1 & set2                #sets only, can >2
#or
set3 = set1.intersection(list2)   #can join sets, lists, tuples, can >2
print(set3)

set2.intersection_update(set1)    #&= procedure
print(set2)

set2 = {3, 4, 5}

#difference
set3 = set1 - set2                 #sets only
#or
set3 = set1.difference(list2)      #sets, tuples, lists
print(set3)

set1.difference_update(set2)       #-=
print(set1)

set1 = {"a", "b", "c", 1, 2, 3}

#symmetric differences
set3 = set1 ^ set2                          #sets only
#or
set3 = set1.symmetric_difference(list2)     #sets, tuples, lists
print(set3)

set1.symmetric_difference_update(set2)      #^=
print(set1)


#Frozenset   < set which its elements cannot be added or removed >
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#function: .copy(), .diffence() -, .intersection() &, .isdisjoint(), .issubset() <= // <, .issuperset() >= // >, .symmetric_difference() ^, union() |








#DICTIONARY   < ordered, changeable and do not allow duplicates >
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "year":2000,                        #Duplicate values will overwrite existing value
  "colors": ["red", "white", "blue"]
}
print(thisdict)
dict1 = dict(name = "John", age = 36, country = "Norway")     #one bracket only
x = ('key1', 'key2', 'key3')     #keys
y = 0                            #values
dict2 = dict.fromkeys(x, y)      #create dictionary
print(dict2)

print(thisdict["brand"])          #use key instead of index (key:values)
print(thisdict.get("year"))
x=thisdict.keys()                 #if the keys or values are changed, x and y will also update automatically
y=thisdict.values()
print(x)
print(y)
z=thisdict.items()           #get key,value in pair, will update automatically also
print(z)
print(type(thisdict))
print(len(thisdict))

#Copy
mydict = thisdict.copy()
mydict = dict(thisdict)

print(mydict.setdefault("brand",2000))       #dict.setdefault(keyname, value(optional))
print(mydict.setdefault("name","Mustang"))   #If the key exist, this parameter has no effect. If the key does not exist, this value becomes the key's value. Default value None

if "brand" in thisdict:              #key only
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change or add item
thisdict["year"] = 2018
thisdict.update({"year": 2020})
#Remove item
thisdict.pop("year")
thisdict.popitem()            #remove last item
del thisdict["electric"]
thisdict.clear()              #clear content
del thisdict                  #delete completely

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "year":2000,                        #Duplicate values will overwrite existing value
  "colors": ["red", "white", "blue"]
}

for x in thisdict:
  print(x)                    #print keys

for x in thisdict.keys():
  print(x)

for x in thisdict:
  print(thisdict[x])          #print values

for x in thisdict.values():
  print(x)

for x, y in thisdict.items():
  print(x, y)



#Nested Dictionary
myfamily = {               #big dictionary
  "child1" : {             #small dictionary
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#OR

child1 = {               #small dictionary, obj
  "name" : "Emil",       #y:obj[y]
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {            #big dictionary
  "child11" : child1,
  "child22" : child2,
  "child33" : child3
}

print(myfamily["child22"]["name"])

for x, obj in myfamily.items():     #x is big keys (child11,22,33), obj is big values, small dictionaries name
  print(x)

  for y in obj:         #y is small keys (name, year)
    print(y + ':', obj[y])












#IF...ELSE
is_logged_in = True
if is_logged_in:
  print("Welcome back!")

"""
Zero (0), empty strings (""), None, and empty collections = False.
Everything else is treated as True. (includes positive, negative numbers, and any non-empty string (even "False" is treated as True because it's a non-empty string))
"""

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

"""
The order must be:
1.regular parameters
2.*args
3.**kwargs
"""

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






"""
#https://youtu.be/kr0mpwqttM0?si=Te4loONg8tIvpWB4
#First-Class Function: A programming language is said to have "first-class functions" if it treats functions as first-class citizens.
#First-Class Citizen (or First-Class Object): An entity in a programming language that supports all the operations generally available to other entities. These operations typically include being assigned to a variable, passed as an argument to a function, and returned from a function.

#1. Assigning functions to variables
def square(n):
    return n * n

f = square    # f is also a function because no parentheses means no execution of function
print(square) # Prints the function object
print(f(5))   # Prints 25




#2. Passing functions as arguments (Higher-Order Functions)
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares) # Prints [1, 4, 9, 16, 25]

def cube(n):
    return n * n * n

cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)





#3. Returning functions from functions
def logger(msg):
    def log_message():
        print('Log:', msg)
    return log_message   #return function as variable, no execution

log_hi = logger('Hi!')        #log_hi is now a log_message function where msg is 'Hi!'
log_hi() #execute log_hi function which is log_message function. Prints 'Log: Hi!'





#4. Practical Example
def html_tag(tag):
    def wrap_text(msg):
        print('<{0}><{1}></{0}>'.format(tag, msg))
    return wrap_text

print_h1 = html_tag('h1')  #'h1' is tag
print_h1('Test Headline')  #'Test Headline' is msg












print('\n\n\n')
#https://youtu.be/FsAPt_9Bf3U?si=4AX3r2f_F7fU9Jni
#Decorators
def outer_function():
    message = 'Hi'

    def inner_function():
        print(message)
    return inner_function

my_func = outer_function()    #my_func = inner_function
my_func()                     #execute my_func means executing inner function (=inner_function())




def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function('Hi')
hi_func()




def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorated_display = decorator_function(display)        #display function as an argument is sent to decorator_function, decorated_function is now wrapper_function which the original_function is display
decorated_display()                                    #execute wrapper_function and means executing original_function() since it returns original_function() (with brackets!)




def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

display = decorator_function(display)        #this line also same as @decorator_function written before def display():
display() 




@decorator_function
def display2():
    print('display function2 ran')

display2()




def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):                  #add *args and **kwargs because maybe the original function needs parameters but we dont know how much parameters needed
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Justin',18)





def changecase(func):
  def myinner():
    return func().upper()      #"Hello Sally".upper() because myfunction() return "Hello Sally"
  return myinner

def myfunction():
  return "Hello Sally"

myfunction = changecase(myfunction)
print(myfunction())




#SAME AS
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

"""




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
    """Takes a number and returns its square value."""
    #Hi
    return number ** 2

# Accessing the documentation string
print(calculate_square.__doc__)        #.__doc__ (docstring only, no comment #)

print(calculate_square.__name__)       #.__name__ function name




import functools               #import functools to use @functools.wraps()

def changecase(func):
  @functools.wraps(func)       #to preserce the function name and docstring (if not, output would be myinner)
  def myinner():
    """docstring in myinner"""
    return func().upper()
  return myinner

@changecase
def myfunction():
  """docstring in myfunction"""
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

x = pow(2,3)            #x to the power of y  // can use 2**3 (exponention operator)
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

"""
x = -1
if x < 0:
  raise Exception("Sorry, invalid")   #raise an error

x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")     #can define the type of error
"""



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





"""VIRTUAL ENVIRONMENT (use command prompt)
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
"""










#OOP
class Person:
  species = "Human"               #Class property
  def __init__(self, name, age=18):     #self is required for python to send name of object to here (eg. p1)  #age = 18 default value
    self.name = name              #Object property (instance property)
    self.age = age                      #left side self.name is actually p1.name of attribute (eg.) while right side name is value get from the parameter name

  def greet(self):
    return "Hello, " + self.name   #although here need to use name, we dont need name as parameter (need self only)

  def welcome(self):
    message = self.greet()              #call another function in a function using self.function()
    print(message + "! Welcome to our website.")


p1 = Person("Emil")
p2 = Person("Tobias", 25)
print(p1.name, p1.age)
p1.welcome()         #call function using self.function()

p1.age = 26             #modify object property
Person.species = "Good" #modify class property

del p1.age            #delete property
print(p1.name)        #This works
# print(p1.age)       #This would cause an error

del Person.welcome

p1.city = "Oslo"      #add new property to this object only

print(p1.name, p1.city)
print(p2.name, p2.age)

print(p1.species)     #same class property
print(p2.species)

#The self parameter must be the first parameter of any method in the class.
#self can be any other name, just that there should be a parameter before any other parameter, but strongly recommend use self


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")      #use self.attributename (attribute same as property)

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()



class Calculator:
  def add(self, a, b):
    return a + b
calc = Calculator()
print(calc.add(5, 3))    #can use function normally




class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1                    #can modify in class
    print(f"Happy birthday! You are now {self.age}")

p1 = Person2("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()



#__str__
print(p1)    #without __str__

class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"     #with __str__, can control what is returned when the object is printed

p1 = Person3("Tobias", 36)
print(p1)






class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []              #all objects have empty songs list at first, no need parameter

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()




#INHERITANCE
class Student(Person):     #create child class(derived class) from parent class(base class), class child(parent):
  pass

x = Student("Mike", 16)
print(x.greet())




class Person:   #parent
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):   #child
  def __init__(self, fname, lname):    #The child's __init__() function overrides the inheritance of the parent one (to add property of object to student)
    Person.__init__(self, fname, lname)   #To keep the inheritance of the parent's __init__() function

class Student(Person):
  def __init__(self, fname, lname, year):    #add new parameter for new property
    super().__init__(fname, lname)       #Person. or super().
    self.graduationyear = year           #add new property

  def welcome(self):                    #add new function
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)




#POLYMORPHISM
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):     #override the move() method
    print("Sail!")

class Plane(Vehicle):
  def move(self):     #override the move() method
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()       #execute the same method for three classes




#ENCAPSULATION
class Person:
  def __init__(self, name, age, salary):
    self.name = name
    self.__age = age         #Private property: add double underscore prefix
    self._salary = salary    #Protected property: add single underscore prefix (like putting a "Staff Only" sign on an unlocked door)

  def get_age(self):         #add a get method to access a private property
    return self.__age

  def set_age(self, age):    #add a set method to modify a private property
    if age > 0:              #can validate data before setting it
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Emil", 25, 12000)
print(p1.name)

#print(p1.__age)            This will cause an error (private property)
print(p1.get_age())
print(p1._Person__age)      #Name Mangling: add _class__ can access private property but not recommend because It defeats the purpose of encapsulation

p1.set_age(26)
print(p1.get_age())

print(p1._salary)           #Can access, but shouldn't



#
class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):      #private method: can only be used by other methods inside the class, cannot be called directly from outside the class
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result)
print(calc._Calculator__validate(5))   #Name Mangling, not recommend










#INNER CLASSES
class Computer:
    def __init__(self, brand):
        self.brand = brand
        # List to hold our complex RAM objects
        self.ram_sticks = []          #because it's one-to-many relationship, so we slowly add on the RAM sticks on each computer afterwards

    def add_ram(self, size, speed, gen, brand):
        # 1. Use the inner blueprint to build a detailed RAM object
        new_ram = self.RAM(size, speed, gen, brand)       #create a new object under RAM class
        
        # 2. Add this new object to the computer's list
        self.ram_sticks.append(new_ram)
        print(f"Added: {brand} {size}GB {gen} ({speed}MHz) stick.")

    def show_system_specs(self):
        # Calculate total RAM by looping through the objects
        total_gb = sum(stick.size for stick in self.ram_sticks)    #stick is just x like for x in range(5)    ram_sticks is one of the properties of Computer while size is one of the properties of RAM

        #SAME AS
        #for x in self.ram_sticks  (self.ram_sticks is a list of RAM objects)
            #total_gb = total_gb + x.size    (add the size of each RAM objects)
        
        print(f"\n--- {self.brand} System Specs ---")
        print(f"Total Memory: {total_gb}GB")
        print("Installed Modules:")
        
        # Loop through each RAM object to print its specific properties
        for i, stick in enumerate(self.ram_sticks, 1):          #count i for self.ram_sticks starts from 1
            print(f"  Slot {i}: {stick.brand} {stick.size}GB {stick.gen} @ {stick.speed}MHz")
    
    def run_memory_diagnostics(self):
        print("\nRunning Memory Diagnostics...")
        # The computer tells each RAM stick to test itself
        for stick in self.ram_sticks:
            stick.run_diagnostics()     #each RAM object run this inner function

    # --- THE INNER CLASS ---
    class RAM:
        def __init__(self, size, speed, gen, brand):
            # Now the RAM holds multiple distinct properties
            self.size = size
            self.speed = speed
            self.gen = gen
            self.brand = brand
            
        def run_diagnostics(self):
            # The RAM has its own behavior
            print(f"Testing {self.brand} {self.size}GB {self.gen} module... Status: OK")


# --- USAGE ---

# 1. Create the main outer object
my_pc = Computer("Asus")

# 2. Add multiple RAM sticks with full details
my_pc.add_ram(size=16, speed=3200, gen="DDR4", brand="Corsair")
my_pc.add_ram(size=16, speed=3200, gen="DDR4", brand="Corsair")
my_pc.add_ram(size=32, speed=3600, gen="DDR4", brand="G.Skill")

# 3. View the system specs (Outer class behavior)
my_pc.show_system_specs()

# 4. Trigger the diagnostics (Outer class triggering inner class behavior)
my_pc.run_memory_diagnostics()






class Computer:
    # 1. We add parameters for the CPU details right here in the main blueprint
    def __init__(self, brand, cpu_name, cpu_speed):
        self.brand = brand
        
        # 2. We pass the variables down to the inner class
        self.cpu = self.CPU(cpu_name, cpu_speed)    #Create new CPU object

    def show_specs(self):
        print(f"Computer: {self.brand}")
        self.cpu.display_cpu()           #.cpu refers to the attribute of Computer object (4 lines before)
        print("-" * 20)

    # --- THE INNER CLASS ---
    class CPU:
        def __init__(self, cpu_brand, speed):
            self.cpu_brand = cpu_brand
            self.speed = speed

        def display_cpu(self):
            print(f"CPU: {self.cpu_brand} running at {self.speed}")


# Now we can build computers with totally different CPUs!

# PC 1 gets an Intel processor
my_pc = Computer("Dell", "Intel Core i7", "2.8 GHz")

# PC 2 gets an AMD processor
gaming_pc = Computer("Alienware", "AMD Ryzen 9", "4.5 GHz")

# PC 3 gets an Apple processor
macbook = Computer("Apple", "M2 Max", "3.5 GHz")


my_pc.show_specs()
gaming_pc.show_specs()
macbook.show_specs()













r'''

#FILE HANDLING
#File Open

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""

"""
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

f = open("filehandling.txt","at")
f.close()

f = open("filehandling.txt","rt")      #open(filename, modes)
#same as f = open("filehandling.txt")
f.close()

f = open(r"C:\Users\HP\Documents\Siting\physics engine\Folder A\file_a.txt", "rt")   #specify the file path if it is located in a different location   (need add r before " because \ is an escape character)
print(f.read())     #print content in file
f.close()

#or
with open("filehandling.txt") as f:        #using with to open file no need to write close to close file
  print(f.read())

with open("filehandling.txt") as f:
  print(f.read(5))

with open("filehandling.txt") as f:
  print(f.readline())
  print(f.readline())   #read first two lines

with open("filehandling.txt") as f:
  for x in f:           #read the whole file line by line
    print(x)



#Write
with open("filehandling.txt", "a") as f:
  f.write("Now the file has more content!")   #append

with open("filehandling.txt") as f:
  print(f.read())

with open("demofile.txt", "w") as f:          #overwrite
  f.write("Woops! I have deleted the content!")

with open("demofile.txt") as f:
  print(f.read())



import os
os.remove("filehandling.txt")    #delete file

if os.path.exists("filehandling.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#os.rmdir("myfolder")     #remove folder (can only remove empty folders)

'''












#NumPy (Numerical Python)
import numpy as np

print(np.__version__)


#ndarray (N-dimensional array)
arr = np.array([1, 2, 3, 4, 5])  #pass a list, tuple or any array-like object into the array() method
arr = np.array((1, 2, 3, 4, 5))  #pass tuple
arr = np.array(range(0, 10, 2))     #pass generator or iterator
arr = np.arange(0, 10, 0.5)         #arange(start(inclusive), stop(exclusive), step(can be float, unlike range))
print(arr)
print(type(arr))                 #numpy.ndarray type


#0-D array / scalars
zerodarr = np.array(42)
print(zerodarr)
#print(zerodarr[0])   ERROR!

#1-D array
onedarr = np.array([1, 2, 3, 4, 5])
print(onedarr)
print(onedarr[2])

#2-D array   (2d matrix)
twodarr = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
#same as
#twodarr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print(twodarr)
print(twodarr[1, 2]) #row, column

#3-D array   (3d matrix)
threedarr = np.array([[[1, 2, 3], [4, 5, 6]],
                      [[11, 22, 33], [44, 55, 66]]])
print(threedarr)
print(threedarr[1, 0, 2])  #layer, row, column

#higher D array
higherdarr = np.array([1, 2, 3, 4], ndmin=5)   #define the number of dimensions using ndmin argument
print(higherdarr)
print(higherdarr[0, 0, 0, 0, -2])  #negative indexing


#check dimensions
print(zerodarr.ndim)
print(threedarr.ndim)



print(higherdarr.ndim)

"""
NumPy ndarray objects: they must have a regular, rectangular (or hyper-rectangular) shape
"""
#arr = np.array([[1, 2, 3], [3, 4, 5, 6, 7], [2, 6]])       ERROR!


#Create an array of all zeros
arr = np.zeros(100)    #np.zeros(size)
print(arr)



#Slicing    [start:end:step]  all optional
print(onedarr[::])
print(twodarr[1, 1:4])     #second row, second column to fifth column (exclusive)
print(twodarr[0:2, 2])
print(twodarr[0:2, 1:4])   #return 2-d array


#Data types   (dtype)
"""
i - integer (int)
b - boolean (bool)
u - unsigned integer
f - float (float)
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
"""

arr = np.array([1, 2, 3, 4], dtype='i4')  #can define data type and size(in byte)
print(arr.dtype)                          #int32 (32 bits)

arr = np.array(['appple', '', 'cherry'], dtype=bool)
print(arr.dtype)
print(arr)

arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9], dtype=int)   #floor to integer
print(arr)


arr = np.array([1, 0, 3])
newarr = arr.astype(bool)   #creates a copy of the array, specify the data type as a parameter
print(newarr)
print(newarr.dtype)



#Copy vs View
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()          #copy create a new array (wont be affected by the original one)
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
y = arr.view()          #**data / value** of view and original will be affected by each other (shape x)
arr[0] = 42
print(arr)
print(y)
y[0] = 100
print(arr)
print(y)

print(x.base)           #copy no base (None)
print(y.base)           #view has base  attribute refers to the original object



#Shape
print(twodarr.shape)    #row, column in tuple
print(threedarr.shape)  #layer, row, column in tuple
print(higherdarr.shape)


#Reshape: add or remove dimensions or change number of elements in each dimension
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)      #1d to 2d (4 x 3 = 12 (same number of elements)) (newarr is view of ori arr, not create a new arr, but shape wont affect ori one)
print(newarr)
print(newarr.base)

newarr2 = arr.reshape(2, 3, 2)   #1d to 3d (2 x 3 x 2 = 12(same number of elements))
print(newarr2)

newarr3 = arr.reshape(2, 2, -1)    #-1 is unknown, numpy will calculate it for us (cannot pass more than one -1)
print(newarr3)

newarr4 = newarr3.reshape(-1)     #flatten arr into 1d arr
print(newarr4)



#Iterating
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

arr = np.array([[0, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:    #print value in 1d arr
  print(x)

for x in arr:
  for y in x:    #2d arr use 2 for loop to print value in scalar
    print(y)
#same as
for x in np.nditer(arr):   #or use np.nditer(arr) instead of a lot of for loops
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['f8']):     #can change data type using op_dtypes, need to add flags=['buffered'] because it doesnt change data type in the array and need extra space to perform this action
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['bool'], casting='unsafe'):
  print(x)

for x in np.nditer(arr[:, ::2]):     #slicing
  print(x)

for idx, x in np.ndenumerate(arr):      #enumeration: idx: count item in array one by one from (0, 0) for 2d, x: item in array
  print(idx, x)




#Join
"""
n-d array has n number of axes, max index of axis is n-1.
Exp: 2d array
[[1,2],
 [3,4]]
if axis = 0: add new rows (stack below the two existing rows) [[1, 2], [3, 4], [5, 6], [7, 8]]
if axis = 1: add new columns (add behind each existing row) [[1, 2, 5, 6], [3, 4, 7, 8]]

shape is (2, 2)
Axis 0 is the first number (the size of the first dimension).
Axis 1 is the second number (the size of the second dimension).
"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2, arr1))   #default is axis = 0 (first dimension of 1d array is column)
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



#Stack
"""
stack always adds a brand-new dimension
n-d array can stack n-d array with max index of axis (parameter) = n
Ex[: 1d array
if axis = 0: treat the 1d array as one of the row in a 2d array
if axis = 1: treat the 1d array as one of the column in a 2d array
"""

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)      #first axis of 1d array is row but not column because stack will add one more dimension
print(arr)
arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=2)
print(arr)


#hstack, vstack, dstack (maybe add d(1d or 2d), maybe remains)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))   #hstack is like concatenate with axis column
print(arr)

arr = np.vstack((arr1, arr2))   #vstack is like stack with axis row
print(arr)

arr = np.dstack((arr1, arr2))   #dstack stacks along axis 2
print(arr)

"""
dstack
1. if the stacked array dimension < 3, promote it to 3d first ( like (3,) to (1,3,1) and (2,3) to (2,3,1) )
2. if dimension >= 3, just remains.
3. then, get the size of result array by adding the the third dimension size number together (like two(1,3,1)dstack to(1,3,2); two(2,3,4,5)dstack to(2,3,8,5))
"""





#Split (split evenly if possible, if not, np.array_split: the extra will be distributed to from the beginning; np.split(): error occurs)
#split an array into several arrays in a list
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

newarr = np.array_split(arr, 3, axis=1)    #split along column
print(newarr)

newarr = np.hsplit(arr, 3)     #opposite of hstack (same goes vsplit(), dsplit())
print(newarr)




#Search
arr = np.array([1, 2, 3, 4, 5, 4, 4])   #np.where() search a value that fulfils, return a tuple contain array of index(es)
x = np.where(arr == 4)
print(x)
x = np.where(arr%2 == 1)
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7.5)    #used on sorted array, perform binary search, return index(es) where the value(s) should be inserted to maintain the search order
print(x)

x = np.searchsorted(arr, 7)      #default start the search from left so return the first index
print(x)

x = np.searchsorted(arr, 7, side='right')   #find index starting from right
print(x)

x = np.searchsorted(arr, [2, 6.5, 8.3, 9, 10])   #use array for more than 1 value
print(x)




#Sort (alphabetical or numeric or boolean)(return a copy of array, original unchanged)
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
arr = np.array([[3, 2, 4], [5, 0, 1]])   #sort the deepest dimension only
print(np.sort(arr))
arr = np.array([True, False, True])
print(np.sort(arr))





#Filter    (will flatten all n-d arrays into 1d array)
#A boolean index list is a list of booleans corresponding to indexes in the array
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]   #boolean index list
newarr = arr[x]      #filtered_array = ori_arr[boolean_index_list]
print(newarr)


filter_arr = []
for element in arr:     #create boolean index list
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr[filter_arr]

#OR

filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)




#1. len(arr) return first num in shape
# 1D Array
arr1 = np.array([10, 20, 30, 40])
print(len(arr1))  # Output: 4
# 2D Array (2 rows, 3 columns)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(len(arr2))  # Output: 2 (returns the number of rows)

#2. arr.shape return Dimensions of the Array
print(arr2.shape)  # Output: (2, 3) -> (rows, columns)
print(arr2.shape[0])  # Output: 2 (Get number of rows (axis 0))
print(arr2.shape[1])  # Output: 3 (Get number of columns (axis 1))

#3. arr.shape return Total Number of Elements
print(arr2.size)  # Output: 6 (2 rows * 3 columns)














#RANDOM
from numpy import random
x = random.randint(100)   #random integers from 0(inclusive) to 100(exclusive)
print(x)

x = random.rand()         #random float from 0(inclusive) to 1(exclusive)
print(x)

x=random.randint(100, size=(3, 5))   #generate array with random integers
print(x)

x = random.rand(3, 5)                #array with random float
print(x)

x = random.choice([3, 5, 7, 9])      #choose a value in array randomly
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)


#Data Distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
"""
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
The probabilities of getting 3, 5, 7, 9 in the array are 0.1, 0.3, 0.6, 0.0 respectively
"""

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))   #return 2d array with size 3 x 5
print(x)



#Random Permutation (change arrangement)
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)      #procedure, not function (make changes to the original one)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))   #function, the original arr arrangement remains





'''

#Seaborn Module
import matplotlib.pyplot as plt
import seaborn as sns

"""
discrete random variable, X
X-axis: 0 <= X < 1
"""
sns.displot([0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5])     #array is the y value in the distribution
plt.show()

"""
continuous random variable (random used here, need to import random from numpy)
"""
sns.displot(random.normal(size=1000), kind="kde")   #kind optional, kde = Kernel Density Estimate used for continuous random variable
plt.show()



#Normal Distribution
x = random.normal(loc=1, scale=2, size=(2, 3))     #x is the array that stores the random test values, loc is mean, scale is standard deviation, size is shape of array
print(x)

sns.displot(x, kind="kde")
plt.show()

sns.displot(random.normal(size=1000), kind="kde")
plt.show()


#Binomial Distribution (success or fail)    y-axis is number of getting x times success in n trials
sns.displot(random.binomial(n=10, p=0.5, size=(1000, 2)))
plt.show()

data = {       #******
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()



#Poisson Distribution
x = random.poisson(lam=2, size=10)
print(x)

sns.displot(random.poisson(lam=2, size=1000))     #lamda is mean
plt.show()
  
data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}
sns.displot(data, kind="kde")
plt.show()

data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}
sns.displot(data, kind="kde")
plt.show()











from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#Uniform Distribution
x = random.uniform(low=2, high=10, size=(100, 2))     #low (lower bound) default 0.0, high (upper bound) default 1.0
print(x)
sns.displot(x, kind='kde')
plt.show()


#Logistic Distribution
x = random.logistic(loc=1, scale=2, size=(50))    #loc (mean) default 0, scale (standard deviation) default 1
print(x)
sns.displot(x, kind="kde")
plt.show()

data = {
  "normal": random.normal(scale=2, size=1000),
  "logistic": random.logistic(size=1000)
}
sns.displot(data, kind="kde")
plt.show()


#Multinomial Distribution  (like binomial but binomial has success and fail only, this can have multiple result (like dice) and use diff color to represent)
x = random.multinomial(n=12, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6], size=(6000))
print(x)
sns.displot(x, kind="kde")
plt.show()


#Exponential Distribution (https://youtu.be/WKFk0NXyO50?si=zFCp_gD9IKxTSiyn&t=136)
sns.displot(random.exponential(scale=2, size=1000), kind="kde")      #scale (lambda, interval between two events) default 1.0
plt.show()


#Chi Square Distribution (x square, x: randomly selecting a single value from a standard normal distribution (follow probability of normal distribution))
x = random.chisquare(df=2, size=(100, 3))      #df (degree of freedom): if 3 means sum of square of three randomly selected value from three standard normal distribution
sns.displot(x, kind="kde")
plt.show()

data = {
  "df1": random.chisquare(df=1, size=(1000)),
  "df2": random.chisquare(df=2, size=(1000)),
  "df3": random.chisquare(df=3, size=(1000))
}
sns.displot(data, kind="kde")
plt.show()


#Rayleigh Distribution
x = random.rayleigh(scale=2, size=(100, 2))       #scale (standard deviation) default 1.0
print(x)
sns.displot(x, kind="kde")
plt.show()


#Pareto Distribution
sns.displot(random.pareto(a=3, size=1000))     #a change the percentage (1.16 for 20% factors cause 80% outcome)
plt.show()

#Zipf Distribution    (pareto continuous, zipf discrete)
"""
Zipf's Law: In a collection, the nth common term is 1/n times of the most common term.
E.g. the 5th most common word in English occurs nearly 1/5 times as often as the most common word.
linear line when log
nth term is 1/(n power a) times of the most common term
"""
x = random.zipf(a=1.01, size=1000)       #a (distribution parameter) (a must be greater than 1)
sns.displot(x[x<10])
plt.show()

"""
x[x<10]
Step 1:The Condition (x < 10)
When you type x < 10, NumPy looks at every single one of your 1,000 generated numbers and asks, "Is this less than 10?"
It creates a hidden list of True and False answers. (e.g., [True, True, False, True...])

Step 2: The Filter (x[...])
When you wrap that condition in brackets next to your original array x, NumPy applies that True/False list like a mask.
It throws away all the numbers that got a "False" (anything 10 or higher) and only plots the numbers that got a "True".
"""


'''














import numpy as np

#UFUNC (Universal Functions) Change or compute the values inside the array element-by-element
x = [1, 2, 3, 4]      #can use for any array-like objects (array, list, tuple)
y = [4, 5, 6, 7]

#with ufunc
z = np.add(x, y)
print(z)

#OR

#without ufunc
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)


#create ufunc
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)      #ufunc = np.frompyfunc(function, numberOfArgumentArray, numberOfOutputArray)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

print(type(np.add))
print(type(myadd))
print(type(np.concatenate))

if type(np.add) == np.ufunc:    #check if the function is a ufunc
  print('add is ufunc')
else:
  print('add is not ufunc')



#Arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([5, 2, 4, 7, 9, 20])

newarr = np.add(arr1, arr2)    #value in arr1 + arr2
print(newarr)

newarr = np.subtract(arr1, arr2)  #arr1 - arr2
print(newarr)

newarr = np.multiply(arr1, arr2)  #arr1*arr2
print(newarr)

newarr = np.divide(arr1, arr2)    #arr1/arr2
print(newarr)

newarr = np.power(arr1, arr2)     #arr1 power arr2
print(newarr)

newarr = np.mod(arr1, arr2)       #remainder arr1 % arr2
print(newarr)
#same
newarr = np.remainder(arr1, arr2)
print(newarr)

newarr = np.divmod(arr1, arr2)     #return 2 arrays: one is whole number quotient of arr1 / arr2, one is remainder
print(newarr)

arr = np.array([-1, -2, 1, 2, 3, -4])
newarr = np.absolute(arr)          #absolute (always positive)
print(newarr)



#Rounding Decimals
arr = np.trunc([-3.1666, 3.6667])  #return the float number closest to zero
print(arr)
#same
arr = np.fix([-3.1666, 3.6667])
print(arr)

arr = np.around(3.1666, 2)          #, 2 means round off to 2 dp, add 1 if >= 5
print(arr)

arr = np.floor([-3.1666, 3.6667])   #floor, nearest lower integer
print(arr)

arr = np.ceil([-3.1666, 3.6667])    #ceil, nearest upper integer
print(arr)



#Logs   (build in method got base 2, 10, e only)
arr = np.arange(1, 10)      #return array with integers from 1 (included) to 10 (not included)
print(arr)

print(np.log2(arr))         #base 2

print(np.log10(arr))        #base 10

print(np.log(arr))          #base e


from math import log        #import log function from math

nplog = np.frompyfunc(log, 2, 1)   #create ufunc for log at other base
print(nplog(100, 15))       #log 100 at base 15



#Summations
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])    #sum of all elements in both arrays
print(newarr)

"""
Example for 2d array:
axis = 0 (row):
squash all the rows together vertically.
The result is effectively grouped by column
(you get one total for column A, one for column B, etc.)

axis = 1 (column):
squash all the columns together horizontally.
The result is effectively grouped by row
(you get one total for row 1, one for row 2, etc.).
"""
newarr = np.sum([arr1, arr2], axis=0)   #2d array cuz [1d array, 1d array]
print(newarr)

newarr = np.sum([arr1, arr2], axis=1)
print(newarr)


newarr = np.cumsum(arr)       #cummulative summation: 2nd element = 1st + 2nd, 3rd = 1st + 2nd +3rd, ....
print(newarr)



#Products
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)              #return product of all elements in the array
print(x)

x = np.prod([arr1, arr2])     #product of all elements in 2d array
print(x)

newarr = np.prod([arr1, arr2], axis=1)
print(newarr)


newarr = np.cumprod(arr)      #cummulative product: 3rd = 1st*2nd*3rd
print(newarr)



#Differences
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)         #difference between two successive elements (total number of elements = ori number - 1) (1st = 2nd - 1st, 2nd = 3rd - 2nd)
print(newarr)

newarr = np.diff(arr, n=2)    #n=2 means perform method twice
print(newarr)
#same
newarr = np.diff(np.diff(arr))
print(newarr)



#Finding LCM, Lowest Common Multiple
num1 = 4
num2 = 6
x = np.lcm(num1, num2)     #lcm for normal numbers
print(x)

arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)     #lcm for values in array (will reduce by 1d)
print(x)



#Finding GCD, Greatest Common Divisor or HCF, Highest Common Factor
num1 = 6
num2 = 9
x = np.gcd(num1, num2)     #hcf for normal numbers
print(x)

arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)     #hcf for values in array (reduce 1d)
print(x)



#Trigonometric
x = np.sin(np.pi/2)    #***in radians (np.sin(), np.cos(), np.tan())
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)

arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)    #degree to radian
print(x)

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)    #radian to degree
print(x)

x = np.arcsin(1.0)     #inverse sin function (arcsin(), arccos(), arctan())
print(x)

arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)

base = 3               #or opposite and adjacent
perpendicular = 4
x = np.hypot(base, perpendicular)    #find hypotenues using pythagoras theorem
print(x)


#Hyperbolic















#Set Operations  (****1d array only)
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)    #find unique elements
print(x)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)    #union
print(newarr)

newarr = np.intersect1d(arr1, arr2, assume_unique=True)    #intersect(assume_unique is optional argument to speed up computation)
print(newarr)

newarr = np.setdiff1d(arr1, arr2, assume_unique=True)     #To find only the values in the first set that is NOT present in the seconds set (like arr1 - arr2)
print(newarr)

newarr = np.setxor1d(arr1, arr2, assume_unique=True)      #To find only the values that are NOT present in BOTH sets
print(newarr)













"""

import matplotlib.pyplot

print(matplotlib.__version__)



import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])     #two x values of two points (x1, x2)
ypoints = np.array([0, 250])   #two y values of two points (y1, y2)
plt.plot(xpoints, ypoints)     #normal plot syntax, draw a line from point to point
plt.show()

xpoints = np.array([1, 2, 6, 8])   #can have many points
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)    #default x value is 0,1,2,3,4,5...
plt.show()





xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

#Markers (parameter: fmt, marker, markersize/ ms, markeredgecolor/ mec, markerfacecolor/ mfc)
plt.plot(xpoints, ypoints, 'o')   #with "o", plot without line
plt.show()

plt.plot(ypoints, marker = 'o')   #line with plot
plt.show()

plt.plot(ypoints, marker = '*')   #use * to mark plot (more marker in python matplotlib markers)
plt.show()

#parameter format string (fmt)(marker line color)
plt.plot(ypoints, 'o:r')   #: dotted, - solid, -- dashed, -. dashdot
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'y')  #can use color syntax, hexadecimal color values, or 140 supported color names
plt.show()

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'hotpink', mfc = '#4CAF50')




#Line (parameter: linestyle/ ls, color/ c, linewidth/ lw)
plt.plot(ypoints, ls = '-.', c = '#4CAF50', linewidth = '7.5')
plt.show()

#multiple lines
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)    #plot all then show
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1, y1, x2, y2)   #plot together
plt.show()




#Labels and title (parameter: fontdict)(function: xlabel(), ylabel(), title())
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y, marker="o")

plt.title("Sports Watch Data")   #title
plt.xlabel("Average Pulse")      #x-axis
plt.ylabel("Calorie Burnage")    #y-axis
plt.show()

#font properties for title and labels, position the title
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Sports Watch Data", fontdict = font1, loc = 'left')
plt.xlabel("Average Pulse", fontdict = font2, loc = 'left')
plt.ylabel("Calorie Burnage", fontdict = font2)
plt.plot(x, y)
plt.show()




#Grid (parameter: axis, color, linestyle, linewidth)(function: grid)
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x, y)
plt.grid()       #add grid
plt.show()

plt.plot(x, y)
plt.grid(axis = 'x')   #add x axis grid only
plt.show()

plt.plot(x, y)
plt.grid(axis = 'y')
plt.show()

plt.plot(x, y)
plt.grid(color = 'green', linestyle = '--', linewidth = 1.5)
plt.show()




#Subplot (function: subplot(), plot(), title(), suptitle())

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)         #(has 1 row, 2 columns of subplot, and this plot is the first plot)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)         #second plot
plt.plot(x,y)

plt.show()


#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(2, 1, 1)         #2 rows 1 column
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()



#title
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")      #small title for subplot

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")     #small title for subplot

plt.suptitle("MY SHOP")  #super title for the entire figure
plt.show()




#Scatter (Showing correlation or relationship between two independent continuous variables (while line graph showing trends))
#(parameter: c/color, c, s, alpha, cmap)(function: scatter(), colorbar())
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)                 #scatter plot syntax
plt.title("relationships between the observations")   #title
plt.xlabel("age of car")      #x-axis
plt.ylabel("speed of car")
plt.show()


#day one, the age and speed of 13 cars:
plt.scatter(x, y)
#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91])
plt.scatter(x, y)

plt.show()


#color all dots (parameter: color/c)
plt.scatter(x, y, color = 'hotpink')
plt.show()


#color each dot (parameter: c)
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c=colors)   #color each dot
plt.show()

#colormap (parameter: cmap)(a list of colors, where each color has a value that ranges from 0 to 100)
#such as viridis, nipy_spectral, more in python matplotlib scatter
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
plt.scatter(x, y, c=colors, cmap='viridis')   #name of colormap
plt.colorbar()           #optioanal, can show the colorbar
plt.show()


x = np.random.randint(100, size=(100))    #random generate values from 0 to 99, fit in 1d array with 100 columns
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')   #alpha is opacity (0 is totally transparent, 1 is fully opaque)
plt.colorbar()
plt.show()




#Bars (parameter: color, width/height(default 0.8)(vertical use width, horizontal use height))(function: bar(), barh())
x = np.array(["A", "B", "C", "D"])    #label of each bar
y = np.array([3, 8, 1, 10])           #height of each bar
plt.bar(x, y)                         #create bar syntax (label, height)
plt.show()

plt.barh(x, y)                        #horizontal bar syntax
plt.show()

plt.bar(x, y, color = "#4CAF50", width = 0.1)
plt.show()




#Histrogram (histogram: continuous range of number, bar: distinct categories (x-axis))
#(function: hist())(parameter: bins, edgecolor)
x = np.random.normal(170, 10, 250)    #where data collected from, using numpy normal distrbution, loc=mean, scale=standard deviation, size=size of array
print(x)
plt.hist(x)        #create histogram syntax, need 1d data only (no need x, y or label, because height is the frequency)
plt.show() 


#set width (bins)
x = np.random.normal(170, 10, 250)

#1. auto
plt.hist(x, bins="auto")
plt.show()

#2. set total number of bins
plt.hist(x, bins=10)
plt.show()

#3. custom bin edges (data type of parameter is list, range, np.ndarray)
step = 5
bins = np.arange(min(x), max(x)+step, step)   #stop not included, so add 1 step
plt.hist(x, bins=bins, edgecolor="black", color="green")
plt.show()

bins = range(140, 205, 5)
plt.hist(x, bins=bins, edgecolor="black", color="green")
plt.show()



#Pie Charts (parameter: labels, startangle, explode, shadow, colors)(function: pie(), legend(parameter: title))
#first wedge starts from the x-axis and moves counterclockwise (like what we do in math)
y = np.array([3.5, 2.5, 2.5, 1.5])     #frequency of each piece(wedge)
plt.pie(y)
plt.show() 

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]    #optional, add label for each wedge
plt.pie(y, labels = mylabels)
plt.show() 

plt.pie(y, labels = mylabels, startangle=90)     #first wedge starts from 90 degree (default is 0)
plt.show()

myexplode = [0.2, 0, 0, 0]        #in array
plt.pie(y, labels = mylabels, explode = myexplode)    #explode make certain wedge(s) to stand out
plt.show() 

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)   #shadow, add shadow to the whole pie chart
plt.show()

mycolors = ["black", "hotpink", "b", "#4CAF50"]
plt.pie(y, labels = mylabels, colors = mycolors)   #set colors to each wedge
plt.show() 

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")          #legend function add list of label of each wedge, parameter: title (optional, title for the legend)
plt.show() 

"""

