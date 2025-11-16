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

def array_operations():
    arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    arr_asc = np.sort(arr) # sorts the array in ascending order.
    print(arr, "\n", arr_asc)
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8, 9])
    print(np.concatenate((a, b))) # "concat" can join only two things while "concatenate" can join two or more things.
    x = np.array([[1, 2], [3, 4]])
    y = np.array([[5, 6]])
    print(np.concatenate((x, y), axis=0))
    # print(np.concatenate((x, y), axis=1)) # This will throw an error, because all the input array dimensions except for the concatenation axis must match exactly.
    c =  np.arange(6)
    print(c.reshape((2, 3)))
    print(np.reshape(c, (3, 2), order='C'))
    # C means to read/write the elements using C-like index order.
    # F means to read/write the elements using Fortran-like index order.
    # A means to read/write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise. 
    # In Fortran, the first index changes rapidly & in C, the last index changes rapidly.

    d = np.array([2, 4, 6, 8, 10])
    d1 = d[np.newaxis, : ] # row-vector.
    d2 = d[:, np.newaxis]  # column-vector.
    print(d1.shape, d2.shape)
    d3 = np.expand_dims(d, axis=1) # adds an extre trailing dimension.
    d4 = np.expand_dims(d, axis=0) # adds an extra leading dimension.
    print(d3.shape, d4.shape)

    e = np.array([[1, 2, 3, 4], [5, 6, 7 ,8], [9, 10, 11, 12]])
    print(e[e < 5])
    five_up = (e > 5)
    print(e[five_up])
    print(e[e % 2 == 0]) # divisible by 2.
    print(e[(e > 5) & (e % 2 == 0)]) # stackng conditions using &. /
    five_and_up = (e > 5) | (e == 5) # stores boolean value.
    print(five_and_up)

    f1 = np.array([[1, 1], [2, 2]])
    f2 = np.array([[3, 3], [4, 4]])
    print(np.vstack((f1, f2))) # horizontal stack.
    print(np.hstack((f1, f2))) # vertical stack.
    f = np.arange(1, 25).reshape(2, 12)
    print(np.hsplit(f, 3)) # splits the array into 3 equal parts.
    print(np.hsplit(f, (3, 4))) # split array after 3rd & 4th element.
    f_copy = f.copy() # creates a complete copy.

    data = np.array([1, 2])
    ones = np.ones(2)
    print(data + ones) # adds elements
    print(data - ones) # subtracts elements
    print(data * ones) # multiplies elements
    print(ones / data) # divides elements
    print(sum(np.array([1, 3, 7, 12]))) # sum of elements 
    h = np.array([[1, 2], [3, 4]])
    print(h.sum(axis=0)) # sum along row.
    print(h.sum(axis=1)) # sum along column.

if __name__ == "__main__":
    # array_fundamentals()
    # basic_arrays()
    array_operations()