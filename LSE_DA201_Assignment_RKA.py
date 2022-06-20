#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Week 2 Assignment Activity
# 
# The objective of this assignment and this notebook is to get acquainted with the data by: 
# * Setting up the working files and folders. 
# * Determining the size and shape of the data sets. 
# * Loading the data into a DataFrame. 
# * Identifying whether there are any missing values. 
# * Determining the vaccination status in Gibraltar by identifying the number of people who:
#     1. Are vaccinated.
#     2. Have received the first dose. 
#     3. Have received the second dose.

# In[1]:


# Import packages. 
import pandas as pd, numpy as np

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


print(f" The vaccinated DataFrame has {vaccinated.shape[0]} rows, and {vaccinated.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{vaccinated.dtypes}")


# In[5]:


vaccinated.isnull().sum()


# In[6]:


vaccinated.describe()


# #### Vaccinated DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Vaccinated DataFrame has 7584 rows and 11 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has no missing values. 

# #### Covid Cases DataFrame - Review

# In[7]:


covid_cases.head()


# In[8]:


covid_cases.tail()


# In[9]:


print(f" The covid_cases DataFrame has {covid_cases.shape[0]} rows, and {covid_cases.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{covid_cases.dtypes}")


# In[10]:


covid_cases.isnull().sum()


# #### Covid Cases DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Covid Cases DataFrame has 7584 rows and 12 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has 8 missing values: 2 in the deaths column, 2 in the cases column, 2 in the recovered column, and 2 in the hospitalised column. However, as determined below, the data belongs to 2 instances on 2020-09-21 and 2020-09-22 in Bermuda. 

# In[11]:


# Filtering ALL cases of missing data. 
nan_covid_cases = covid_cases[covid_cases.isna().any(axis=1)]
nan_covid_cases


# #### Tweets DataFrame - Review

# In[12]:


tweets.head()


# In[13]:


tweets.tail()


# In[14]:


print(f" The tweets DataFrame has {tweets.shape[0]} rows, and {tweets.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{tweets.dtypes}")


# In[15]:


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

# In[16]:


# Filter for Gibraltar. Print the DataFrame fully. 
gibraltar = covid_cases[covid_cases['Province/State'] == 'Gibraltar']
pd.set_option("display.max_rows", None)
gibraltar


# In[17]:


# Creating subset Gibraltar DataFrame with Deaths, Cases, Recovered, and Hospitalised. 
gibraltar_covid = gibraltar[['Deaths', 'Cases', 'Recovered', 'Hospitalised']]
gibraltar_covid


# ### 3. Discriptive Statistics on Gibraltar's Covid Cases

# In[18]:


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

# ## Week 3 Assignment Activity
# 
# The objective of this assignment merge the covid_cases and vaccinated DataFrames in order to: 
# 1. Determine the number of cases across the UK.
# 2. Determine if there are differences over time between the first and second dose application.
# 3. Highlight any discoveries or insights.

# In[19]:


# Merge the covid_cases and vaccinated into a covid DataFrame. 
covid = covid_cases.merge(vaccinated, how='left')
covid


# In[20]:


# View the DataFrame. 
print(f" The covid DataFrame has {covid.shape[0]} rows, and {covid.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{covid.dtypes}")


# In[21]:


# Convert the data type of the Date column from object to DateTime.
covid['Date'] = pd.to_datetime(covid['Date'])

print(f" The Date column now is of type: {covid['Date'].dtypes}")


# In[22]:


# Drop unnecessary columns.
covid.drop(['Lat', 'Long', 'ISO 3166-1 Alpha 3-Codes', 'Intermediate Region Code'], axis = 1, inplace = True)

# Confirm remaining columns. 
print(f" The covid DataFrame now has the following columns and column types: \n{covid.dtypes}")


# ### 1. Determine the number of cases across the UK.

# In[23]:


# Assumes that daily cases being reported are NEW cases. 
covid.groupby('Country/Region')[['Cases']].sum()


# ### 2. Determine if there are differences over time between the first and second dose application.

# In[46]:


# Create a dose difference series and determine the sum. 
covid['Dose Difference'] = covid['Second Dose'] - covid['First Dose']
print(f"There are {covid['Dose Difference'].sum()} people who took the second dose compared to the first does in the UK")


# In[50]:


# Inspect vaccination per Province/State. 
covid.groupby('Province/State')[['Vaccinated', 'First Dose', 'Second Dose', 'Dose Difference']].sum() .sort_values("Dose Difference", ascending=True)


# ### 3. General Observations
# 
# 1. The total number of cases across the United Kingdom is 1.627917e+09. 
# 2. Vaccine update reduced between the first and the second vaccine doses with 2,118,019 less people taking the second dose. 
# 3. Gibraltar had the highest number of individuals who received the first dose but not the second; 264,745 less people received the second dose. 
# 4. The general trend in vaccination starts slow with first doses; speeds up with some second doses (a few compared to the first doses). However, as expected, first doses start to reduce while second doses pick up drastically. 
# 5. All in all though, over time, the amount of vaccinations seem to slow down towards the end of the data set with the second doses. This could be a result of the data sample stopping before people receive their second dose. 
# 
# 

# In[ ]:




