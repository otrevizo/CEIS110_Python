# -*- coding: utf-8 -*-
"""

CEIS110 Module 5

# Purpose: Extract temp, humidity data from weather database into CSV file
# Run ceis110_module3.py to build weather database before running this program

# import sqlite3


"""

# %% Libraries
import sqlite3

# %% Functions
# convert Celsius temperature to Fahrenheit
def convertCtoF(tempC):
    return (tempC*9.0/5.0) + 32.0

# %% Module 5 - Lists - Part 1

# Purpose: Extract temp, humidity data from weather database into CSV file
# convert Celsius temperature to Fahrenheit

# file names for database and output file
dbFile = "weather.db"
output_file_name = 'formatdata.csv'

# connect to and query weather database and
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
            # outf.write(',,')
            continue
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
