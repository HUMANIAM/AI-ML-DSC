# hello numpy I start to use you to keep my learning of ML and its algorithms.

# Here is the readability of python so simple code.
def quicksort(arr):
    if len(arr) <= 1 : return arr

    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([5, 2, 3, 2, 2, 6, 10]))

# strings
h, w = "hello", "world"
hw = h + " " + w
print("message: %s\nLen: %d"%(hw, len(hw)))
print(hw.capitalize())
print(hw.upper())
print(hw.center(50))
print(hw.ljust(10))
print(h.replace('l', '(ell)'))
print('   word '.strip())

# Containers. [lists, dicts, sets, tuples]
# Lists
xs = [3, 1, 2]
print(xs, xs[1])
print("last: %d"%(xs[-1]))
xs[2] = "string with intgers"
print(xs)
xs.append(3.5)
print(xs)
xs.pop()
print(xs)

## slicing
nums = list(range(5))
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:3])
print(nums[:-1])
nums[2:4] = [100, 110]
print(nums)

## loops
animals = ['cat', 'dog', 'monkey']
for animal in animals:
    print("- Name: %s"%(animal))

for idx, animal in enumerate(animals):
    print("- index: %d name:%s"%(idx+1, animal))

## list comprehensions is really useful when one wants to transform one type to another.
nums = [1, 2, 3, 4]

### c++ way
nums_squares = []
for n in nums:
    nums_squares.append(n**2)

print(nums_squares)

### list comprehension way
even_nums_squares = [n**2 for n in nums if n%2==0]
print(even_nums_squares)

# tuples: is an immutable ordered list of values. A tuple is in many ways similar to a list; one of the most
# ----    important difference is that tuples can be used as keys in dicts and as elements in set while list can't
print("Tuples\n-------------")
relations = {("sherin", "maka"):"motherhood", ("ibrahim", "ahmed"):"brotherhood"}
pair = ("sherin", "maka")
print("Relationship between {0} is {1}".format(pair, relations[pair]))

# sets: unordered holds distinct values no duplication
print("SETS\n-------------")
family = {"ahmed", "samia", "tahra", "kamlia", "elsaid"}
print("ahmed" in family)
print("sohad" in family)
family = family.union({"maka", "sherin"})
print(family)

## Looping
for idx, member in enumerate(family):
    print("ID: %d Name:%s"%(idx+1, member))

# dictionaries. dictionary stores key and value pairs. like map in java or c++.
print("Dict\n-------------")
family = {"brother":"ahmed", "sister1":"tahra", "sister2":"samia"}
print("brother: %s"%(family["brother"]))
print("brother in dict: %d"%("brother" in family))
print("father in dict: %d"%("father" in family))
family["father"] = "elsaid"
print("father in dict: %d"%("father" in family))
print("mother: %s"%(family.get("mother", "None")))
family["mother"] = "kamlia"

## loop over dictionary.
print("--- My family names")

### Iterate by key
for relation in family:
    print("relation: %s name: %s"%(relation, family[relation]))

### Iterate by key and value.
for rel, name in family.items():
    print("relation: %s name:%s"%(rel, name))

### dict comprehension.
relations = ["brother", "sister1", "sister2", "mother", "father"]
names     = ["ahmed", "tahra", "samia", "kamlia", "elsaid"]
family = {rel:name for rel, name in zip(relations, names)}
print(family)

# Function
print("Function\n-------------")
def say_hello(to):
    print("hello, %s"%to)

## default paramters.
def say_hi(to="ahmed"):
    print("hi, %s"%to)

say_hello("ahmed")
say_hi()
say_hi("abdo")

# Class
print("-----------\nClass\n-------------")
class Member(object):
    def __init__(self, name, job) -> None:
        super().__init__()
        self.name = name
        self.job = job

    def tell_me_about_yourself(self):
        print("I am %s and I am working as %s"%(self.name, self.job))

member = Member("ibrahim", "programmer")
member.tell_me_about_yourself()

# Numpy: is the core library for scientific computing in python. It provides a high-performance multidimensional 
#-----  array object and tools for working with these arrays. 
print("-----------\nNumpy\n-------------")

## Arrays
# a numpy array is a grid of values. all of the same type, and is indexed by a tuple of nonnegative ints.
# the number of dims is the rank of the array; the shape of arr is a tuple of ints giving the size of the array along each dims.

import numpy as np

# 1D
a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1])
a[0] = 5

#2D
b = np.array([[1, 0], [0,1]])
print(b.shape)
print(b[0,0], b[0, 1])
b[:0] = np.array([-1, -1])
print(b)

## prebuilt arrays in numpy
a = np.zeros((2, 2))
print(a)

o = np.ones((2, 2), dtype=int)
print(o)

c = np.full((2, 2), 7, dtype=int)
print(c)

d = np.eye(2, dtype=int)
print(d)

r = np.random.random((2, 2))
print(r)

# indexing.
## slicing. so powerful.
a = np.array(range(1,13)).reshape((3,-1))
print(a)
print(a[:, -1]) # last column
print(a[-1, :]) # last row
print(a[-1, 1:3]) # the second and third column from the latest row
print(a[-1, -1]) # the most bottom-right element in the mat
print(a[1, :])  # rank1 > shape(4,)
print(a[1:2, :]) # rank2 > shape(1, 4)
print(a[:, -1:])  # lastest column with rank 2
print(a[[0, -1], [0, -1]]) # set manually

# boolen array indexing. Lets you pick out arbitrary elements of an array.
# you can use it when you want to pick specific kind of elements that satisfies some conditions.
print("mask:", a[a > 10])

#DataTypes. you can specify the data type with dtype key.
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print("Addition: ", np.add(x,y))
print("Substraction: ", np.subtract(x, y))
print("ElementWiseProduction: ", np.multiply(x, y))
print("MatrixMultiplication: ", np.dot(x, y))
print("Squar: ", np.sqrt(x))
print("sumPerCol: ", np.sum(x, axis=0)) # per column
print("sumPerRow: ", np.sum(x, axis=1)) # per row
print("MatrixSum: ", np.sum(x))

# transpose a matrix.
print("Transpose: ", x.T)
print("Transpose rank1 [.....] does nothing: ", np.array([1, 2, 3]).T)
print("Transpose rank2 [[......]] does: ", np.array([[1, 2, 3]]).T)

# BroadCasting. powerful mechanism that allows numpy to work with arrays of different shapes.
# ------------ most of the times we have small arrays and large arrays and we need to use the smaller ones to do
#              operations on the larger ones.
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)

# so slow.
for i in range(4):
    y[i, :] = x[i, :] + v

# using tiling
y = x + np.tile(v, (4, 1))

# using broadcasting
y = x + v

# functions that support broadcasting are called universal functions.
# Compute outer product of vectors
v = np.array([1,2,3])  # v has shape (3,)
w = np.array([4,5])    # w has shape (2,)
print(np.reshape(v, (3, 1)) * w)
"""
Broadcasting typically makes your code more concise and faster,
so you should strive to use it where possible.
"""

#SCIPY scientific computation library
from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 1], [1, 0], [2, 0]])
d = squareform(pdist(x, 'euclidean'))
print(d)

#MATPLOT plotting library.
from matplotlib import pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)

plt.xlabel("x axis label")
plt.ylabel("y axis label")
plt.title("Sin(x) and Cos(x)")
plt.legend(['Sin(x)', 'Cos(x)'])

# plt.show()

# SubPlots.
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title("Sin(x)")
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("Cos(x)")
plt.show()
