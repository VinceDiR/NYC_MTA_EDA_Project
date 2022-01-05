# NYC_MTA_EDA_Project
 
The goal of this project is to perform exploratory data analysis on MTA turnstile data using SQL and Python, generate actionable, revenue-generating insights for a hypothetical business, and present that information in clear and concise manner using Python visualization libraries (pandas, matplotlib, seaborn). As a further goal, I'd like to collate this information with geographic data on New York City's subway stations, and neighborhood demographic information broken down by NYC neighborhood. Ultimately the combined data will provide our target audience with traffic, demographic, and geographic data that helps them better understand where and when would be the best subway stations to reach what demographics.

Question/need:

The plan is to analyze the MTA turnstile data for the calendar year 2021. The insights we're going to be pulling from this data will primarily be focused on identifying the volume of foot traffic (broken down into entries/exits) moving through a given subway station in NYC, on a given day, at a given time. By aligning this data with data pulled from the 2020 Census, and geo data for each subway station, I believe we can generate some compelling insights about the quantity and demographics of the foot traffic moving through each of NYC's subway stations during the calendar year 2021.

In terms of who would find these insights useful,the proposed target audience for this data is a digital signage business looking to launch a pilot program in NYC's subway stations. Not only would the information help them understand where the highest volume of traffic is (and thus the best stations to install signage), but also the dates and times during which traffic is highest, and the prevailing demographics of a given station's neighborhood. This will help them price adspace appropriately for their customers. The insights would surely have applications beyond the proposed use case, but for the purposed of keeping the scope of this first project manageable we will be focused on the above mentioned use case.


Data Description:

We will be using MTA Turnstile data, taken from http://web.mta.info/developers/turnstile.html and organized into a SQLite Database locally. We will also be using geographic data found on the NYC Open Data website: https://data.cityofnewyork.us/Transportation/Subway-Stations/arq3-7z49 to plot each subway station on a map. Finally, we will include census block and demographic data found on Kaggle: https://www.kaggle.com/zusmani/us-census-2020 to overlay demographic onformation on the map to give a complete view.

What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?

Turnstile Data 
If modeling, what will you predict as your target?
Tools:
How do you intend to meet the tools requirement of the project?
Are you planning in advance to need or use additional tools beyond those required?
MVP Goal:
What would a minimum viable product (MVP) look like for this project?
