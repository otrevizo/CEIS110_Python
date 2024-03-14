# -*- coding: utf-8 -*-
"""

CEIS110 Module 6 - Plots
"""

# %% Libraries
import pandas as pd
import matplotlib.pyplot as plt

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
* Pandas documentation (access May 18, 2022) https://pandas.pydata.org/docs/


"""
