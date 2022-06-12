#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Week 2 Assignment Activity
# 
# The objective if this assignment and this notebook is to get acquainted with the data by: 
# * Setting up the working files and folders. 
# * Determining the size and shape of the data sets. 
# * Loading the data into a DataFrame. 
# * Identifying whether there are any missing values. 
# * Determining the vaccination status in Gibraltar by identifying the number of people who:
#     1. Are vaccinated.
#     2. Have received the first dose. 
#     3. Have received the second dose.
# 
# --------

# In[1]:


# Import packages. 
import pandas as pd

# Load datasets and create the DataFrames.
covid_cases = pd.read_csv('covid_19_uk_cases.csv')
vaccinated = pd.read_csv('covid_19_uk_vaccinated.csv')
tweets = pd.read_csv('tweets.csv')


# ### 1. View and Examine the DataFrames
# For each DataFrame:
# * View the first and last five rows.
# * Determine the number of rows and columns.
# * Determine the data types in the DataFrames.
# * Determine the number of missing values.

# #### Vaccinated DataFrame - Review

# In[2]:


vaccinated.head()


# In[3]:


vaccinated.tail()


# In[4]:


vaccinated.shape


# In[5]:


vaccinated.dtypes


# In[6]:


vaccinated.isnull().sum()


# In[7]:


vaccinated.describe()


# #### Vaccinated DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Vaccinated DataFrame has 7584 rows and 11 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has no missing values. 

# #### Covid Cases DataFrame - Review

# In[8]:


covid_cases.head()


# In[9]:


covid_cases.tail()


# In[10]:


covid_cases.shape


# In[11]:


covid_cases.dtypes


# In[12]:


covid_cases.isnull().sum()


# #### Covid Cases DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Covid Cases DataFrame has 7584 rows and 12 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has 8 missing values: 2 in the deaths column, 2 in the cases column, 2 in the recovered column, and 2 in the hospitalised column. However, as determined below, the data belongs to 2 instances on 2020-09-21 and 2020-09-22 in Bermuda. 

# In[13]:


# Filtering ALL cases of missing data. 
nan_covid_cases = covid_cases[covid_cases.isna().any(axis=1)]
nan_covid_cases


# #### Tweets DataFrame - Review

# In[14]:


tweets.head()


# In[15]:


tweets.tail()


# In[16]:


tweets.shape


# In[17]:


tweets.dtypes


# In[18]:


tweets.isnull().sum()


# #### Tweets DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Tweets DataFrame has 3960 rows and 21 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has a lot missing values. All of the "in_reply_to..." and the "quoted_status_..." columns are missing all data. The "possibly_sensitive" column is missing 830 values. The other columns are missing none to 1.

# ### 2. Filter Covid Cases for Gibraltar
# 
# 1. Filter the data for the region Gibraltar as displayed in the covid_19_uk_cases.csv.
# 2. Print the Gibraltar DataFrame fully. 
# 3. Subset the Gibraltar DataFrame that you have created consisting of the following columns: Deaths, Cases, Recovered and Hospitalised.

# In[19]:


# Filter for Gibraltar. Print the DataFrame fully. 
gibraltar = covid_cases[covid_cases['Province/State'] == 'Gibraltar']
pd.set_option("display.max_rows", None)
gibraltar


# In[20]:


# Creating subset Gibraltar DataFrame with Deaths, Cases, Recovered, and Hospitalised. 
gibraltar_covid = gibraltar[['Deaths', 'Cases', 'Recovered', 'Hospitalised']]
gibraltar_covid


# ### 3. Discriptive Statistics on Gibraltar's Covid Cases

# In[21]:


gibraltar_covid.describe()


# --------

# ### 4. General Observations
# 
# 1. The Data doesn't have a specified index; rather a sequence number. 
# 
# 2. Out of a total 5727 cases in Gibraltar, 4907 were hospitalized, 4670 recovered, and 97 died. 
# 
# 3. The number of hospitalization in Gibraltar is extremely high relative to the number of total cases. 
# 
# 4. The DataFrame has 8 missing values: 2 in the deaths column, 2 in the cases column, 2 in the recovered column, and 2 in the hospitalised column. However, as determined below, the data belongs to 2 instances on 2020-09-21 and 2020-09-22 in Bermuda. The reason for the missing data is likely due to the Tropical Storm Teddy, which hit Bermuda on the 21st of September. Teddy's centre was located offshore approximately 310 km south-east of Bermuda main island, with maximum sustained wind of 165 km/h.
# 
# 5. More people have taken the first dose of vaccination than the second. 

# ---

# In[ ]:




