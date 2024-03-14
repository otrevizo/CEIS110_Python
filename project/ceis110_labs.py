# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 07:43:46 2021

@author: trevizo

Adapted code from CEIS110, Prof. G. Cooper

Updated July 11, 2023
- Module 2 changed. Now Module 2 asks student to write a simple program.
- Piror version had Module 2 install noaa-spk
- New version has installation of noaa-spk within Module 3
"""

# %% Libraries
# in CEIS week 3
from noaa_sdk import noaa
import sqlite3
import datetime
# in CEIS week 4
# import sqlite3
import pandas as pd
# in CEIS week 6
import matplotlib.pyplot as plt


# %% Functions


def convertCtoF(tempC):
    """ convertCtoF(tempC) converts degrees Celcius to Farenheit """
    return (tempC * 9.0 / 5.0) + 32.0


# %% Module 1 - Anaconda
'''
Install Anaconda
'''


# %% Module 2 - Simple program
'''
Prerequisites:
1. Open the Anaconda >> Spyder.

2. Write a simple program

'''

name = input('What is your name: ')
city = input('What city do you live in: ')
temperature = float(input('What is the temperature: '))
if temperature > 60:
    print('Hello ', name, ', it is nice where your live.')
else:
    print('Hello ', name, ', it is cold where your live.')

# %% Module 3 - NOAA API and build DB
'''
NOA API prerequisites:
See https://pypi.org/project/noaa-sdk/ for details on noaa_sdk package used
1. Open a terminal window
    a) Windows. Open the Anaconda >> Prompt command window.
    b) Macs. Open Launchpad, then click the terminal icon.
    c) Linux, Open a terminal window.

2. At the prompt, enter the following command:
    pip install noaa-sdk
   
3. The last line of the output says
    “Successfully installed noaa-sdk” you are good!

4. Before closing the window, capture this result in a screenshot.

'''

# %%% Build DB

# Purpose: Build weather database from NOAA data
# Name: Your name
# Date: the date
# See https://pypi.org/project/noaa-sdk/ for details on noaa_sdk package used

# Needs
# from noaa_sdk import noaa
# import sqlite3
# import datetime

print("CEIS110 Week 3")

# parameters for retrieving NOAA weather data
zipCode = "60610"  # change to your postal code
country = "US"

# date-time format is yyyy-mm-ddThh:mm:ssZ, times are Zulu time (GMT)

# gets the most recent 14 days of data
today = datetime.datetime.now()
past = today - datetime.timedelta(days=14)
startDate = past.strftime("%Y-%m-%dT00:00:00Z")
endDate = today.strftime("%Y-%m-%dT23:59:59Z")

# create connection - this creates database if not exist
print("Preparing database...")
dbFile = "weather.db"
conn = sqlite3.connect(dbFile)
# create cursor to execute SQL commands
cur = conn.cursor()

# drop previous version of table if any so we start fresh each time
dropTableCmd = "DROP TABLE IF EXISTS observations;"
cur.execute(dropTableCmd)

# create new table to store observations
createTableCmd = """ CREATE TABLE IF NOT EXISTS observations (
                        timestamp TEXT NOT NULL PRIMARY KEY,
                        windSpeed REAL,
                        temperature REAL,
                        relativeHumidity REAL,
                        windDirection INTEGER,
                        barometricPressure INTEGER,
                        visibility INTEGER,
                        textDescription TEXT
                     ) ; """
cur.execute(createTableCmd)
print("Database prepared")

# get hourly weather observations from NOAA Weather Service API
print("Getting weather data...")
n = noaa.NOAA()
observations = n.get_observations(zipCode, country, startDate, endDate)

# populate table with weather observations
print("Inserting rows...")

# The following variable is required by the database
insertCmd = """ INSERT INTO observations
(timestamp, windSpeed, temperature, relativeHumidity, windDirection,
barometricPressure, visibility, textDescription)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

count = 0
for obs in observations:
    insertValues = (obs["timestamp"],
                    obs["windSpeed"]["value"],
                    obs["temperature"]["value"],
                    obs["relativeHumidity"]["value"],
                    obs["windDirection"]["value"],
                    obs["barometricPressure"]["value"],
                    obs["visibility"]["value"],
                    obs["textDescription"])
    cur.execute(insertCmd, insertValues)
    count += 1

if count > 0:
    cur.execute("COMMIT;")

print(count, "rows inserted")
print("Database load complete!")

# %% Module 4 Part 1 - DB Reads

# Purpose: Query database using SQL
# Name: Your name
# Date: Your date
# Run BuildWeatherDB.py to build weather database before running this program

# Needs:
# import sqlite3
# import pandas as pd

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

# %% Module 5 - Lists - Part 1

# Purpose: Extract temp, humidity data from weather database into CSV file
# Run BuildWeatherDB.py to build weather database before running this program

# import sqlite3

# convert Celsius temperature to Fahrenheit
# def convertCtoF(tempC):
#     return (tempC*9.0/5.0) + 32.0

# file names for database and output file
dbFile = "weather.db"
output_file_name = 'formatdata.csv'

# connect to and query weather database and
dbFile = "weather.db"
conn = sqlite3.connect(dbFile)
# create cursor to execute SQL commands
cur = conn.cursor()
selectCmd = """ SELECT temperature, relativeHumidity FROM observations
                ORDER BY timestamp; """
cur.execute(selectCmd)
allRows = cur.fetchall()

# limit the number of rows output to half
rowCount = len(allRows) // 2         # double slash does integer division
rows = allRows[:rowCount]

# write data to output file
with open(output_file_name, "w+") as outf:
    outf.write('Celsius,Fahrenheit,Humidity')
    outf.write('\n')
    for row in rows:
        tempC = row[0]
        if tempC is None:       # handle missing temperature value
            outf.write(',,')
        else:
            tempF = convertCtoF(tempC)
            outf.write(str(tempC) + ',')
            outf.write(str(tempF) + ',')
        humidity = row[1]
        if humidity is None:    # handle missing humidity value
            outf.write('\n')
        else:
            outf.write(str(humidity) + '\n')
            # print data to file separated by commas

# %% Module 5 - Lists Part 2

# Purpose: Extract temp, humidity data from weather database into CSV file
# Run BuildWeatherDB.py to build weather database before running this program

# import sqlite3

# convert Celsius temperature to Fahrenheit
# def convertCtoF(tempC):
#     return (tempC*9.0/5.0) + 32.0

# file names for database and output file
dbFile = "weather.db"
output_file_name = 'formatdata2.csv'    # add 2 to file name for 2nd data set

# connect to and query weather database and
dbFile = "weather.db"
conn = sqlite3.connect(dbFile)
# create cursor to execute SQL commands
cur = conn.cursor()
selectCmd = """ SELECT temperature, relativeHumidity FROM observations
                ORDER BY timestamp; """
cur.execute(selectCmd)
allRows = cur.fetchall()
# limit the number of rows output to half
rowCount = len(allRows) // 2    # double slash does integer division
rows = allRows[rowCount:]
# use [rowCount:] instead of [:rowCount] for 2nd data set

# write data to output file
with open(output_file_name, "w+") as outf:
    outf.write('Celsius,Fahrenheit,Humidity')
    outf.write('\n')
    for row in rows:
        tempC = row[0]
        if tempC is None:       # handle missing temperature value
            outf.write(',,')
        else:
            tempF = convertCtoF(tempC)
            outf.write(str(tempC) + ',')
            outf.write(str(tempF) + ',')
        humidity = row[1]
        if humidity is None:       # handle missing humidity value
            outf.write('\n')
        else:
            outf.write(str(humidity) + '\n')
            # print data to file separated by commas

# %% Module 6 - Plots

# data frames to plot
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")

# %%% Boxplot
# Box plot code
# Purpose: Create box plot for period 2 data

# import pandas as pd
# import matplotlib.pyplot as plt

df2.boxplot()
plt.suptitle('Period 2 box plot')
plt.show()

# %%% Line chart
# Compare periods plot
# Purpose: Create Celsius plot comparing period 1 and period 2
# data frame 1 and data frame 2 have an attrubute named 'Celcius'

plt.figure()
df1.Celsius.plot(label='period')
df2.Celsius.plot(label='period 2')
plt.legend(loc='best')
plt.suptitle('Celsius')
plt.show()

# %%% Histogram
# Histogram
# Purpose: Create a histogram of humidity data from the second period

df2['Humidity'].hist(bins=10, alpha=0.5)
plt.suptitle('Histogram of Humidity')
plt.show()

# %%% Scatter chart
# Purpose: Create scatter plot of humidity for period 1.
# Can replace df1 to df2 to display second period data

plt.scatter(df1.index.values, df1['Humidity'])
plt.suptitle('Humidity')
plt.show()


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
