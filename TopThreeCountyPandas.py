# Complementing missing data with minimum number of vaccines per country

import pandas as pd

df = pd.read_csv("country_vaccination_stats.csv")

dfGroup = df.groupby("country")
dfGroupMin = dfGroup.min().reset_index()
dfGroupMinFull = dfGroupMin.fillna(0)

df = df.fillna(dfGroupMinFull)
print(df)


# Top 3 countries with the highest median daily vaccination numbers

groupped = df.groupby("country")
grouppedMedian = groupped.median().reset_index()
grouppedMedianTopThree = grouppedMedian.head(3)
print(grouppedMedian)
