"""
Using numba to speed up custom numpy functions.  This is the corresponding Python file to a
Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/17/2020
"""

import numpy as np
import numba as nb


@nb.jit
def miles_to_kilometers(miles):
    return miles * 1.609
