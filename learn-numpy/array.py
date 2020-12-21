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