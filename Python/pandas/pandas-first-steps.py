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

data_xctf = {
    '8K': ['24:20.80', '24:33.50', '24:58.80', None, '26:24.20'],
    '6K': ['18:58.80', '19:10.20', '19:25.80', '20:54.00', '20:20.50'],
    '5K': ['15:32.00', '15:39.00', '15:59.00', '17:31.60', '16:38.40'],
    '10000m': [None, None, '31:51.73', '35:50.22', None],
    '5000m': ['14:23.21', None, '15:27.01', '16:44.14', '15:27.64'],
    '3000m': ['8:32.83', '8:52.60', '8:51.80', '9:47.70', '9:03.60'],
    '1 Mile': ['4:20.59', '4:20.39', '4:40.34', '4:57.53', '4:40.76'],
    '1500m': ['3:54.67', '3:57.78', None, '4:32.14', '4:08.17']
}
run_dataframe = pd.DataFrame(
    data_xctf,
    index=['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek']
)

assert (run_dataframe.columns == pd.Index(
    ['8K', '6K', '5K', '10000m', '5000m', '3000m', '1 Mile', '1500m'],
    dtype='object'
)).all()

assert (run_dataframe.index == pd.Index(
    ['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek'],
    dtype='object'
)).all()

small_run_dataframe = run_dataframe['Joseph Smith':'Lisa Grohn']
assert (small_run_dataframe.index == pd.Index(['Joseph Smith', 'Ben Fishbein', 'Lisa Grohn'], dtype='object')).all()

small_run_dataframe = run_dataframe[1:3]
assert (small_run_dataframe.index == pd.Index(['Joseph Smith', 'Ben Fishbein'], dtype='object')).all()

small_run_dataframe = run_dataframe.loc[:, ['8K', '6K', '5K']]

assert (small_run_dataframe.columns == pd.Index(['8K', '6K', '5K'], dtype='object')).all()
assert (small_run_dataframe.index == pd.Index(
    ['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek'],
    dtype='object'
)).all()

# Women's XC PRs
lisa_slu_xc_prs = run_dataframe.iloc[3, [0, 1, 2]]
assert (lisa_slu_xc_prs.values == [None, '20:54.00', '17:31.60']).all()

# Men's Track PRs
mens_slu_tf_prs = run_dataframe.iloc[np.array([0, 1, 2, 4]), np.arange(3, 8)]
assert (mens_slu_tf_prs.columns == pd.Index(['10000m', '5000m', '3000m', '1 Mile', '1500m'], dtype='object')).all()
assert (mens_slu_tf_prs.index == pd.Index(
    ['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Andy Jarombek'],
    dtype='object'
)).all()

assert run_dataframe.at['Thomas Caulfield', '5000m'] == '14:23.21'
assert run_dataframe.iat[0, 4] == '14:23.21'

data_xctf = {
    '8K': [1460.80, 1473.50, 1498.80, np.nan, 1584.20],
    '6K': [1138.80, 1150.20, 1165.80, 1254.00, 1220.50],
    '5K': [932.00, 939.00, 959.00, 1051.60, 998.40]
}
run_sec_dataframe = pd.DataFrame(
    data_xctf,
    index=['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek']
)

# Tom and Joe's combined seconds for races.
tom_joe_seconds: pd.Series = run_sec_dataframe.iloc[0] + run_sec_dataframe.iloc[1]

assert type(tom_joe_seconds) == pd.Series
assert (tom_joe_seconds == [2934.3, 2289.0, 1871.0]).all()

# Everyones 400m pace for the 6K
pace_per_400_6k = run_sec_dataframe.loc[:, ['6K']] / 15
assert (pace_per_400_6k.values.astype(np.int32) == [[75], [76], [77], [83], [81]]).all()

# Pace per 400m for each race.
run_sec_dataframe / [20, 15, 12.5]

run_seconds_dataframe = run_sec_dataframe.T

fivek_200_pace = run_seconds_dataframe.loc['5K'] / 25
assert (fivek_200_pace.values.astype(np.int32) == [37, 37, 38, 42, 39]).all()

# Series and DataFrame types have methods for each arithmetic operation.
fivek_200_pace = run_seconds_dataframe.loc['5K'].div(25)
assert (fivek_200_pace.values.astype(np.int32) == [37, 37, 38, 42, 39]).all()

mean_func = lambda x: x.mean()
mean_run_sec = run_sec_dataframe.apply(mean_func)
assert (mean_run_sec.values.astype(np.int32) == [1504, 1185, 976]).all()

mean_run_sec = run_seconds_dataframe.apply(mean_func, axis='columns')
assert (mean_run_sec.values.astype(np.int32) == [1504, 1185, 976]).all()

sorted_run_sec = run_seconds_dataframe.sort_index()
assert (sorted_run_sec.index == pd.Index(['5K', '6K', '8K'], dtype='object')).all()
assert (sorted_run_sec.columns == pd.Index(
    ['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek'],
    dtype='object'
)).all()

sorted_run_sec = run_seconds_dataframe.sort_index(axis=1)
assert (sorted_run_sec.index == pd.Index(['8K', '6K', '5K'], dtype='object')).all()
assert (sorted_run_sec.columns == pd.Index(
    ['Andy Jarombek', 'Ben Fishbein', 'Joseph Smith', 'Lisa Grohn', 'Thomas Caulfield'],
    dtype='object'
)).all()

sorted_5k = run_seconds_dataframe.T.sort_values(by='5K')
assert (sorted_5k.loc[:, ['5K']].values == [[932], [939], [959], [998.4], [1051.6]]).all()

ranked_races = run_seconds_dataframe.T.rank()
assert (ranked_races.index == pd.Index(
    ['Thomas Caulfield', 'Joseph Smith', 'Ben Fishbein', 'Lisa Grohn', 'Andy Jarombek'],
    dtype='object'
)).all()

# Get an overview of different statistics about the DataFrame
described_df = run_seconds_dataframe.describe()
assert (described_df.index == pd.Index(
    ['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'],
    dtype='object'
)).all()

# Mean absolute deviation from mean value - the mean of all distances from the mean value.
mad_df = run_seconds_dataframe.mad()
assert (mad_df.values.astype(np.int32) == [189, 190, 193, 101, 211]).all()
