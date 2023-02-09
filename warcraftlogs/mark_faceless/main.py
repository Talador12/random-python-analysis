"""
Analysis of "Mark of the Faceless" data

==========
===TODO===
==========
- get player list
- player with debuff column
- average damage per cast (raid)
- average damage per cast (player)
"""
import pandas as pd

df = pd.read_csv('data/mark_faceless_2023-02-09.csv')
print(df.info())

