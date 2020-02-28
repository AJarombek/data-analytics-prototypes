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
patter_matches = locations.str.findall(pattern)
