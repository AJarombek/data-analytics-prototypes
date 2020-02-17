"""
Advanced numpy concepts.  This is the corresponding Python file to a Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/14/2020
"""

import numpy as np
from timeit import default_timer as timer

# Numpy arrays are made up of a pointer to data, a data type (dtype), a shape, and strides.
# Strides are the distance it takes (in bytes) in any dimension to advance to the next element
arr_1d_int = np.zeros(5, dtype=np.int64)

assert arr_1d_int.dtype == np.int64
assert arr_1d_int.shape == (5,)

# A 64 bit integer takes up 8 bytes - so the stride is 8.
assert arr_1d_int.strides == (8,)

arr_2d_int32 = np.zeros((4, 5), dtype=np.int32)

assert arr_2d_int32.dtype == np.int32
assert arr_2d_int32.shape == (4, 5)

# A 32 bit integer takes up 4 bytes.
# In the second dimension, a stride is 4 because the next element in that dimension is only 4 bytes away.
# In the first dimension, a stride is 20 because the entire second dimension (of length 5 * 4 bytes) is traversed
# to reach the next element.
assert arr_2d_int32.strides == (20, 4)

# Check the object hierarchy of numpy types
assert np.int64.mro() == [np.int64, np.signedinteger, np.integer, np.number, np.generic, object]

assert np.uint8.mro() == [np.uint8, np.unsignedinteger, np.integer, np.number, np.generic, object]

assert np.float64.mro() == [np.float64, np.floating, np.inexact, np.number, np.generic, float, object]

assert np.string_.mro() == [np.bytes_, bytes, np.character, np.flexible, np.generic, object]

assert np.object_.mro() == [np.object_, np.generic, object]

assert np.issubdtype(np.int64, np.number)
assert np.issubdtype(np.int64, np.signedinteger)
assert not np.issubdtype(np.uint16, np.signedinteger)

arr = np.arange(16)

# Reshaping arrays in numpy follows two different orderings - C and Fortran
# (named after the respective programming languages).  By default reshape() uses C ordering, which is row major.
# This means the row is filled out one at a time.
arr2 = arr.reshape((4, 4))
assert (arr2 == [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]).all()

# C ordering (row major) can be explicitly specified.
arr3 = arr.reshape((4, 4), order='C')
assert (arr3 == [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]).all()

# Fortran ordering (column major) fills out columns one at a time.
arr4 = arr.reshape((4, 4), order='F')
assert (arr4 == [
    [0, 4, 8, 12],
    [1, 5, 9, 13],
    [2, 6, 10, 14],
    [3, 7, 11, 15]
]).all()

arr = arr.reshape((4, 4))

raveled_arr = arr.ravel()
flattened_arr = arr.flatten()
assert (raveled_arr == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]).all()
assert (raveled_arr == flattened_arr).all()

fortran_raveled_arr = arr.ravel('F')
assert (fortran_raveled_arr == [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]).all()

# By default arrays are concatenated on axis 0 (row) ...
arr1 = np.array([[1], [2]])
arr2 = np.array([[3], [4]])
concat_arr = np.concatenate((arr1, arr2))
assert (concat_arr == [[1], [2], [3], [4]]).all()

concat_arr = np.concatenate((arr1, arr2), axis=0)
assert (concat_arr == [[1], [2], [3], [4]]).all()

# ... however they can be configured to concatenate on axis 1 (column)
concat_arr = np.concatenate((arr1, arr2), axis=1)
assert (concat_arr == [[1, 3], [2, 4]]).all()

# Equivalent to np.concatenate() on axis 0
concat_arr = np.vstack((arr1, arr2))
assert (concat_arr == [[1], [2], [3], [4]]).all()

# Equivalent to np.concatenate() on axis 1
concat_arr = np.hstack((arr1, arr2))
assert (concat_arr == [[1, 3], [2, 4]]).all()

# Split an array into multiple arrays at certain indexes.
arr = np.arange(10)
split_arr = np.split(arr, [2, 4, 9])

assert (split_arr[0] == [0, 1]).all()
assert (split_arr[1] == [2, 3]).all()
assert (split_arr[2] == [4, 5, 6, 7, 8]).all()
assert (split_arr[3] == [9]).all()

arr = np.arange(3).repeat(2)
assert (arr == [0, 0, 1, 1, 2, 2]).all()

repeat_arr = np.array([5]).repeat(5)
full_arr = np.full([5], 5)
assert (repeat_arr == [5, 5, 5, 5, 5]).all()
assert (full_arr == [5, 5, 5, 5, 5]).all()

tile_arr = np.tile(arr, (2, 1))
assert (tile_arr == [[0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]]).all()

tile_arr = np.tile(arr, (1, 2))
assert (tile_arr == [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]).all()

# Advanced broadcasting (vectorizations performed on an array) including creating a new axis for an existing array
arr1 = np.zeros((3, 3))
arr2 = np.array([1, 2, 3])
arr1[:] = arr2[:, np.newaxis]
assert (arr1 == [[1, 1, 1], [2, 2, 2], [3, 3, 3]]).all()

reduced_value = np.add.reduce(np.arange(10))
assert reduced_value == 45

# Logical AND chained with reduce() is equivalent to all()
arr = np.array([1, 1])
all_equal_one = np.logical_and.reduce(arr == 1)
assert all_equal_one

arr = np.arange(16).reshape((4, 4))

accumulated_arr = np.add.accumulate(arr, axis=0)
assert (accumulated_arr == [
    [0, 1, 2, 3],
    [4, 6, 8, 10],
    [12, 15, 18, 21],
    [24, 28, 32, 36]
]).all()

accumulated_arr = np.add.accumulate(arr, axis=1)
assert (accumulated_arr == [
    [0, 1, 3, 6],
    [4, 9, 15, 22],
    [8, 17, 27, 38],
    [12, 25, 39, 54]
]).all()

divide_arr = np.divide.outer(np.array([3, 6, 9]), np.array([1, 2, 3]))
assert (divide_arr == [[3, 1.5, 1], [6, 3, 2], [9, 4.5, 3]]).all()

mult_arr = np.multiply.outer(np.array([3, 6, 9]), np.array([1, 2, 3]))
assert (mult_arr == [[3, 6, 9], [6, 12, 18], [9, 18, 27]]).all()

# Reduce to the following array: [(0 + 1), (2 + 3), (4)]
reduce_add_arr = np.add.reduceat(np.arange(5), [0, 2, 4])
assert (reduce_add_arr == [1, 5, 4]).all()

# Custom ufuncs can be created with frompyfunc().  Note that these functions take a performance hit
# compared to their numpy counterparts.  There is a way to speed up custom functions to numpy-like performance
# with the numba library.


def miles_to_kilometers(miles):
    return miles * 1.609


# Create a custom unary unfunc (takes a single argument) that converts miles to kilometers
mile2km = np.frompyfunc(miles_to_kilometers, 1, 1)

arr = np.array([1, 3, 5])
converted_arr = mile2km(arr)
assert (converted_arr == [1.609, 4.827, 8.045]).all()


def comma_separated_strings(x, y):
    return f'{x}, {y}'


# Create a custom binary ufunc (takes two arguments) that concatenates two strings with a comma
cs_str = np.frompyfunc(comma_separated_strings, 2, 1)

arr1 = np.array(['first', 'last'])
arr2 = np.array(['andy', 'jarombek'])

cs_arr = cs_str(arr1, arr2)
assert (cs_arr == ['first, andy', 'last, jarombek']).all()

# The arrays returned from a custom frompyfunc() function always have the type object
assert cs_str(arr1, arr2).dtype == object
assert mile2km(arr).dtype == object

# The type can be more specific with the help of the vectorize() function.
mile2km = np.vectorize(miles_to_kilometers, otypes=[np.float64])
converted_arr = mile2km(arr)
assert (converted_arr == [1.609, 4.827, 8.045]).all()

cs_str = np.vectorize(comma_separated_strings, otypes=[np.unicode])
cs_arr = cs_str(arr1, arr2)
assert (cs_arr == ['first, andy', 'last, jarombek']).all()

assert converted_arr.dtype == np.float64
assert cs_arr.dtype == '<U14'

# Unfortunately, these custom ufuncs take a major performance hit
start = timer()
for _ in range(10000):
    mile2km(arr)
end = timer()

# 75 ms on my machine
print(f'Time taken with custom ufunc: {end - start} seconds')

start = timer()
for _ in range(10000):
    arr * 1.609
end = timer()

# 11 ms on my machine
print(f'Time taken with numpy vectorization: {end - start} seconds')

# More complex data types are possible in numpy arrays
metric_dtype = [('miles', np.int32), ('kilometers', np.float64)]
mi_km_arr = np.array([(1, 1.609), (2, 3.218)], dtype=metric_dtype)

assert mi_km_arr[0]['miles'] == 1
assert mi_km_arr[0]['kilometers'] == 1.609

# Sort a numpy array in place, similar to Python arrays
arr = np.array([2, 3, 1])
arr.sort()
assert (arr == [1, 2, 3]).all()

# Sort a numpy array, returning a new array instance
arr = np.array([2, 3, 1])
sorted_arr = np.sort(arr)

assert (sorted_arr == [1, 2, 3]).all()
assert (arr == [2, 3, 1]).all()

arr = np.array([[9, 6, 3], [8, 5, 2], [7, 4, 1]])
sorted_arr = np.sort(arr)
assert (sorted_arr == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]).all()

sorted_arr = np.sort(arr, axis=0)
assert (sorted_arr == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]).all()

sorted_arr = np.sort(arr, axis=1)
assert (sorted_arr == [[3, 6, 9], [2, 5, 8], [1, 4, 7]]).all()

# An indexer produced by argsort() is used to indirectly sort an array.
arr = np.array([6, 8, 3, 5, 1])
indexer = arr.argsort()
assert (indexer == [4, 2, 3, 0, 1]).all()

sorted_arr = arr[indexer]
assert (sorted_arr == [1, 3, 5, 6, 8]).all()

# You can also use different sorting algorithms (defaults to quick sort)
indexer = arr.argsort(kind='heapsort')
assert (indexer == [4, 2, 3, 0, 1]).all()

# The result is the same
sorted_arr = arr[indexer]
assert (sorted_arr == [1, 3, 5, 6, 8]).all()

arr = np.random.randn(1000)

start = timer()
for _ in range(1000):
    _ = arr[arr.argsort(kind='quicksort')]
end = timer()

# 36 ms on my machine
print(f'Time taken to sort with quicksort: {end - start} seconds')

start = timer()
for _ in range(1000):
    _ = arr[arr.argsort(kind='mergesort')]
end = timer()

# 41 ms on my machine
print(f'Time taken to sort with mergesort: {end - start} seconds')

start = timer()
for _ in range(1000):
    _ = arr[arr.argsort(kind='heapsort')]
end = timer()

# 62 ms on my machine
print(f'Time taken to sort with heapsort: {end - start} seconds')

# Perform a binary search on a sorted array.
arr = np.array([1, 2, 4, 8, 16, 32, 64])
index = arr.searchsorted(16)
assert index == 4

indexes = arr.searchsorted([2, 8, 32])
assert (indexes == [1, 3, 5]).all()

mmap = np.memmap('sample_mmap', dtype='float64', mode='w+', shape=(2, 2))
assert mmap.shape == (2, 2)
assert (mmap == [[0, 0], [0, 0]]).all()

# Alter the memory map in-place
mmap[0] = 1
assert (mmap == [[1, 1], [0, 0]]).all()

# Delete the memory map.  It will still exist as a binary file on disk.
mmap.flush()
del mmap

# Prove that the memory map no longer exists in the program.
try:
    mmap

    # This point is never reached
    assert False
except NameError:
    assert True
    print("mmap does not exist")

# Revive the memory map.  Its contents are the same
mmap = np.memmap('sample_mmap', dtype='float64', shape=(2, 2))
assert (mmap == [[1, 1], [0, 0]]).all()

# Flags provide additional information about a numpy array.
arr = np.random.randn(10)
assert arr.flags['C_CONTIGUOUS']
assert arr.flags['F_CONTIGUOUS']

arr = np.arange(4).reshape((2, 2))
assert arr.flags['C_CONTIGUOUS']
assert not arr.flags['F_CONTIGUOUS']

arr = np.ones((2, 2), order='F')
assert not arr.flags['C_CONTIGUOUS']
assert arr.flags['F_CONTIGUOUS']

# In theory summing contiguous data should be faster than non-contiguous data, however I haven't seen any
# evidence of this.
start = timer()
for _ in range(1000):
    np.ones((100, 100), order='C').sum(1)
end = timer()

# 20 ms on my machine
print(f'Time taken to sum contiguous data: {end - start} seconds')

start = timer()
for _ in range(1000):
    np.ones((100, 100), order='F').sum(1)
end = timer()

# 15 ms on my machine
print(f'Time taken to sum non-contiguous data: {end - start} seconds')
