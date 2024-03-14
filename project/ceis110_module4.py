# -*- coding: utf-8 -*-
"""
CEIS110 Module 4

Purpose: Query database using SQL
Name: Your name
Date: Your date

Run ceis110_module3.py first to build weather database before running this program

Needs:
import sqlite3
import pandas as pd

"""

# %% Load the libraries

import sqlite3
import pandas as pd


# %% Module 4 Part 1 - DB Reads


print("CEIS110 Week 4 Part 1")

# file names for database and output file
dbFile = "weather.db"

# format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

# connect to and query weather database
conn = sqlite3.connect(dbFile)
# Create SQL command
selectCmd = " SELECT * FROM observations ORDER BY timestamp; "


# print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)

# %% Module 4 Part 2 - DB Reads
# To see the lowest and highest temperatures observed in this data set...

print("CEIS110 Week 4 Part 2")

# create SQL command
selectCmd = " SELECT MIN(temperature), MAX(temperature) FROM observations; "

# print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)


selectCmd = "SELECT temperature, windspeed, \
    textDescription FROM observations where textDescription = 'Clear'; "
result = pd.read_sql_query(selectCmd, conn)
print(result)


# %% References
"""
Tips and references:

runfile('filename.py')

# Delete all variables from the namespace
%reset
help(functioname)

References:
* https://pypi.org/project/noaa-sdk/
* https://www.weather.gov/documentation/services-web-api
* https://api.weather.gov/openapi.jsonhttps://api.weather.gov/openapi.json
* https://www.weather.gov/media/documentation/docs/NWS_Geolocation.pdf
* https://github.com/paulokuong/noaa
* MySQL Documentation (accessed May 18, 2022) https://dev.mysql.com/doc/
* MySQL Tutorial (accessed May 18, 2022) https://dev.mysql.com/doc/refman/8.0/en/tutorial.html
* sqlite3 documentation (accessed May 18, 2022) https://docs.python.org/3/library/sqlite3.html
* Python datetime module (accessed May 18, 2022) https://docs.python.org/3/library/datetime.html
* Pandas documentation (access May 18, 2022) https://pandas.pydata.org/docs/


"""
