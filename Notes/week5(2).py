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

'''
Example for 2d array:
axis = 0 (row):
squash all the rows together vertically.
The result is effectively grouped by column
(you get one total for column A, one for column B, etc.)

axis = 1 (column):
squash all the columns together horizontally.
The result is effectively grouped by row
(you get one total for row 1, one for row 2, etc.).
'''
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
