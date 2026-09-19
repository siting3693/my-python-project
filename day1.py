#comment
'docstring'
"docstring"
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
