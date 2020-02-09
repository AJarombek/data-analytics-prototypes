"""
First investigative steps into the numpy (numerical python) library.  This is the corresponding Python file to a Jupyter
notebook of the same name.
Author: Andrew Jarombek
Date: 2/8/2020
"""

import numpy as np
from timeit import default_timer as timer

# Creates a numpy array containing five values.  The values are randomly generated with mean 0 and variance 1.
# Basically floating-point numbers close to zero.
# https://www.mathsisfun.com/data/standard-deviation.html
# Source: https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
random_array = np.random.randn(5)
assert len(random_array) == 5

# numpy arrays can be multi-dimensional
md_rand_array = np.random.randn(4, 3)
assert md_rand_array.size == 12
assert md_rand_array.shape == (4, 3)

# Create an array of ten integers ranging from 0 to 9.
arr = np.arange(10)

# Perform vectoriztion on the array.  In numpy, this is when a looping operation on an array
# is conducted without an actual for loop.
mult_arr = arr * 2
assert (mult_arr == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]).all()

div_arr = arr / 2
assert (div_arr == [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5]).all()

mod_arr = arr % 3
assert (mod_arr == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]).all()

# Vectorization operations create a new view of the array - they don't alter the original array.
assert (arr == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).all()
assert not (arr == [0, 1, 2, 3, 4, 5, 6, 6, 8, 9]).all()

# This vectorization creates an array where each value equals 'True'
equals_array = arr == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert len(equals_array) == 10

for item in equals_array:
    assert item

# Demonstrate the speed increase of using numpy arrays over built-in Python arrays
start = timer()
for _ in range(1000):
    _ = np.arange(1000) * 2
end = timer()

# 2 ms on my machine
print(f'Time taken with numpy arrays: {end - start} seconds')

start = timer()
for _ in range(1000):
    _ = [item * 2 for item in np.arange(1000)]
end = timer()

# 320 ms on my machine
print(f'Time taken with Python arrays: {end - start} seconds')

# Using the standard numpy array constructor
arr = np.array(['watched', 'frozen', 'broadway', 'with', 'fam', ',', 'race', 'in', 'a', 'bit'])
assert len(arr) == 10
