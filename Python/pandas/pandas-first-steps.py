"""
First steps working with pandas data structures.  This is the corresponding Python file to a
Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/17/2020
"""

import pandas as pd
import numpy as np

series = pd.Series([1, 2, 3, 4, 5])

assert series.equals(pd.Series([1, 2, 3, 4, 5]))
assert series.dtype == np.int64
assert (series.index == pd.RangeIndex(start=0, stop=5, step=1)).all()

series = pd.Series([1, 2, 3], index=['c', 'b', 'a'])
assert (series.index == pd.Index(['c', 'b', 'a'])).all()

assert series[1] == 2
assert series['b'] == 2

sub_series: np.array = series[['a', 'b']]
assert (sub_series == np.array([3, 2])).all()

sub_series: np.array = series[['b', 'b']]
assert (sub_series == np.array([2, 2])).all()

# Numpy vectorizations/functions can be performed on pandas Series
new_series = series ** 2
assert (new_series == [1, 4, 9]).all()

# Indexes can be checked for existance with 'in' ...
assert 'a' in series

# ... values can not.
assert 1 not in series

# You can create a series with a dictionary
races = {'freezer 5 mile': 5, 'armory night at the races': 1, 'ocean breeze miles mania': 1}
race_series = pd.Series(races)

assert (race_series == [5, 1, 1]).all()
assert (race_series.index == pd.Index(
    ['freezer 5 mile', 'armory night at the races', 'ocean breeze miles mania']
)).all()

series = pd.Series({1: 1, 2: 2, 3: 4, 4: 8}, np.arange(5))

assert (pd.notnull(series) == [False, True, True, True, True]).all()
assert (pd.isnull(series) == [True, False, False, False, False]).all()

assert (pd.notnull(series) == series.notnull()).all()
assert (pd.isnull(series) == series.isnull()).all()

# It didn't actually snow :(
snow = pd.Series([3, 0.1, 0], index=[17, 18, 19])
rain = pd.Series([1.1, 0, 0.6, 0], index=[16, 17, 18, 19])

snow_and_rain: pd.Series = snow + rain

assert pd.Series(snow_and_rain[16]).isnull().all()
assert snow_and_rain[17] == 3
assert snow_and_rain[18] == 0.7
assert snow_and_rain[19] == 0

snow.name = 'snow'
assert snow.name == 'snow'

assert (snow.index == pd.Index([17, 18, 19])).all()
snow.index = ['Feb 17th', 'Feb 18th', 'Feb 19th']
assert (snow.index == pd.Index(['Feb 17th', 'Feb 18th', 'Feb 19th'])).all()

runs = {
    'user': ['andy', 'andy', 'andy'],
    'type': ['run', 'core', 'run'],
    'date': ['02-19-2020', '02-19-2020', '02-18-2020'],
    'time': ['20:15', '8:00', '16:00']
}
frame: pd.DataFrame = pd.DataFrame(runs)

# Frame head and tail operate the same as UNIX head and tail commands
frame_head = frame.head(2)
assert frame_head.shape == (2, 4)
assert (frame_head.index == pd.Index([0, 1])).all()

frame_tail = frame.tail(2)
assert frame_tail.shape == (2, 4)
assert (frame_tail.index == pd.Index([1, 2])).all()

# Columns can be retrieved with property (dot) notation or indexing
assert frame.time.equals(pd.Series(['20:15', '8:00', '16:00']))
assert frame['time'].equals(pd.Series(['20:15', '8:00', '16:00']))

# Set all items in the 'time' column to '10:00'
frame['time'] = '10:00'
assert frame['time'].equals(pd.Series(['10:00', '10:00', '10:00']))

frame['time'] = np.array(['25:00', '8:00', '20:00'])
assert frame['time'].equals(pd.Series(['25:00', '8:00', '20:00']))

frame['date'] = pd.Series(['02-01-2020', '02-02-2020', '02-03-2020'], index=[1, 2, 0])
assert frame['date'].equals(pd.Series(['02-03-2020', '02-01-2020', '02-02-2020']))

columns = frame.columns
assert (columns == pd.Index(['user', 'type', 'date', 'time'], dtype='object')).all()

frame['distance'] = pd.Series([3.5, 3], index=[0, 2])
assert frame['distance'].loc[0] == 3.5
assert frame['distance'].isnull().loc[1] == True
assert frame['distance'].loc[2] == 3

assert (frame.columns == pd.Index(['user', 'type', 'date', 'time', 'distance'], dtype='object')).all()
del frame['distance']
assert (frame.columns == pd.Index(['user', 'type', 'date', 'time'], dtype='object')).all()

# Transposing in pandas works just like numpy
transposed_frame = frame.T
assert (transposed_frame.columns == pd.Index([0, 1, 2], dtype='object')).all()
assert (transposed_frame.index == pd.Index(['user', 'type', 'date', 'time'], dtype='object')).all()

transposed_frame = frame.T.T
assert (transposed_frame.columns == pd.Index(['user', 'type', 'date', 'time'], dtype='object')).all()
assert (transposed_frame.index == pd.Index([0, 1, 2], dtype='object')).all()

# Access all the values of a dataframe as a numpy array.
values = frame.values
assert (values == np.array([
    ['andy', 'run', '02-03-2020', '25:00'],
    ['andy', 'core', '02-01-2020', '8:00'],
    ['andy', 'run', '02-02-2020', '20:00']
])).all()

# Indexes in pandas are immutable
index = pd.Index(['a', 'b', 'c'])

try:
    index[3] = 'd'

    # Not Reached
    assert False
except TypeError as e:
    assert str(e) == 'Index does not support mutable operations'

reindexed_frame = frame.reindex([1, 2, 0])
assert (reindexed_frame.values == np.array([
    ['andy', 'core', '02-01-2020', '8:00'],
    ['andy', 'run', '02-02-2020', '20:00'],
    ['andy', 'run', '02-03-2020', '25:00']
])).all()

dropped_frame = frame.drop(2)
assert (dropped_frame.values == np.array([
    ['andy', 'run', '02-03-2020', '25:00'],
    ['andy', 'core', '02-01-2020', '8:00']
])).all()

dropped_frame = frame.drop([0, 2])
assert (dropped_frame.values == np.array([
    ['andy', 'core', '02-01-2020', '8:00']
])).all()

dropped_frame = frame.drop('user', axis=1)
assert (dropped_frame.values == np.array([
    ['run', '02-03-2020', '25:00'],
    ['core', '02-01-2020', '8:00'],
    ['run', '02-02-2020', '20:00']
])).all()

frame.drop('time', axis=1, inplace=True)
assert (frame.values == np.array([
    ['andy', 'run', '02-03-2020'],
    ['andy', 'core', '02-01-2020'],
    ['andy', 'run', '02-02-2020'],
])).all()
