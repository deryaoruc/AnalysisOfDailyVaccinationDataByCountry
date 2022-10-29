CREATE TEMP TABLE grouppedMedian AS 
SELECT country, date, 
COALESCE(MEDIAN(daily_vaccinations),0) AS daily_vaccinations_median, 
vaccines
FROM country_vaccination_stats c
GROUP by country

CREATE TEMP TABLE merged AS 
SELECT c.country, c.date, c.daily_vaccinations, 
c.vaccines, g.country,g.daily_vaccinations_median
FROM country_vaccination_stats c
INNER JOIN grouppedMedian g ON c.country=g.country

CREATE TABLE new_country_vaccination_stats AS 
SELECT country,date,
COALESCE(daily_vaccinations,daily_vaccinations_median) AS daily_vaccinations,
vaccines
FROM merged