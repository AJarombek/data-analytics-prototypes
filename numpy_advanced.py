"""
Advanced numpy concepts.  This is the corresponding Python file to a Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/14/2020
"""

import numpy as np

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
