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

# Check the datatype of a grouping object
assert type(grouping) is pd.core.groupby.generic.DataFrameGroupBy

# Loop through each grouping object.  Prove it is made up of a string name and a DataFrame group.
for name, group in grouping:
    assert type(name) is str
    assert type(group) is pd.DataFrame
    print(name)
    print(group)

# Covert all 0 values in the DataFrame to NaN.
lines_coded_nan = lines_coded[lines_coded.apply(lambda x: x > 0)]

# Melt these values as I did in the above example.
lines_coded_nan_melted = pd.melt(lines_coded_nan.reset_index(), ['index'])

grouping_nan = lines_coded_nan_melted.groupby('index')

# 'count' will exclude NaN values.
years_coded = grouping_nan.count()
assert (
    years_coded.index == ['Groovy', 'HCL', 'HTML', 'Java', 'JavaScript', 'PHP', 'Python', 'SQL', 'Sass', 'Swift']
).all()

assert (years_coded.values == np.array([
    [7, 5],
    [7, 3],
    [7, 5],
    [7, 7],
    [7, 5],
    [7, 4],
    [7, 6],
    [7, 6],
    [7, 4],
    [7, 3]
], dtype=object)).all()

# 'count' does not exclude 0 values.
years_in_data_frame = grouping.count()

assert (years_in_data_frame.reset_index().values == np.array([
    ['Groovy', 7, 7],
    ['HCL', 7, 7],
    ['HTML', 7, 7],
    ['Java', 7, 7],
    ['JavaScript', 7, 7],
    ['PHP', 7, 7],
    ['Python', 7, 7],
    ['SQL', 7, 7],
    ['Sass', 7, 7],
    ['Swift', 7, 7]
], dtype=object)).all()

# The results of a groupby operation can be indexed.
grouping_nan_value = lines_coded_nan_melted.groupby('index')['value']
years_coded = grouping_nan_value.count()

assert (years_coded.reset_index().values == np.array([
    ['Groovy', 5],
    ['HCL', 3],
    ['HTML', 5],
    ['Java', 7],
    ['JavaScript', 5],
    ['PHP', 4],
    ['Python', 6],
    ['SQL', 6],
    ['Sass', 4],
    ['Swift', 3]
], dtype=object)).all()

# The above groupby indexing operation is syntactic sugar for the following groupby statement
grouping_nan_value = lines_coded_nan_melted['value'].groupby(lines_coded_nan_melted['index'])
years_coded_2 = grouping_nan_value.count()

assert (years_coded.values == years_coded_2.values).all()
