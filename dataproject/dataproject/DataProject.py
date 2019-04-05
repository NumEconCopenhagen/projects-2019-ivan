#%%
# Importing packages

import pandas as pd
import numpy as np

import pandas_datareader
import datetime

from pandas_datareader import wb

# Remember to pip install wbdata pip install pandas-datareader

#%%
# Cleaning data: choosing data, indicators

countries = ["WLD", "EGY", "PRT", "ARG", "SWE", "SEN", "JPN", "FRA"]

indicators = {"NY.GDP.PCAP.KD":"GDP per capita", "SP.DYN.TFRT.IN":"Fertility Rate",  
              "SP.DYN.LE00.IN":"Life expectancy at birth", "SP.DYN.IMRT.IN":"Mortality rate, infant"}

#%%
# As we are interested in how the economic growth through the years(1970-2016) have affected the livingstandards for the chosen countries, 
# we have chosen these indicators: GDP per Capita, Fertility Rate, Life expectancy at birth and Mortality rate, Infant. 

data_wb = wb.download(indicator= indicators, country= countries, start=1960, end=2016)
data_wb = data_wb.rename(columns = {"NY.GDP.PCAP.KD":"gdp_capita", "SP.DYN.TFRT.IN":"fert",  
                                    "SP.DYN.LE00.IN":"expec", "SP.DYN.IMRT.IN":"mort"})
data_wb = data_wb.reset_index()
round(data_wb.head(-1), 2)

#%%
# Cleaning data: clearing missing data.

print(f"Original: {data_wb.shape[0]} observations, {data_wb.shape[1]} variables")
del data_wb["mort"]
print(f"Cleared: {data_wb.shape[0]} observations, {data_wb.shape[1]} variables")


#%%
# Plotting: Useful packages for this project

import matplotlib.pyplot as plt
%matplotlib inline 
from ipywidgets import interact, interactive, fixed, interact_manual 
import ipywidgets as widgets


#%%
# Defining data
country=data_wb["country"]
year=data_wb["year"]
gdp_capita=data_wb["gdp_capita"]
fert = data_wb["fert"]
expec = data_wb["expec"]


#%%
# Figure 1: Plotting fertility rate for all the chosen countries

fert_dev = data_wb[data_wb["country"].isin(['Argentina', 'Senegal', 'Japan', 'France', 'World', "Sweden",
                                              "Egypt, Arab rep.", "Portugal"])]

def plot(fig):
    
    fig_fert_dev = fig.set_index('year')
    fig_fert_dev.groupby(['country'])['fert'].plot(legend=True);


fig = plt.figure(dpi=100)
plt.xticks(np.arange(0, 56, 10))
plt.gca().invert_xaxis()
plot(fert_dev)

#%%
# Here we can see that overall the fertility rate has decreased in the time period (1960-2016), but it is clear that for the 
# more developed countries have a lower fertility rate. 
# We can see that Senegal has a fertility rate that approx 3.6 higher than Portugal.


#%%
# Interactive figure 2: GDP per capita and the fertility rate (1960-2016)
def interactive_figure(country, data_wb):
    
    data_country = data_wb[data_wb.country == country]
    year = data_country.year
    gdp_capita = data_country.gdp_capita
    fert = data_country.fert
    
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(year, gdp_capita, 'b')
    ax1.set_ylabel("GDP per Capita", color='b')
    
    ax2 = ax1.twinx()
    ax2.plot(year, fert, 'r')
    ax2.set_ylabel("Fertility rate", color='r')
    
    plt.xticks(np.arange(0, 56, 10))
    plt.gca().invert_xaxis()

#%%
# Showing the interactive figure 2
widgets.interact(interactive_figure,
    year = widgets.fixed(year),
    data_wb = widgets.fixed(data_wb),
    country=widgets.Dropdown(description="Country", options=data_wb.country.unique()),
    gdp_capita=widgets.fixed(gdp_capita), fert = widgets.fixed(fert)
    
);

#%%
# Interactive figure 3: GDP per capita and the life expectancy at birth (1960-2016)
def interactive_figure(country, data_wb):
    
    data_country = data_wb[data_wb.country == country]
    year = data_country.year
    gdp_capita = data_country.gdp_capita
    expec = data_country.expec
    
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(year, gdp_capita, 'b')
    ax1.set_ylabel("GDP per Capita", color='b')
    
    ax2 = ax1.twinx()
    ax2.plot(year, expec, 'g')
    ax2.set_ylabel("Life expectancy at birth", color='g')
    
    plt.xticks(np.arange(0, 56, 10))
    plt.gca().invert_xaxis()

#%%
# Showing the interactive figure 3
widgets.interact(interactive_figure,
    year = widgets.fixed(year),
    data_wb = widgets.fixed(data_wb),
    country=widgets.Dropdown(description="Country", options=data_wb.country.unique()),
    gdp_capita=widgets.fixed(gdp_capita), expec = widgets.fixed(expec)
    
);

#%%
# Here we can see that there is a positive correlation between the development of the life expectancy
# at birth and GDP per Capita in the time period (1960-1970). 
# Although for Senegal there is an interesting development as life expectancy at birht rises over the
# whole period while GDP per capita is falling from 1960-1995.

#%%
#Conclusion 

# From the data presented in this analysis, we found tell that there seem to be a negative correlation 
# between how wealthy a country is and the population growth as expected. As this was a short analysis, 
# and the main objective was to present the data in a nice and easy way, there is a lot of aspects, there 
# remain to be uncovered and a further analysis should include more data on economic growth and perhaps an 
# econometric approach.
