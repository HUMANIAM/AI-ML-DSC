
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# In[173]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


# # Assignment 4 - Hypothesis Testing
# This assignment requires more individual learning than previous assignments - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# The following data files are available for this assignment:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
# 
# Each function in this assignment below is worth 10%, with the exception of ```run_ttest()```, which is worth 50%.

# ## Read data

# In[214]:


# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}


# In[215]:


# read cities houses
cities_homes = pd.read_csv('City_Zhvi_AllHomes.csv')
cities_homes.replace({"State": states}, inplace=True)

# read university towns
university_towns = pd.read_csv('university_towns.txt', sep="\n", names=["State"])

# read GDP of US
US_GDPs = pd.read_excel('gdplev.xls', skiprows =5, na_values=' ')
US_GDPs = US_GDPs.iloc[2:, [4, 6]]
US_GDPs.columns = ["Year", "GDP in Chained $"]
US_GDPs = US_GDPs[US_GDPs["Year"].str[:-2] >= "2000"]


# In[213]:


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    states_regions = [[]]
    state = None
    for un_town in university_towns['State']:
        st = ((un_town.split('[')[0]).split('(')[0]).strip()
        
        # if it's region name then append it to its state
        if un_town.find('[edit') == -1 and st is not None: 
            states_regions.append([state, st])
        else:
            state = st;
            
    df = pd.DataFrame(states_regions, columns = ['State', 'RegionName']).dropna()
    
    return df


# In[177]:


# set index for university towns
university_towns_ = get_list_of_university_towns()
university_towns_copy = university_towns_.set_index(['State', 'RegionName'])


# In[212]:


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    quarters = {0:'q1', 1:'q2', 2:'q3', 3:'q4'}
    b, i = 51, 51                                    # start from 2000 year
    df = cities_homes[['State', 'RegionName']].copy()
    cols_len = len(cities_homes.columns)
    
    # make add housing price in quarter format
    while i < cols_len:
        q = quarters[((i-b)/3)%4]
        year_q = str(2000 + int((i-b)/12)) + q
    
        # mean of current quarter
        df[year_q] = cities_homes.ix[:, i:i+3].mean(axis=1)
         
        i += 3
    
    df.set_index(['State', 'RegionName'], inplace=True)
    
    return df


# In[211]:


# convert US_GDPs from months format to quarters format
US_GDPs_Quarters = convert_housing_data_to_quarters()


# In[210]:


def get_recession():
    """recession starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    return start quarter and end quarter of the recession as (startq, endq)"""
    
    us_gdps = US_GDPs['GDP in Chained $']
    sz = len(us_gdps)
    
    for i in range(1, sz):
        j = i
        # sequence of decline
        while j < sz and us_gdps.iloc[j] < us_gdps.iloc[j-1] :
            j += 1
           
        # at least 2 consuctive growth
        if j < sz-1 and (j-i) > 1 and us_gdps.iloc[j+1] > us_gdps.iloc[j]:
            return (i, j+1)
        
    return None
    


# In[209]:


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    start_recesion_index = get_recession()[0]
    return US_GDPs.iloc[start_recesion_index]['Year'] 


# In[141]:


get_recession_start()


# In[208]:


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    end_recession_index = get_recession()[1]
    return US_GDPs.iloc[end_recession_index]['Year']


# In[164]:


get_recession_end()


# In[207]:


def get_recession_bottom():
    '''A recession bottom is the quarter within a recession which had the lowest GDP.
    Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    recession = get_recession()
    botttom_index = US_GDPs['GDP in Chained $'][recession[0]:recession[1]].idxmin()
    return US_GDPs['Year'][botttom_index]


# In[184]:


get_recession_bottom()


# In[206]:


def get_quarter_before_recession():
    quarter_before_recession = get_recession()[0] - 1
    return US_GDPs.iloc[quarter_before_recession]['Year']


# In[205]:


def get_recession_bottom_house_prices():
    # get bottom recesssion houses price
    return US_GDPs_Quarters[get_recession_bottom()]


# Hypothesis: University towns have their mean housing prices less effected by recessions.
#     Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before 
#     the recession starts compared to
#     the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

# In[204]:


def price_houses_ratio_before_recession():
    # get the houses price in the quarter before the start quarter of recession
    quarter_before_recess      = get_quarter_before_recession()
    price_houses_before_recess = US_GDPs_Quarters[quarter_before_recess]
    
    
    # get bottom recesssion houses price
    bottom_houses_prices = get_recession_bottom_house_prices()
    
    # price houses ratio
    price_houses_ratio_before_recess = price_houses_before_recess / bottom_houses_prices
    
    return price_houses_ratio_before_recess.rename('price_ratio')


# In[203]:


# prices ratio quarter before recession start and recession bottom
prices_ratio = price_houses_ratio_before_recession().to_frame()


# In[252]:


def get_univ_town_prices_ratio():
    """merge price_ratio with university towns to get price ratio"""
    return prices_ratio[prices_ratio.index.isin(university_towns_copy.index)].dropna().squeeze()
    


# In[253]:


def get_non_univ_town_price_ratio():
    # non university towns price ratio before the recession start
    return prices_ratio[prices_ratio.index.isin(university_towns_copy.index) == False].dropna().squeeze()


# In[254]:


print(len(prices_ratio))
print(len(prices_ratio[prices_ratio.index.isin(university_towns_copy.index) == False]))
print(len(prices_ratio[prices_ratio.index.isin(university_towns_copy.index)]))


# In[255]:


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    alpha = 0.01
    
    price_ratio_non_univ_towns = get_non_univ_town_price_ratio()
    price_ratio_univ_towns = get_univ_town_prices_ratio()
    t_test, pvalue = ttest_ind(price_ratio_non_univ_towns, price_ratio_univ_towns)

    different = True if pvalue < alpha else False
    better = "non-university town" if price_ratio_non_univ_towns.mean() < price_ratio_univ_towns.mean() else "university town"
    
    
    return (different, pvalue, better)


# In[256]:


run_ttest()
# get_univ_town_prices_ratio()

