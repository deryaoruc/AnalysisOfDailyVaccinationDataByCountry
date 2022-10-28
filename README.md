## Analysis of Daily Vaccination Data by Country With Pandas and SQL

#### Using pandas and sqlite, some modifications and analyzes were made on the table given about the daily vaccinations of the countries as of date.

+ Complementing Missing data With Pandas: 
  + The data were grouped into the minimum number of vaccinations by country, and the countries without daily vaccination data were given a value of 0.
  + With the minimum number of vaccinations found, missing data in the main table are completed by country
+ Top Three Country With Pandas
  + The top 3 countries with the highest median daily vaccination numbers are listed, taking into account the version of the dataset attributed to the missing values.
+ Total Vaccinations Number With Pandas
  + Considering the version of the data set attributed to missing values, the total number of vaccinations performed on 1/6/2021 (MM/DD/YYYY) was found.
+ Complementing Missing Data With SQLite
  + The data were grouped according to the median of the number of vaccinations by country, and the countries without daily vaccination data were given a value of 0.
  + Filling in missing data with the median of daily vaccinations by country