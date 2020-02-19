"""
Using numba to speed up custom numpy functions.  This is the corresponding Python file to a
Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/17/2020
"""

import numpy as np
import numba as nb
from timeit import default_timer as timer


@nb.jit
def miles_to_kilometers(miles):
    return miles * 1.609


assert miles_to_kilometers(1) == 1.609

# Hold those you care for and who always have your back close.  You can overcome anything.

arr = np.array([1, 3, 5])
arr_kilometers = miles_to_kilometers(arr)
assert (arr_kilometers == [1.609, 4.827, 8.045]).all()

# Using numba functions are actually faster than numpy vectorization
start = timer()
for _ in range(1000):
    miles_to_kilometers(np.arange(100))
end = timer()

# 1.4 ms on my machine
print(f'Time taken with numba: {end - start} seconds')

# Numpy vectorization is slower but close behind numba
start = timer()
for _ in range(1000):
    np.arange(100) * 1.609
end = timer()

# 2.1 ms on my machine
print(f'Time taken with numpy vectorization: {end - start} seconds')

# Custom ufuncs with frompyfunc() are by far the slowest
miles_to_kilometers = np.frompyfunc(lambda miles: miles * 1.609, 1, 1)

start = timer()
for _ in range(1000):
    miles_to_kilometers(np.arange(100))
end = timer()

# 11.3 ms on my machine
print(f'Time taken with custom ufuncs with frompyfunc(): {end - start} seconds')
