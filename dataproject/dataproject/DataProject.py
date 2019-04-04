#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'dataproject\dataproject'))
	print(os.getcwd())
except:
	pass

#%%
#Importing packages

import pandas as pd
import numpy as np

import pandas_datareader
import datetime

from pandas_datareader import wb

# Remember to install pip wbdata pip pandas

#%%
#Cleaning data

countries = ["WLD", "EGY", "PRT", "ARG", "ISL", "SWE", "SEN", "JPN", "FRA"]


#%%
indicators = {"NY.GDP.PCAP.KD":"GDP per capita", "NY.GDP.MKTP.CD":"GDP(current US $)", "SP.DYN.TFRT.IN":"Fertility Rate" }


#%%
data_wb = wb.download(indicator= indicators, country= countries, start=1960, end=2016)
data_wb = data_wb.rename(columns = {"NY.GDP.PCAP.KD":"gdp_capita","NY.GDP.MKTP.CD":"gdp", 
                                    "SP.DYN.TFRT.IN":"fert"})
data_wb = data_wb.reset_index()
data_wb.head(-10)


#%%
# plot
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from ipywidgets import interact, interactive, fixed, interact_manual 
import ipywidgets as widgets


#%%
country=data_wb["country"]
year=data_wb["year"]
gdp_capita=data_wb["gdp_capita"]
fert = data_wb["fert"]


#%%
def interactive_figure(country, data_wb):
    """define an interactive figure that uses countries and the dataframe as inputs """
    
    data_country = data_wb[data_wb.country == country]
    year = data_country.year
    gdp_capita = data_country.gdp_capita
    
    fig = plt.figure(dpi=100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(year, gdp_capita, 'b')
    ax1.set_ylabel("GDP per Capita", color='b')
    
    ax2 = ax1.twinx()
    ax2.plot(year, fert, 'r')
    ax2.set_ylabel("Fertility rate", color='r')
    
    
    plt.xticks(np.arange(10, 56, 10))
    plt.xticks(rotation=90)
    fig.tight_layout()
    plt.gca().invert_xaxis()


#%%
widgets.interact(interactive_figure,
    year = widgets.fixed(year),
    data_wb = widgets.fixed(data_wb),
    country=widgets.Dropdown(description="Country", options=data_wb.country.unique()),
    gdp_capita=widgets.fixed(gdp_capita), fert = widgets.fixed(fert)
    
);


#%%



