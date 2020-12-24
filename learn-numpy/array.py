import numpy as np

L = list(range(10))          #############
print(L)                     #############
L2 = [str(c) for c in L]     #python code#
print(L2)                    #############

# import array
# A = array.array('i', L)      #############
# pritn(A)                     #############

# integer array:
L3 = np.array([3.14, 4, 2, 3])
print(L3)

# Create a length-10 integer array filled with zeros
L4 = np.zeros(10, dtype=int)
print(L4)

# Create a 3x5 floating-point array filles with 1s
L5 = np.ones((3, 5), dtype=float) 
print(L5)

# Create a 3x5 array filled with 3.14
L6 = np.full((3,5), 3.14)
print(L6)

# Create an array filled with a linear squence
# String ar 0, ending at 20, steeping by 2
# this is similar to th4e built-in range() function
print(np.arange(0, 20, 2))

# Create an array of five values evenly spaced between 0 and 1
print(np.linspace(0, 1, 5))

# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
print(np.random.random((3, 3)))

# Create a 3x3  array of narmally distrubute random values
# with mean 0 and standard deviation 1
print(np.random.normal(0, 1, (3, 3)))

# Create a 3x3 array of random integers in the interval [0, 10)
print(np.random.randint(0, 10, (3, 3)))

# Create a 3x3 identity matrix
print(np.eye(3))

# Create an uninitialized array of three integers
# The values will be whatever happens to already ecist at that memory location
print(np.empty(3))

# seed for reproducibility
# seed : By specifying a seed, it is possible to fix the random number to be generated in advance. 
# This is used when reproducibility is required in analysis or processing that uses random numbers.
np.random.seed(0)

x1 = np.random.randint(10, size=6)            #One-dimensional array
x2 = np.random.randint(10, size=(3, 4))       #Two-dimensional array
x3 = np.random.randint(10 ,size=(3, 4, 5))    #Three-dimensioanl array

# Each array has attributes ndim (the number of dimensions), shape (the size of each dimension), and size (the total size of the array)
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)

# Another useful attribute is the dtype, the data type of the array 
print("dtype:", x3.dtype)

# Other attributes include itemsize, which lists the size (in bytes) of each array element, and nbytes, which lists the total size (in bytes) of the array
# In general, we expect that nbytes is equal to itemsize times size.
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")

# One important–and extremely useful–thing to know about array slices is that they return views rather than copies of the array data.
# This is one area in which NumPy array slicing differs from Python list slicing　
# in lists, slices will be copies.
print(x2)
# Let's extract a $2 \times 2$ subarray from this:
x2_sub = x2[:2, :2]
print(x2_sub)
# Now if we modify this subarray, we'll see that the original array is changed!
# This default behavior is actually quite useful: 
# it means that when we work with large datasets, we can access and process pieces of these datasets without the need to copy the underlying data buffer.
x2_sub[0, 0] = 99
print(x2_sub)
print(x2)

# Another useful type of operation is reshapring of arrays.
# The most flexible way of doing this is with the reshpe method.
# Note that for this to work, the size of the initial array must match the size of the reshaped array. 
#  Where possible, the reshape method will use a no-copy view of the initial array, but with non-contiguous memory buffers this is not always the case.
grid = np.arange(1, 10).reshape((3,3))
print(grid)

