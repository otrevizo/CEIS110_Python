# -*- coding: utf-8 -*-
"""
CEIS110 Module 3  - NOAA API and build DB

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

"""

# %% Load the libraries

from noaa_sdk import noaa
import sqlite3
import datetime


# %% Build DB

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

# %% Create a new table to store observations
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

# %% Get hourly weather observations from NOAA Weather Service API
print("Getting weather data...")
n = noaa.NOAA()
observations = n.get_observations(zipCode, country, startDate, endDate)

# %% Populate table with weather observations
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


"""
