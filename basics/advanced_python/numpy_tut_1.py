import numpy as np
import math

""" Numpy array rules.
All elements of the array must be of the same type of data.

Once created, the total size of the array can't change.

The shape must be “rectangular”, not “jagged”; e.g., each row of a two-rdimensional array must have the same number of columns.

"""

def array_fundamentals():
    # a = np.array([[1, 2, 3], 
    #               [4, 5, 6]])

    a = np.array([1, 2, 3, 4, 5, 6])
    print(a) # (2, 3)
    print(a.shape)
    b = a[:3]
    print(b)
    b = a[3:]
    print(b)
    b[0] = 80 # numpy ndarrays make copies instead of views (python lists create views).
    # this means when "b" is changed, even "a" changes.
    print(b)
    print(a)

    # The number of dimensions of an array is contained in the ndim attribute.
    print(a.ndim)

    # The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension.
    print(a.shape)
    print(len(a.shape) == a.ndim)

    # The fixed, tota number of elements in array s contained in the size attribute.
    print(a.size)
    print(a.size == math.prod(a.shape))

    # The arrays are homogeneous, meaning they only contain elements of 1 datatype. 
    print(a.dtype)

def basic_arrays():
    print(np.zeros(2))  # array filled with zeroes.
    print(np.ones(2))   # identity matrix.
    print(np.empty(2))  # empty array with random values - saving memory & filling values later, hence speed factor.
    print(np.arange(3)) # create an array with range of elements.
    print(np.arange(2, 9, 2)) # contains a range of evenly spaced intervals, specify 1st number, last number & step size.
    print(np.linspace(0, 10, num=5)) # create an array with values that are spaced linearly in a specified interval.
    print(np.ones(2, dtype=np.int64)) # explictly mention the data-type.

if __name__ == "__main__":
    # array_fundamentals()
    basic_arrays()
