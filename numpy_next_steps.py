"""
Additional investigation into the numpy (numerical python) library.  This is the corresponding Python file to a Jupyter
notebook of the same name.
Author: Andrew Jarombek
Date: 2/11/2020
"""

import numpy as np
import matplotlib.pyplot as plt

arr = np.array([1, 4, 9])
sqrt_arr = np.sqrt(arr)
assert (sqrt_arr == [1, 2, 3]).all()

arr2 = np.array([3, 5, 7])
add_arr = np.add(arr, arr2)
assert (add_arr == [4, 9, 16]).all()

max_arr = np.maximum(arr, arr2)
assert (max_arr == [3, 5, 9]).all()

log2_arr = np.log2(np.array([1, 2, 4, 8]))
assert (log2_arr == [0, 1, 2, 3]).all()

points = np.arange(-1, 1.5, 0.5)
assert (points == [-1, -0.5, 0, 0.5, 1]).all()

xs, ys = np.meshgrid(points, points)
assert xs.shape == (5, 5)
assert ys.shape == (5, 5)

# Initial look at using numpy arrays with matplotlib
plt.imshow(xs, cmap=plt.cm.gray)
plt.colorbar()

plt.imshow(ys, cmap=plt.cm.gray)
plt.colorbar()

always_cared_for = True
arr1 = np.array(['you', 'are', 'always', 'very', 'loved'])
arr2 = np.array([1, 2, 3, 4, 5])

loved_arr = np.where(always_cared_for, arr1, arr2)
assert (loved_arr == ['you', 'are', 'always', 'very', 'loved']).all()

cond = np.array([True, False, True, False])
arr1 = np.array([1, 0, 3, 0])
arr2 = np.array([0, 2, 0, 4])

res_arr = np.where(cond, arr1, arr2)
assert (res_arr == [1, 2, 3, 4]).all()

res_arr = np.where(arr1 == 0, -1, arr1)
assert (res_arr == [1, -1, 3, -1]).all()

arr = np.array([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
assert arr.mean() == 14.3
assert arr.sum() == 143

assert (arr <= 1).any()
assert not (arr <= 1).all()

unique_arr = np.unique(arr)
assert (unique_arr == [1, 2, 3, 5, 8, 13, 21, 34, 55]).all()
