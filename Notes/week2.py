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
print(~3)    #~ is NOT (set 0 to 1 and 1 to 0)
'''
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
'''

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
