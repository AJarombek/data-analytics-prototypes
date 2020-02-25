"""
Working with a SQL database with pandas.
Author: Andrew Jarombek
Date: 2/24/2020
"""

from sqlalchemy import MetaData, Column, Table, String, create_engine
import pandas as pd
import numpy as np

# SQLite is an in-application database.
engine = create_engine('sqlite:///test.sqlite')

meta = MetaData()

stuffed_animals = Table(
    'stuffed_animals', meta,
    Column('name', String, primary_key=True),
    Column('species', String, nullable=False),
    Column('caretaker', String, nullable=False)
)

meta.drop_all(engine)
meta.create_all(engine)

insert_dotty = stuffed_animals.insert().values(name='Dotty', species='Horse', caretaker='Andy')
insert_lily = stuffed_animals.insert().values(name='Lily', species='Bear', caretaker='Andy')
insert_fluffy = stuffed_animals.insert().values(name='Fluffy', species='Goat', caretaker='Andy')
insert_puffy = stuffed_animals.insert().values(name='Puffy Duffy', species='Dog', caretaker='Laurel')
insert_sock = stuffed_animals.insert().values(name='Sock Monkey', species='Monkey', caretaker='Laurel')

connection = engine.connect()

connection.execute(insert_dotty)
connection.execute(insert_lily)
connection.execute(insert_fluffy)
connection.execute(insert_puffy)
connection.execute(insert_sock)

result: pd.DataFrame = pd.read_sql('select * from stuffed_animals', engine)
print(result)

assert (result.head(3).values == np.array([
    ['Dotty', 'Horse', 'Andy'],
    ['Lily', 'Bear', 'Andy'],
    ['Fluffy', 'Goat', 'Andy']
])).all()
