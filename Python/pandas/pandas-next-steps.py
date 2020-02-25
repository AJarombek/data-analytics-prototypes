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
