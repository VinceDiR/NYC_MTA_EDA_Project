# 2021 MTA Traffic & 2020 Census Data Analysis - Interactive Map for Digital Signage Pilot Program
Nate DiRenzo
## Abstract
The goal of this project is to provide insights to our stakeholders-- Executives at Outfront Media and the MTA Construction and Development Department. Specifically, this analysis aims to provide stakeholders with reliable information about the most-trafficked stations during 2021, broken down by borough. In addition, I have provided insights into system-wide trends, and an interactive map combining the most salient traffic information with 2020 Census Demographic information. The goal is to provide stakeholders with a insights to help inform where they choose to deploy the pilot program for their new digital signage, and intelligently price adspace for partnrs with up-to-date traffic and demographic information. To accomplish this project, I pulled down a year's worth of turnstile data, cleaned it up, performed calcuations for relevant traffic information, created a number of visualizations, then connected this information with geographic data for NYC Subway Stations, and plotted that as well as an overlay of 2020 Neighborhood Tabulation Areas Demographic information using leafmap.
## Design
In thinking about my approach to this project I strove to reduce variance in the data as much as possible. I noticed that Recovery Audits were often fraught, and there were a number of turnstiles that counted in reverse, regularly had massive resets, or were clearly malfunctioning. In the interest of managing complexity, I calculated all of our most salient columns (net_traffic, audit_length, avg_traffic) before removing any data. Given I was working with a year's worth of data, I took a fairly draconic approach to cleaning the data. I got rid of all Recovery Audit observations, cast all net traffic values as positive, and reduced the entire dataset to only the observations which fell into the 99th percentile. Once properly organized, creating and plotting a number of dataframes using groupby() and aggregate functions was relatively straight forward.
## Data
I pulled all of the MTA Turnstile Data for 2021 [Here.](http://web.mta.info/developers/turnstile.html) The data was stored in a SQLite Database and pulled into pandas using the SQLAlchemy library. Once I finished my initial analysis of the turnstile data, I merged the aggregated station dataframe with geograppies of NYC subway stations found [here.](https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49) and plotted them as a layer along with 2019 Data from the American Community Survey found [here.](https://www1.nyc.gov/site/planning/planning-level/nyc-population/american-community-survey.page.page)
## Algorithms
1. Reversed Counters - I cast these as absolutes
2. Counter Resets - Solved with absolutes, biggest offenders taken out with Recovery Audits & percentile masking.
3. Nonsense Readings - Gotten rid of via percentile masking.
4. Ticker-style to incremental data - Dervied total traffic from single observation using groupby() and diff().
5. Converting to datetime - Swapped out text fields for datetime values. Powerful tool in pandas.
6. Filling in NA's - only NA's should be the start of a turnstile's observations for a given time period, so all of them were filled with 0.
7. Outliers - Removed via percentile masking.
8. Spatial plotting - Used Geopandas and leafmap to make static, interactive visualizations.
## Tools
- SQLite, SQLAlchemy for storage/querying.
- Python, Jupyter Notebook are the mediums through which we work with the data.
- Matplotlib, Seaborn, Pandas, Geopandas, leafmap - Plotting and visualization libraries
- FuzzyWuzzy, Voila!, pandas-profiling - miscellaneous
## Communication
I will present my findings via a 5 minute executive briefing featuring visualizations created in matplotlib, seaborn, geopandas, and leafmap. I will also render my notebook using Voila! so full functionality is accessible. Slides will be available as PDF in this reppository.
