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

# I hope you aren't being hard on yourself about any of it.
# You have to do what makes you happy and I lovingly understand.

# Numpy arrays provide the standard set operations
arr1 = np.array([3, 6, 9])
arr2 = np.array([9, 12, 15])

intersect_arr = np.intersect1d(arr1, arr2)
assert (intersect_arr == [9])

union_arr = np.union1d(arr1, arr2)
assert (union_arr == [3, 6, 9, 12, 15]).all()

diff_array = np.setdiff1d(arr1, arr2)
assert (diff_array == [3, 6]).all()

diff_array = np.setdiff1d(arr2, arr1)
assert (diff_array == [12, 15]).all()

xor_array = np.setxor1d(arr1, arr2)
assert (xor_array == [3, 6, 12, 15]).all()

# Numpy allows arrays to be saved and loaded from binary files.  The following example saves and loads
# the Fibonacci sequence array.
np.save('fib_array', arr)

loaded_arr = np.load('fib_array.npy')
assert (loaded_arr == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]).all()

# Based on a matrix dot product example: https://www.mathsisfun.com/algebra/matrix-multiplying.html
prices = np.array([3, 4, 2])
sold = np.array([[13, 8, 6], [9, 7, 4], [7, 4, 0], [15, 6, 3]]).T

assert (prices == [3, 4, 2]).all()
assert (sold == [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]).all()

# Matrix dot products can be computed with np.dot() or the Python '@' infix operator
dot_product = np.dot(prices, sold)
assert (dot_product == [83, 63, 37, 75]).all()

dot_product = prices @ sold
assert (dot_product == [83, 63, 37, 75]).all()

# Other linear algebra functions are provided such as matrix decomposition methods
# (which are way above my knowledge level)
q, r = np.linalg.qr(sold)
print(f'Q = {q}\n')
print(f'R = {r}\n')

# Q and R can then be used to reconstruct the matrix (this is basically all I know about matrix decompositions)
reconstructed_sold = q.dot(r)
reconstructed_sold = np.dot(q, r)
print(f'Q @ R = {reconstructed_sold}')

reconstructed_sold = q.dot(r).astype(np.int32)
assert (reconstructed_sold == [[13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]]).all()

# Numpy random numbers are "pseudo-random"
# (aka they use an assortment of seeds which will by themselves always produce the same numbers).
np.random.normal(size=(2, 2))

# This is proved with an explict seed instead of the 'random' libraries global random seed.
random_generator = np.random.RandomState(2)

first_rand = random_generator.randint(-1, 2, size=5)
second_rand = random_generator.randint(-1, 2, size=5)

# This random number generator will produce the same two lists as shown above.
other_random_generator = np.random.RandomState(2)

other_first_rand = other_random_generator.randint(-1, 2, size=5)
other_second_rand = other_random_generator.randint(-1, 2, size=5)

assert (first_rand == other_first_rand).all()
assert (second_rand == other_second_rand).all()

# Broadcasting [2 x 3] and [2 x 3].
arr1 = np.arange(6).reshape((2, 3))
arr2 = np.ones(6).reshape((2, 3))

assert arr1.shape == (2, 3)
assert arr2.shape == (2, 3)

result = arr1 + arr2

assert result.shape == (2, 3)

# Broadcasting [2 x 3 x 4] and [3 x 4].
arr1 = np.arange(24).reshape((2, 3, 4))
arr2 = np.arange(12).reshape((3, 4))

assert arr1.shape == (2, 3, 4)
assert arr2.shape == (3, 4)

result = arr1 - arr2

assert result.shape == (2, 3, 4)

# Broadcasting [2 x 3] and [3 x 2].
arr1 = np.arange(6).reshape((2, 3))
arr2 = np.arange(6).reshape((3, 2))

assert arr1.shape == (2, 3)
assert arr2.shape == (3, 2)

try:
    result = arr1 + arr2

    # This point will never be reached.
    assert False

except ValueError as e:
    assert str(e).strip() == 'operands could not be broadcast together with shapes (2,3) (3,2)'

# Broadcasting [2 x 3] and [2 x 1].
arr1 = np.arange(6).reshape((2, 3))
arr2 = np.arange(1, 3).reshape((2, 1))

assert arr1.shape == (2, 3)
assert arr2.shape == (2, 1)

result = arr1 + arr2

assert result.shape == (2, 3)

# Broadcasting [2 x 3 x 4] and [1 x 4].
arr1 = np.arange(24).reshape((2, 3, 4))
arr2 = np.arange(1, 5).reshape((1, 4))

assert arr1.shape == (2, 3, 4)
assert arr2.shape == (1, 4)

result = arr1 * arr2

assert result.shape == (2, 3, 4)
