
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.0** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # The Series Data Structure

# In[67]:


import pandas as pd
get_ipython().magic('pinfo pd.Series')


# In[3]:


animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)


# In[4]:


numbers = [1, 2, 3]
pd.Series(numbers)


# In[5]:


animals = ['Tiger', 'Bear', None]
pd.Series(animals)


# In[6]:


numbers = [1, 2, None]
pd.Series(numbers)


# In[7]:


import numpy as np
np.nan == None


# In[8]:


np.nan == np.nan


# In[9]:


np.isnan(np.nan)


# In[10]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[11]:


s.index


# In[12]:


s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s


# In[13]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s


# # Querying a Series

# In[38]:


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s


# In[15]:


s.iloc[3]


# In[16]:


s.loc['Golf']


# In[39]:


s[3]
# you deal with the dictionary as you deal with arrays in standard python but that doesn't always works


# In[19]:


s['Golf']


# In[22]:


sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)


# In[26]:


s[0] #This won't call s.iloc[0] as one might expect, it generates an error instead


# In[40]:


s = pd.Series([100.00, 120.00, 101.00, 3.00])
s


# In[41]:


total = 0
for item in s:
    total+=item
print(total)


# In[42]:


import numpy as np

total = np.sum(s)
print(total)


# In[43]:


#this creates a big series of random numbers
s = pd.Series(np.random.randint(0,1000,10000))
s.head()


# In[44]:


len(s)


# In[52]:


# compare time take by for loop to sum and np.sum 


# In[45]:


# execute the next segment of code 100 times to show the average execution time
%%timeit -n 100
summary = 0
for item in s:
    summary+=item


# In[46]:



get_ipython().run_cell_magic('timeit', '-n 100', 'summary = np.sum(s)')


# In[53]:


s+=2 #adds two to each item in s using broadcasting
s.head()


# In[55]:


for label, value in s.iteritems():
    s.set_value(label, value+2)
s.head()

# amazing all above code can be written by s += 2


# In[ ]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\nfor label, value in s.iteritems():\n    s.loc[label]= value+2')


# In[69]:


get_ipython().run_cell_magic('timeit', '-n 10', 's = pd.Series(np.random.randint(0,1000,10000))\ns+=2')


# In[70]:


s = pd.Series([1, 2, 3])
s.loc['Animal'] = 'Bears'
s


# In[71]:


original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)


# In[72]:


original_sports


# In[73]:


cricket_loving_countries


# In[74]:


all_countries


# In[75]:


all_countries.loc['Cricket']


# # The DataFrame Data Structure

# In[1]:


import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()


# In[8]:


df.loc['Store 2']


# In[9]:


type(df.loc['Store 2'])


# In[10]:


df.loc['Store 1']


# In[11]:


df.loc['Store 1', 'Cost']


# In[12]:


df.T


# In[13]:


df.T.loc['Cost']


# In[14]:


df['Cost']


# In[15]:


df.loc['Store 1']['Cost']


# In[16]:


df.loc[:,['Name', 'Cost']]


# In[17]:


df.drop('Store 1')


# In[18]:


df


# In[19]:


copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
copy_df


# In[20]:


get_ipython().magic('pinfo copy_df.drop')


# In[21]:


del copy_df['Name']
copy_df


# In[25]:


df['Location'] = None
df


# # Dataframe Indexing and Loading

# In[34]:


costs = df['Cost']
costs


# In[35]:


costs+=2
costs


# In[36]:


df


# In[ ]:


get_ipython().system('cat olympics.csv')


# In[57]:


df = pd.read_csv('olympics.csv')
df.head()


# In[58]:


df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1)
df.head()


# In[59]:


cols = df.columns


# In[60]:


for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()


# # Querying a DataFrame

# In[45]:


df['Gold'] > 0


# In[46]:


only_gold = df.where(df['Gold'] > 0)
only_gold.head()


# In[47]:


only_gold['Gold'].count()


# In[48]:


df['Gold'].count()


# In[49]:


only_gold = only_gold.dropna()
only_gold.head()


# In[50]:


only_gold = df[df['Gold'] > 0]
only_gold.head()


# In[51]:


len(df[(df['Gold'] > 0) | (df['Gold.1'] > 0)])


# In[52]:


df[(df['Gold.1'] > 0) & (df['Gold'] == 0)]


# # Indexing Dataframes

# In[61]:


df.head()


# In[62]:


df['country'] = df.index
df = df.set_index('Gold')
df.head()


# In[63]:


df = df.reset_index()
df.head()


# In[64]:


df = pd.read_csv('census.csv')
df.head()


# In[65]:


df['SUMLEV'].unique()


# In[66]:


df=df[df['SUMLEV'] == 50]
df.head()


# In[67]:


columns_to_keep = ['STNAME',
                   'CTYNAME',
                   'BIRTHS2010',
                   'BIRTHS2011',
                   'BIRTHS2012',
                   'BIRTHS2013',
                   'BIRTHS2014',
                   'BIRTHS2015',
                   'POPESTIMATE2010',
                   'POPESTIMATE2011',
                   'POPESTIMATE2012',
                   'POPESTIMATE2013',
                   'POPESTIMATE2014',
                   'POPESTIMATE2015']
df = df[columns_to_keep]
df.head()


# In[68]:


df = df.set_index(['STNAME', 'CTYNAME'])
df.head()


# In[69]:


df.loc['Michigan', 'Washtenaw County']


# In[76]:


df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]


# # Missing values

# In[86]:


df = pd.read_csv('log.csv')
df


# In[78]:


get_ipython().magic('pinfo df.fillna')


# In[87]:


df = df.set_index('time')
df = df.sort_index()
df.head()


# In[88]:


df = df.reset_index()
df = df.set_index(['time', 'user'])
df.head()


# In[89]:


df = df.fillna(method='ffill')
df.head()

