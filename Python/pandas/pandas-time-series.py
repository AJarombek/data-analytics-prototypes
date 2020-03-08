"""
Investigate working with dates/timestamps in pandas.  This is the corresponding Python file to a Jupyter notebook
of the same name.
Author: Andrew Jarombek
Date: 3/6/2020
"""

import pandas as pd
import numpy as np
from datetime import datetime
from pandas._libs.tslibs.timestamps import Timestamp

# You are always loved.  Do what brings you joy.

mile_races = pd.Series(
    np.array(['4:54', '4:47', '4:52', '4:48']),
    [datetime(2019, 12, 20), datetime(2020, 2, 13), datetime(2020, 2, 27), datetime(2020, 3, 5)]
)

assert mile_races.index.dtype == '<M8[ns]'

# Honestly dont remember which day this race happened.
first_race = mile_races.index[0]
assert type(first_race) == pd._libs.tslibs.timestamps.Timestamp
assert str(first_race) == '2019-12-20 00:00:00'

last_ocean_breeze_mile = mile_races['2/27/2020']
assert last_ocean_breeze_mile == '4:52'

last_ocean_breeze_mile_2 = mile_races['20200227']
assert last_ocean_breeze_mile == last_ocean_breeze_mile_2

races_2020 = mile_races['2020']
assert (races_2020.reset_index().values == np.array([
    [Timestamp('2020-02-13 00:00:00'), '4:47'],
    [Timestamp('2020-02-27 00:00:00'), '4:52'],
    [Timestamp('2020-03-05 00:00:00'), '4:48']
], dtype=object)).all()

races_feb_2020 = mile_races['2020-02']
assert (races_feb_2020.reset_index().values == np.array([
    [Timestamp('2020-02-13 00:00:00'), '4:47'],
    [Timestamp('2020-02-27 00:00:00'), '4:52']
], dtype=object)).all()

first_three_races = mile_races['12/1/2019':'2/29/2020']
assert (first_three_races.reset_index().values == np.array([
    [Timestamp('2019-12-20 00:00:00'), '4:54'],
    [Timestamp('2020-02-13 00:00:00'), '4:47'],
    [Timestamp('2020-02-27 00:00:00'), '4:52']
], dtype=object)).all()

# Current ski trip to Killington with Joe & Ben.
ski_trip = pd.date_range('2020-03-06', '2020-03-08')
assert type(ski_trip) == pd.core.indexes.datetimes.DatetimeIndex

ski_trip_2 = pd.date_range(start='2020-03-06', periods=3)
assert (ski_trip == ski_trip_2).all()

ski_trip_3 = pd.date_range(end='2020-03-08', periods=3)
assert (ski_trip == ski_trip_3).all()

# Sundays in March.
march_sundays = pd.date_range('2020-03-01', '2020-03-31', freq='W-SUN')
