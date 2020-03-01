"""
Initial investigation of matplotlib.  This is the corresponding Python file to a Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 3/1/2020
"""

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

basic_plot = plt.plot(np.array([1, 2, 1]))
assert type(basic_plot) == list

fig = plt.figure()
plot1 = fig.add_subplot(2, 2, 1)
plot2 = fig.add_subplot(2, 2, 2)
plot3 = fig.add_subplot(2, 2, 3)
plot4 = fig.add_subplot(2, 2, 4)
assert type(fig) == matplotlib.figure.Figure

sec_per_mile = np.array([294, 309, 321, 312, 287, 271, 324])
mile_pace_plot = plt.plot(sec_per_mile, 'k--')

# Same plot as the one above, with the arguments passed more explicitly.
plt.plot(sec_per_mile, color='k', linestyle='dashed')
