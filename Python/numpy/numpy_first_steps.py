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

# You can check the data type of numpy arrays with dtype
arr = np.array([1, 2, 3])
assert arr.dtype == np.int64

# Multi-dimensional arrays can also be created with array()
arr = np.array([[0, 0.5, 1, 1.5], [2, 2.5, 3, 3.5]])

assert arr.shape == (2, 4)
assert arr.dtype == np.float64
assert arr.ndim == 2

# Create an array filled with zeros.
arr = np.zeros(3)

assert len(arr) == 3
assert (arr == 0).all()
assert arr.dtype == np.float64

# Empty creates an array without initializing values.  Its content may just be garbage values.
empty_arr = np.empty((2, 2))

assert empty_arr.shape == (2, 2)

# 3D array
arr_3d = np.zeros((2, 2, 2))
assert arr_3d.ndim == 3

# Create an array filled with ones.
ones_arr = np.ones(3)
assert (ones_arr == 1).all()

full_arr = np.full((2, 3), 4)

assert full_arr.ndim == 2
assert full_arr.shape == (2, 3)
assert (full_arr == 4).all()

# Creates an array with the following content:
# [1, 0, 0]
# [0, 1, 0]
# [0, 0, 1]
eye_arr = np.eye(3)
id_arr = np.identity(3)

assert eye_arr.shape == (3, 3)
assert id_arr.shape == (3, 3)

assert (eye_arr == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]).all()
assert (id_arr == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]).all()

# numpy has more data types than Python arrays, allowing for more efficient memory storage of integers, floats.
# These data types are backed by C data types.
arr = np.array([2, 3])
assert arr.dtype == np.int64

arr = arr.astype(np.int32)
assert arr.dtype == np.int32

# 'i2' is equivalent to np.int16
arr = arr.astype('i2')
assert arr.dtype == np.int16

arr = arr.astype(np.int8)
assert arr.dtype == np.int8

# Typical Python slicing...
arr = np.arange(10)
assert len(arr[1:4]) == 3
assert (arr[1:4] == [1, 2, 3]).all()

# ...and indexing is available for numpy arrays
assert arr[1] == 1

# Change all values in the array
arr[:] = 2
assert (arr == 2).all()

# Without explicitly invoking copy(), slices return views (references) of the original array
arr = np.arange(10)
arr2 = arr[:]
arr2[:] = 2
assert (arr == 2).all()

arr = np.arange(10)
arr2 = arr[:].copy()
arr2[:] = 2
assert not (arr == 2).all()

# Unlike Python arrays, slices accept comma separated values.  Each value is a slice for a dimension of the array
arr_2d = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
assert arr_2d[1, 1] == 4

full_arr = arr_2d[:, :]
assert full_arr.shape == (3, 3)
assert len(full_arr) == 3
assert len(full_arr[0]) == 3
assert (full_arr == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]).all()

sliced_arr = arr_2d[1:, :1]
assert (sliced_arr == [[3], [6]]).all()

sliced_arr = arr_2d[:, 2]
assert (sliced_arr == [2, 5, 8]).all()

sliced_arr = arr_2d[:, 2:]
assert (sliced_arr == [[2], [5], [8]]).all()

arr_2d[:, 2] = 10
assert (arr_2d == [[0, 1, 10], [3, 4, 10], [6, 7, 10]]).all()

# Boolean indexed arrays
bool_idx_arr = arr_2d[2, arr_2d[2] == 6]
assert (bool_idx_arr == [6]).all()

bool_idx_arr = arr_2d[1, arr_2d[1] > 3]
assert (bool_idx_arr == [4, 10]).all()

bool_idx_arr = arr_2d[arr_2d > 3]
assert (bool_idx_arr == [10, 4, 10, 6, 7, 10]).all()

bool_idx_arr = arr_2d[~(arr_2d > 5)]
assert (bool_idx_arr == [0, 1, 3, 4]).all()

bool_idx_arr = arr_2d[(arr_2d < 2) | (arr_2d > 8)]
assert (bool_idx_arr == [0, 1, 10, 10, 10]).all()

bool_idx_arr = arr_2d[(arr_2d > 2) & (arr_2d < 8)]
assert (bool_idx_arr == [3, 4, 6, 7]).all()

arr_2d[(arr_2d > 3) & (arr_2d < 7)] = 20
assert (arr_2d == [[0, 1, 10], [3, 20, 10], [20, 7, 10]]).all()

# Fancy Indexing
arr_2d = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33], [41, 42, 43]])

indexed_arr = arr_2d[[0, 2]]
assert (indexed_arr == [[11, 12, 13], [31, 32, 33]]).all()

indexed_arr = arr_2d[[-4, -2]]
assert (indexed_arr == [[11, 12, 13], [31, 32, 33]]).all()

arr_3d = np.arange(18).reshape(2, 3, 3)
assert (arr_3d == [
    [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ],
    [
        [9, 10, 11],
        [12, 13, 14],
        [15, 16, 17]
    ]
]).all()

indexed_arr = arr_3d[[1]]
assert (indexed_arr == [[[9, 10, 11], [12, 13, 14], [15, 16, 17]]]).all()

indexed_arr = arr_3d[[0, 1], [1, 1]]
assert (indexed_arr == [[3,  4,  5], [12, 13, 14]]).all()

# Rearrange the axis.  The original shape was (X, Y, Z).  The resulting shape is (Z, X, Y)
transposed_arr = arr_3d.transpose((2, 0, 1))
assert (transposed_arr == [
    [
        [0, 3, 6],
        [9, 12, 15]
    ],
    [
        [1, 4, 7],
        [10, 13, 16]
    ],
    [
        [2, 5, 8],
        [11, 14, 17]
    ]
]).all()

# arange() works just like Python's range()
arr_2d = np.arange(12, 36, 2).reshape(3, 4)
assert (arr_2d == [[12, 14, 16, 18], [20, 22, 24, 26], [28, 30, 32, 34]]).all()

arr_2d = arr_2d.T
assert (arr_2d == [[12, 20, 28], [14, 22, 30], [16, 24, 32], [18, 26, 34]]).all()
