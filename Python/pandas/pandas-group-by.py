"""
Investigating the groupby() method in pandas.  This is the corresponding Python file to a
Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 3/4/2020
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

lines_coded = pd.DataFrame({
        '2014': [0, 4282, 0, 0, 0, 0, 0, 0, 0, 0],
        '2015': [0, 1585, 931, 0, 0, 0, 0, 0, 325, 0],
        '2016': [2008, 12962, 1122, 1413, 0, 5433, 0, 0, 942, 179],
        '2017': [6663, 12113, 1288, 2289, 10726, 3670, 163, 0, 812, 113],
        '2018': [16414, 4769, 1975, 10833, 698, 356, 4198, 3801, 1392, 2164],
        '2019': [13354, 4439, 20192, 4855, 2208, 357, 4468, 4089, 2622, 2324],
        '2020': [5022, 1664, 3666, 36, 0, 0, 727, 1332, 156, 652]
    },
    index=['JavaScript', 'Java', 'Python', 'HTML', 'Swift', 'PHP', 'Sass', 'HCL', 'SQL', 'Groovy']
)

assert lines_coded.shape == (10, 7)

lines_coded_v2 = lines_coded.reset_index()
assert (lines_coded_v2.columns == ['index', '2014', '2015', '2016', '2017', '2018', '2019', '2020']).all()

melted = pd.melt(lines_coded_v2, ['index'])
assert (melted.columns == ['index', 'variable', 'value']).all()

grouping = melted.groupby('index')
sum_lines = grouping.sum()
assert (sum_lines.reset_index().values == np.array([
    ['Groovy', 5432],
    ['HCL', 9222],
    ['HTML', 19426],
    ['Java', 41814],
    ['JavaScript', 43461],
    ['PHP', 9816],
    ['Python', 29174],
    ['SQL', 6249],
    ['Sass', 9556],
    ['Swift', 13632]
], dtype=object)).all()

mean_lines = grouping.mean()
assert (mean_lines.reset_index().values == np.array([
    ['Groovy', 776.0],
    ['HCL', 1317.4285714285713],
    ['HTML', 2775.1428571428573],
    ['Java', 5973.428571428572],
    ['JavaScript', 6208.714285714285],
    ['PHP', 1402.2857142857142],
    ['Python', 4167.714285714285],
    ['SQL', 892.7142857142857],
    ['Sass', 1365.142857142857],
    ['Swift', 1947.4285714285713]
], dtype=object)).all()
