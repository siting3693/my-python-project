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

'''
NumPy ndarray objects: they must have a regular, rectangular (or hyper-rectangular) shape
'''
#arr = np.array([[1, 2, 3], [3, 4, 5, 6, 7], [2, 6]])       ERROR!




#Slicing    [start:end:step]  all optional
print(onedarr[::])
print(twodarr[1, 1:4])
print(twodarr[0:2, 2])
print(twodarr[0:2, 1:4])   #return 2-d array


#Data types   (dtype)
'''
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
'''

arr = np.array([1, 2, 3, 4], dtype='i4')  #can define data type and size
print(arr.dtype)

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
print(x)
y[0] = 100
print(arr)
print(x)

print(x.base)           #no base (None)
print(y.base)           #base  attribute refers to the original object



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

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in arr:    #print value in 1d arr
  print(x)

for x in arr:
  for y in x:    #2d arr use 2 for loop to print value in scalar
    print(y)
#same as
for x in np.nditer(arr):   #or use np.nditer(arr) instead of a lot of for loops
  print(x)

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):     #can change data type using op_dtypes, need to add flags=['buffered'] because it doesnt change data type in the array and need extra space to perform this action
  print(x)

for x in np.nditer(arr[:, ::2]):     #slicing
  print(x)

for idx, x in np.ndenumerate(arr):      #enumeration: idx: count item in array one by one from (0, 0) for 2d, x: item in array
  print(idx, x)




#Join
'''
n-d array has n number of axes, max index of axis is n-1.
Exp: 2d array
[[1,2],
 [3,4]]
if axis = 0: add new rows (stack below the two existing rows) [[1, 2], [3, 4], [5, 6], [7, 8]]
if axis = 1: add new columns (add behind each existing row) [[1, 2, 5, 6], [3, 4, 7, 8]]

shape is (2, 2)
Axis 0 is the first number (the size of the first dimension).
Axis 1 is the second number (the size of the second dimension).
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2, arr1))   #default is axis = 0
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)



#Stack
'''
stack always adds a brand-new dimension
n-d array can stack n-d array with max index of axis = n
Ex[: 1d array
if axis = 0: treat the 1d array as one of the row in a 2d array
if axis = 1: treat the 1d array as one of the column in a 2d array
'''

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)
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
arr = np.hstack((arr1, arr2))   #stack two arrays horizontally (side by side)
print(arr)

arr = np.vstack((arr1, arr2))   #stack two arrays vertically (top to bottom)
print(arr)

arr = np.dstack((arr1, arr2))   #d stands for depth (front to back)
print(arr)





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
'''
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
The probabilities of getting 3, 5, 7, 9 in the array are 0.1, 0.3, 0.6, 0.0 respectively
'''

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))   #return 2d array with size 3 x 5
print(x)



#Random Permutation (change arrangement)
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)      #procedure, not function (make changes to the original one)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))   #function, the original arr arrangement remains







#Seaborn Module
import matplotlib.pyplot as plt
import seaborn as sns

'''
discrete random variable, X
X-axis: 0 <= X < 1
'''
sns.displot([0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 5])     #array is the y value in the distribution
plt.show()

'''
continuous random variable (random used here, need to import random from numpy)
'''
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

