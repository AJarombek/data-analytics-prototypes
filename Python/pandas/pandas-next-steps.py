"""
Further steps working with pandas.  This is the corresponding Python file to a Jupyter notebook of the same name.
Author: Andrew Jarombek
Date: 2/24/2020
"""

import json
import pandas as pd
import numpy as np

json_data = json.dumps({1: {'a': 1, 'b': 2}, 2: {'a': 3, 'b': 4}})

df = pd.read_json(json_data, orient='index')
assert (df.index == pd.Index([1, 2])).all()
assert (df.columns == pd.Index(['a', 'b'])).all()

new_json_data = df.to_json(orient='index')
assert json.loads(new_json_data) == json.loads(json_data)

feb_runs = [
    11.56, 12,
    2.34, 3.63, 2.85, 3.06, 3.92, 7.87, 12.5,
    2.81, 3.8, 2.65, 7.5, 2.63, 14, 13.21,
    1.28, 1.88, 2.64, 5.20, 3.76, 7.87, 12.59,
    2.81, 2.81, 3.45
]
buckets = [0, 3, 8, 15]
cuts = pd.cut(feb_runs, buckets)
assert len(cuts) == 26

codes = cuts.codes
assert (codes == [2, 2, 0, 1, 0, 1, 1, 1, 2, 0, 1, 0, 1, 0, 2, 2, 0, 0, 0, 1, 1, 1, 2, 0, 0, 1]).all()

categories: pd.IntervalIndex = cuts.categories
assert len(categories) == 3

value_counts: pd.Series = pd.value_counts(cuts)
assert type(value_counts.index) == pd.CategoricalIndex
assert (value_counts.values == [10, 10, 6]).all()

bucket_names = ["Slept too Long Run", "Regular Run", "Log Run/Workout"]
cuts = pd.cut(feb_runs, buckets, labels=bucket_names)
assert len(cuts) == 26

value_counts = pd.value_counts(cuts)
assert type(value_counts.index) == pd.CategoricalIndex
assert (value_counts.values == [10, 10, 6]).all()

cuts = pd.qcut(feb_runs, 4)
value_counts = pd.value_counts(cuts)
assert (value_counts.values == [9, 7, 6, 4]).all()

race_locations = pd.DataFrame({
    'location': [
        "Ocean Breeze Athletic Complex - New York, NY",
        "The Armory - New York, NY",
        "Tod's Point - Old Greenwich, CT",
        "Franklin D. Roosevelt State Park - Yorktown Heights, NY"
    ],
    'race_count': [3, 2, 1, 2]
})

locations: pd.Series = race_locations.T.loc['location']
assert len(locations) == 4

ny_locations = locations.str.contains('NY')
assert (ny_locations == [True, True, False, True]).all()

pattern = r"([A-Za-z'\.\s]+) - ([A-Za-z'\s]+), ([A-Z]{2})"
pattern_matches = locations.str.findall(pattern)

assert len(pattern_matches) == 4
assert pattern_matches[0] == [('Ocean Breeze Athletic Complex', 'New York', 'NY')]

matches = locations.str.findall(pattern).str[0]
assert len(matches) == 4
assert matches[0] == ('Ocean Breeze Athletic Complex', 'New York', 'NY')

states = matches.str.get(2)
assert (states == ['NY', 'NY', 'CT', 'NY']).all()

# Flatten data by using hierarchical indexing
exercises = pd.Series([2.1, 1, 0.5, 2, 2.15], index=[['run', 'run', 'run', 'walk', 'run'], [1, 2, 3, 4, 5]])
assert exercises['run'][1] == 2.1
assert exercises['run'][2] == 1
assert exercises['run'][3] == 0.5
assert exercises['walk'][4] == 2
assert exercises['run'][5] == 2.15

stacked_exercises = exercises.unstack()
unstacked_exercises = exercises.unstack().stack()

swapped_exercises = exercises.swaplevel(0, 1)
assert swapped_exercises[1]['run'] == 2.1
assert swapped_exercises[2]['run'] == 1
assert swapped_exercises[3]['run'] == 0.5
assert swapped_exercises[4]['walk'] == 2
assert swapped_exercises[5]['run'] == 2.15

sorted_exercises = exercises.sort_index(level=0)
assert exercises.iloc[3] == 2
assert sorted_exercises.iloc[3] == 2.15

sum_exercises = exercises.sum(level=0)
assert sum_exercises['run'] == 5.75
assert sum_exercises['walk'] == 2

location_indexed = race_locations.set_index(['location'])
assert (location_indexed.index == [
    "Ocean Breeze Athletic Complex - New York, NY",
    "The Armory - New York, NY",
    "Tod's Point - Old Greenwich, CT",
    "Franklin D. Roosevelt State Park - Yorktown Heights, NY"
]).all()

users = pd.DataFrame({
    'username': ['andy', 'joe', 'tom', 'fish'],
    'first': ['Andrew', 'Joseph', 'Thomas', 'Benjamin'],
    'last': ['Jarombek', 'Smith', 'Caulfield', 'Fishbein']
})

runs = pd.DataFrame({
    'username': ['andy', 'joe', 'andy', 'fish'],
    'date': ['2020-02-28', '2020-02-29', '2020-03-01', '2020-02-28'],
    'distance': [2.1, 8, 13, 5],
    'minutes': [16, 54, 92, 30],
    'seconds': [5, 51, 0, 10]
})

# Implicitly merge on the 'username' column in users and runs.  This is similar to a SQL INNER JOIN.
merged = pd.merge(users, runs)

assert (merged.iloc[2].values == np.array(['joe', 'Joseph', 'Smith', '2020-02-29', 8.0, 54, 51], dtype=object)).all()
assert (merged.values == np.array([
    ['andy', 'Andrew', 'Jarombek', '2020-02-28', 2.1, 16, 5],
    ['andy', 'Andrew', 'Jarombek', '2020-03-01', 13.0, 92, 0],
    ['joe', 'Joseph', 'Smith', '2020-02-29', 8.0, 54, 51],
    ['fish', 'Benjamin', 'Fishbein', '2020-02-28', 5.0, 30, 10]
], dtype=object)).all()

# Implicitly perform an inner join on the 'username' column in users and runs.  This is equivalent to the first merge.
inner_merged = pd.merge(users, runs, how='inner')

assert (merged.values == inner_merged.values).all()
