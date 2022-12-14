# Complementing missing data with minimum number of vaccines per country

import pandas as pd

df = pd.read_csv("country_vaccination_stats.csv")

dfGroup = df.groupby("country")
dfGroupMin = dfGroup.min().reset_index()
dfGroupMinFull = dfGroupMin.fillna(0)

df = df.fillna(dfGroupMinFull)
print(df)


# Number of total vaccinations done on 1/6/2021 (MM/DD/YYYY)

x = df.groupby("date").sum().reset_index()
xSorted = x.sort_values('date',ascending=True)
print(x)