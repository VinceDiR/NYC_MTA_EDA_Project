# NYC_MTA_EDA_Project #
 
## By: Nate DiRenzo

The goal of this project is to perform exploratory data analysis on MTA turnstile data using SQL and Python, generate actionable, revenue-generating insights for a hypothetical business, and present that information in clear and concise manner using summary statistics and Python visualization libraries (pandas, matplotlib, seaborn, geopandas). As a further goal, I'd like to collate this information with geographic data on New York City's subway stations, and neighborhood tabulation area demographic information taken from the 2020 Census. Ultimately the combined data will provide our target audience with traffic, demographic, and geographic data that helps them better understand the populations moving through NYC's subway stations at a granular level.

### Question/need:

The plan is to analyze the MTA turnstile data for the calendar year 2021. The insights we're going to be pulling from this data will primarily be focused on identifying the volume of foot traffic (broken down into entries/exits) moving through a given subway station in NYC, on a given day, at a given time. By aligning this data with data pulled from the 2020 Census, and geo data for each subway station, I believe we can generate some compelling insights about the quantity and demographics of the foot traffic moving through each of NYC's subway stations during the calendar year 2021, as well as information such as most trafficked stations by borough, income levels, race, and ethnicity.

In terms of who would find these insights useful,the proposed target audience for this data is a digital signage business looking to launch a pilot program in NYC's subway stations. Currently, Outfront Media is making a billion dollar investment in digital signage in the NYC transit system. The strategy team at Outfront would be a good proposed audience for this project. 

Not only would the information help them understand where the highest volume of traffic is (and thus the best stations to install signage), but also the dates and times during which traffic is highest, and the prevailing demographics of a given station's neighborhood. This will help them understand where investments in new digital ad spaces would be most impactful, price adspace appropriately for their customers, and more effectively attract new clients with hard thorough information about ROI. The insights would surely have applications beyond the proposed use case, but for the purposed of keeping the scope of this first project manageable we will be focused only on the above mentioned.


#### Data Description:

We will be using MTA Turnstile data, taken from http://web.mta.info/developers/turnstile.html and organized into a SQLite Database locally. 

We will also be using geographic data found on the NYC Open Data website: https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49 to plot each subway station on a map. 

Finally, we will include census block and demographic data found on Kaggle: https://www.kaggle.com/zusmani/us-census-2020 to overlay demographic onformation on the map to give a complete view.

The observations found within each dataset are as follows: 

1. Each observation in the mta_turnstile data represents an audit event for a specific turnstile, at a specifc station, on a specific day, at a specific time. They contain unique, identifying data such as Control Area (C/A), Remote Unit (UNIT), and Subunit Channel Position (SCP) as well features containing station information, date & time, information, cumulative ticker-style entry and exit measurements, and subway lines accessible from a given station.

2. Each observation found in the Open Data Subway Station table contains information about a specific station, including name and geo coordinates to position locations on a map. This data should be easily joined with the turnstile data on the station/name columns.

3. Last, we'd like to connect the merged station and turnstile data with geographic and demographic information taken from the 2020 Census. We'd like to merge two different tables here, one with GEOJSON data for defining the Neighborhood Tabulation Areas (NTA's) on our map, and a further table to align demographic information for each NTA.

##### Tools:

This project will call for the use of a number of Python libraries, including sqlalchemy, pandas, matplotlib, geopandas, plotly. We plan to do some work with spatial tools such as geopandas that go beyond what is required in the project.

###### MVP Goal:

An MVP would be a clean turnstile dataset, including new calculated columns highlighting traffic data, aggregations by station, date, and time, and visualizations to provide insights about the most trafficked stations.

Step 2 in the iterative process will be merging in station location data and overlaying it on a map of Census NTA units.

The 'final' version will include demographic data from each NTA, formatting that data over the already-existing map we have created using shapefiles for 2020 Census NTA units, and MTA subway stations, and tying the data together so that station-level observations can be viewed alongside NTA demopgraphic information. 
