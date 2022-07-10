#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # DA201: Data Analytics using Python

# ## Week 1: Prepare Workstation
# ---

# In[105]:


# Import Matplotlib, Seaborn, NumPy, and Pandas.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import datetime

# Set chart attributes. 
sns.set(rc = {'figure.figsize':(15,10)})

# Load datasets and create the DataFrames.
covid_cases = pd.read_csv('covid_19_uk_cases.csv')
vaccinated = pd.read_csv('covid_19_uk_vaccinated.csv')
tweets = pd.read_csv('tweets.csv')


# ### Github Repo
# 
# - [My Github Repo](https://github.com/rabuhassan/lse_da_covid_analysis.git)
# - Screenshot demo
# 
# !['My Github screenshot](https://github.com/rabuhassan/lse_da_covid_analysis/blob/main/GithubScreenshot.png?raw=true)
# 
# 
# ---
# ---
# 

# ## Week 2: Assignment Activity
# ----
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

# ### 1. Viewing and Examining the DataFrames
# * Review
# * Observations

# #### Vaccinated DataFrame - Review

# In[63]:


vaccinated.head()


# In[64]:


vaccinated.tail()


# In[65]:


print(f" The vaccinated DataFrame has {vaccinated.shape[0]} rows, and {vaccinated.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{vaccinated.dtypes}")


# In[66]:


vaccinated.isnull().sum()


# In[67]:


vaccinated.describe()


# #### Vaccinated DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Vaccinated DataFrame has 7584 rows and 11 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has no missing values. 

# #### Covid Cases DataFrame - Review

# In[68]:


covid_cases.head()


# In[69]:


covid_cases.tail()


# In[70]:


print(f" The covid_cases DataFrame has {covid_cases.shape[0]} rows, and {covid_cases.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{covid_cases.dtypes}")


# In[71]:


covid_cases.isnull().sum()


# #### Covid Cases DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Covid Cases DataFrame has 7584 rows and 12 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has 8 missing values: 2 in the deaths column, 2 in the cases column, 2 in the recovered column, and 2 in the hospitalised column. However, as determined below, the data belongs to 2 instances on 2020-09-21 and 2020-09-22 in Bermuda. 

# In[72]:


# Filtering ALL cases of missing data. 
nan_covid_cases = covid_cases[covid_cases.isna().any(axis=1)]
nan_covid_cases


# #### Tweets DataFrame - Review

# In[73]:


tweets.head()


# In[74]:


tweets.tail()


# In[75]:


print(f" The tweets DataFrame has {tweets.shape[0]} rows, and {tweets.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{tweets.dtypes}")


# In[76]:


tweets.isnull().sum()


# #### Tweets DataFrame - Observations
# 
# 1. First 5 and last 5 rows observed. 
# 2. The Tweets DataFrame has 3960 rows and 21 columns. 
# 3. Data types: object, float, and int. 
# 4. The DataFrame has a lot missing values. All of the "in_reply_to..." and the "quoted_status_..." columns are missing all data. The "possibly_sensitive" column is missing 830 values. The other columns are missing none to 1.

# ### 2. Focus on Gibraltar
# 
# 1. Filter the data for the region Gibraltar as displayed in the covid_19_uk_cases.csv.
# 2. Print the Gibraltar DataFrame fully. 
# 3. Subset the Gibraltar DataFrame that you have created consisting of the following columns: Deaths, Cases, Recovered and Hospitalised.

# In[77]:


# Filter for Gibraltar. Print the DataFrame fully. 
gibraltar = covid_cases[covid_cases['Province/State'] == 'Gibraltar']
pd.set_option("display.max_rows", None)
gibraltar


# In[78]:


# Creating subset Gibraltar DataFrame with Deaths, Cases, Recovered, and Hospitalised. 
gibraltar_covid = gibraltar[['Deaths', 'Cases', 'Recovered', 'Hospitalised']]
gibraltar_covid


# #### Discriptive Statistics on Gibraltar's Covid Cases

# In[79]:


gibraltar_covid.describe()


# ### 3. General Observations
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
# 
# ---
# ---
# 

# ## Week 3: Assignment Activity
# -----
# 
# The objective of this assignment merge the covid_cases and vaccinated DataFrames in order to: 
# 1. Determine the number of cases across the UK.
# 2. Determine if there are differences over time between the first and second dose application.
# 3. Highlight any discoveries or insights.

# In[80]:


# Merge the covid_cases and vaccinated into a covid DataFrame. 
covid = covid_cases.merge(vaccinated, how='left')
covid


# In[81]:


# View the DataFrame. 
print(f" The covid DataFrame has {covid.shape[0]} rows, and {covid.shape[1]} columns.") 
print(f" It has the following columns and column types: \n{covid.dtypes}")


# In[82]:


# Convert the data type of the Date column from object to DateTime.
covid['Date'] = pd.to_datetime(covid['Date'])

print(f" The Date column now is of type: {covid['Date'].dtypes}")


# In[83]:


# Drop unnecessary columns.
covid.drop(['Lat', 'Long', 'ISO 3166-1 Alpha 3-Codes', 'Intermediate Region Code'], axis = 1, inplace = True)

# Confirm remaining columns. 
print(f" The covid DataFrame now has the following columns and column types: \n{covid.dtypes}")


# ### 1. Number of cases across the UK.

# In[84]:


# Assumes that daily cases being reported are NEW cases. 
# Use group by and aggregate to determine the number of cases. 
covid.groupby('Country/Region')[['Cases']].sum()


# ### 2. Differences over time between the first and second dose application.

# In[85]:


# Create a dose difference series and determine the sum. 
covid['Dose Difference'] = covid['First Dose'] - covid['Second Dose']
print(f"There are {covid['Dose Difference'].sum()} people less who took the second dose compared to the first does in the UK")


# In[86]:


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
# ---
# ---
# 

# ## Week 4: Assignment Activity
# -----
#     
# The objective of this activity is to: 
# 
# 1. Create a chart that communicates the number of individuals who have received a second dose compared to individuals who have received their first dose in each area.
# 2. Create a visualisation that communicates the number of deaths per month in each region. Review the visualisation to determine whether there are areas that hit higher peaks earlier than other areas.
# 3. Identify which region has the greatest number of recoveries. Then, create a visualisation that communicates the number of recoveries per month in each area. Review the visualisation to determine whether this has been consistent over time.

# ### 1. Second dose compared to First dose recepients per area.

# In[87]:


# Create a sub-group for the vaccines. 
vaccines_group = covid.groupby(['Province/State'])['First Dose', 'Second Dose'].sum().reset_index()


# In[88]:


# Calculate the difference between first and second dose takers. 
vaccines_group['Difference'] = vaccines_group['First Dose'] - vaccines_group['Second Dose']


# In[89]:


# Calculate the RoI (ratio of interest). 
# Eligible*100/first dose; or (first dose - second dose)*100/first dose = first dose only.) 

vaccines_group['RoI'] = (100*vaccines_group['Difference'])/vaccines_group['First Dose']


# In[90]:


# Determine percentage of first dose against second dose. 

vaccines_group['First Percentage'] = (vaccines_group['Second Dose'] / vaccines_group['First Dose'])*100


# In[91]:


vaccines_group


# * Around 95% of those who have had their first dose are fully vaccinated. 

# In[99]:


plot_vaccines = vaccines_group[['Province/State', 
                                'First Dose', 
                                'Second Dose']]

plot_vaccines.plot(kind="bar", x='Province/State')
plt.title('Vaccination Ratios')
plt.xlabel("Province/State")
plt.ylabel("Numbers")
plt.savefig('Vaccination Ratios')


# ### 2. Assess deaths.
# 
# * Group the data by Province/State and Date, and aggregate the death count.
# * Create a lineplot to display the trend of deaths across all regions over time. (Hint: Use the sns.set(rc = {'figure.figsize':(15,8)}) code to increase the size of the plot.)
# * Group the data by Province/State aggregating the death count to determine which Province/State causes the data set to be skewed. 
# * Re-create the lineplot excluding the Province/State that is causing the skewed data set.
# * Convert Date into Months and plot the same line graph as previously. (Hint: Use this code snippet to convert the date: ds1_plot['Month']=pd.to_datetime(ds1_plot['Date']+pd.offsets.MonthBegin(0)).
# * Save this visualisation in an exported and shareable format (PNG).
# * Dot down some ideas to answer the question posed at the end of this activity.

# In[64]:


covid.head()


# In[67]:


# Create a simple lineplot to examine trends per Province/State.

rc = sns.lineplot(x='Date', y='Deaths', hue='Province/State', data=covid)
sns.set(rc = {'figure.figsize':(15,8)})


# * The Province/State labeled as 'Others' is skewing the data. 

# In[75]:


# Replot death trends per Province/State without Others.

rc = sns.lineplot(x='Date', y='Deaths', hue='Province/State', data=covid[covid['Province/State'] != 'Others'])
sns.set(rc = {'figure.figsize':(15,8)})


# In[101]:


# Replot deaths trands per Provice/State without Others and per Month. 
covid['Month'] = covid['Date'] + pd.offsets.MonthBegin(0)

# Plot
rc = sns.lineplot(x='Month', y='Deaths', hue='Province/State', data=covid[covid['Province/State'] != 'Others'])
sns.set(rc = {'figure.figsize':(15,8)})

plt.title('Death Rate per Province/State')
plt.xlabel("Months")
plt.ylabel("Numbers")

# Save plot
plt.savefig('Death Rates.png')


# * Say something here. 

# ### 3. Assess recoveries. 
# 
# Which region has the greatest number of recoveries? The number of recoveries per month in each area. Determine whether this has been consistent over time.
# 
# * Group the data by Province/State, and aggregate the count of recovered cases and sort the values of recovered cases in ascending order.
# * Convert Date into Months as previously and create a lineplot.
# * Group Province/State and Month to aggregate the count of recovered cases.
# * Create a lineplot to visualise the trend of recovered cases across the months.
# * Save this visualisation in an exported and shareable format (PNG). 
# * Dot down some ideas to answer the question posed at the end of this activity.

# In[171]:


recovered_cases = covid.groupby(['Province/State'])['Recovered'].sum().sort_values(ascending=True)
recovered_cases


# * Channel Islands have the highest number of recovered cases. 

# In[104]:


# Plot
rc = sns.lineplot(x='Month', y='Recovered', hue='Province/State', data=covid)
plt.title('Recovery per Province/State')
plt.xlabel("Months")
plt.ylabel("Numbers of Recovered Cases")


# ### 5. General Observations
# 
# 1. Around 95% of those who have had their first dose are fully vaccinated.
# 2. The Province/State labeled as 'Others' is skewing the data.
# 3. Deaths seem to have peaked only in very few Provinces / States such as British Virgin Islands. 
# 4. Channel Islands has the highest recovery numbers. 
# 
# ---
# ---

# ## Week 5: Assignment Activity
# -----
# 
# The objective is to identify the top trending hashtags related to COVID.

# In[35]:


# View the data. 
tweets.head()


# In[183]:


tweets.columns


# In[284]:


# Check for retweets to assess if there's an impact on the data. 
tweets.retweet_count.value_counts()


# In[285]:


# Check for retweets to assess if there's an impact on the data. 
tweets.favorite_count.value_counts()


# * Too small of a sample for influence. 

# **Look for hashtags**

# In[288]:


tweets['text'] = tweets['text'].astype(str)


# In[290]:


tweets_text = tweets['text'].apply(lambda x: x if x.strip() != None else None)
tweets_text.shape
tweets_text.head()


# In[296]:


# Loop through to extract the hashtags.

hash_tags = []
for y in [x.split(' ') for x in tweets_text.values]:
    for x in y:
        if '#' in x:
            hash_tags.append(x)
            
print(hash_tags)
            
# Create a Series containing the values. 
hash_tags = pd.Series(hash_tags).value_counts()


# In[297]:


# Display the first 30. 
hash_tags.head(30)


# In[299]:


# Create a DataFrame from the series for the visualisations. 
data = pd.DataFrame(hash_tags).reset_index()
# Rename the Columns. 
data.columns = ['word', 'count']
data['count'] = data['count'].astype(int)
data


# In[300]:


# Display the top 100. 

display(data.loc[(data['count']>100)])


# In[301]:


# Plot records for hashtags that are greater than 100.

ax = sns.barplot(x='count', y='word', data=data.loc[(data['count']>100)])


# In[331]:


txt_file = open("stop_words_english.txt", "r")
file_content = txt_file.read()
sw_list = file_content.split("\n")
txt_file.close()


# In[332]:


tweets_text_values = tweets_text.values

tweets_text_values_words = [x.split(' ') for x in tweets_text_values]

tweets_text_values_words_all = []

tweets_text_values_words_all = [z for y in tweets_text_values_words for z in y                                 if 'http' not in z and not                                 z.startswith(('%','%')) and z.lower() not in sw_list]

tweets_text_values_words_all = pd.Series(tweets_text_values_words_all).value_counts()


# In[333]:


tweets_text_values_words_all.head(50)


# In[334]:


data2 = pd.DataFrame(tweets_text_values_words_all).head(16).reset_index()

data2.columns = ['word', 'count']


# In[335]:


data2 = data2[data2['word'].str.strip('word') != '']
data2


# In[336]:


ax = sns.barplot(x='count', y='word', data=data2)


# In[337]:


dft = pd.DataFrame(tweets_text_values)
dft.columns = ['Tweets']


# In[341]:


subset = dft[dft['Tweets'].str.contains('people')]

for i in subset.index:
    print('Tweet: ', i)
    print(subset.loc[i, 'Tweets'], '\n')


# ### 3. Observations
# 
# 1. Perhaps unsurprisingly, Covid, Covid19, China, and people are top of the list of hashtags and words used on twitter. 
# 2. Greece and Athens are two other words that were used much at the time. Further to the review of the data set and cross checking with the news, numbers in Greece at the time where peaking. 
# 
# ---
# ---
# 

# ## Week 6: Assignement Activity
# ---

# The objective is to (1) demonstrate the use of the functions provided, and (2) answer additional questions posed by the government.
# In addition, to anwser 3 questions with regards to Data and Data Analytics. 

# In[36]:


# Adjust settings
get_ipython().run_line_magic('matplotlib', 'inline')


# In[37]:


# Load and select relevant subset of the data
# Make sure to change the relative path to function in your environment
ds1 = pd.read_csv('covid_19_uk_cases.csv')
ds2 = pd.read_csv('covid_19_uk_vaccinated.csv')

sample = ds1[['Province/State','Date','Hospitalised']]


# In[38]:


# Select data for a specific province
sample_ci = sample[sample['Province/State'] == "Channel Islands"]


# In[39]:


# Define function to plot moving averages
def plot_moving_average(series, window, plot_intervals=False, scale=1.96):
    
    # Create a rolling window to calculate the rolling mean using the series.rolling function
    rolling_mean = series.rolling(window=window).mean()
    
    # Declare the dimensions for the plot, plot name and plot the data consisting of the rolling mean from above 
    plt.figure(figsize=(18,4))
    plt.title('Moving average\n window size = {}'.format(window))
    plt.plot(rolling_mean, 'g', label='Simple moving average trend')

    
    # Plot confidence intervals for smoothed values
    if plot_intervals:
        
        # Calculate the mean absolute square 
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        
        # Calculate the standard deviation using numpy's std function
        deviation = np.std(series[window:] - rolling_mean[window:])
        
        # Calculate the upper and lower bounds 
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        
        # Name and style upper and lower bound lines and labels 
        plt.plot(upper_bound, 'r--', label='Upper bound / Lower bound')
        plt.plot(lower_bound, 'r--')
    
    # Plot the actual values for the entire timeframe
    plt.plot(series[window:], label='Actual values')
    plt.grid(True)


# In[40]:


# Define function to calculate the mean absolute error
def mean_absolute_error(a, b): return abs(b - a)


# ### Question 1:
# 
# The consultant indicated that the function is functional, but did not demonstrate how to use it. Use the provided function, `plot_moving_average()`, to plot the data for the selected province (variable name is `sample_ci` and set the window parameter to 7 days. 

# In[43]:


# Demonstrate the use of the function to plot moving averages
window = 7
plot_moving_average(sample_ci['Hospitalised'], window, plot_intervals=False, scale=1.96)


# ### Question 2:
# 
# The consultant performed a calculation that looks interesting, but the team is unsure about what the intention was and how to interpret the output. Can you offer some insights into the meaning of the code and output in the cell below? Is it useful?

# In[44]:


# Return the top three days with biggest difference between daily value and rolling 7-day mean
s = sample_ci.copy()
s_rolling = s['Hospitalised'].rolling(window=7).mean()
s['error'] = mean_absolute_error(s['Hospitalised'][7:], s_rolling[7:])
s.sort_values('error', ascending=False).head(3)


# >In the above, I believe the consultant was trying to anwser a few questions: 
# * Firstly, to identify the top 3 days that may have seen peaks in terms of covid hospitalizations. 
# * Secondly, through identitying these days, and calculating the error, the consultant would be able to assert whether or not the peaks are accurate. 
# * Lastly, if the peeks are deemed inaccurate due to the error, the consultant could then take a step back and reconsidered the rolling average, as it may be skewed by the inaccurate peaks. 
# 
# All in all, the calcuation is useful and does provide some insights into the data and the situation during covid. If accurate, these findings could as an example help highlight a "super-spreader" event that may have take place a few days before the peak. 

# ### Question 3:
# 
# The management team had some additional questions around the project where they asked for further feedback to be included in your final presentation. Make sure to answer the questions in the Notebook in Markdown format in preparation for your presentation. The expectation is that you will provide short and direct responses to help them understand the importance and impact of the questions below.

# #### Question 3.1
# - What is the difference between qualitative and quantitative data? How can these be used in business predictions?
# 
# Anwser:
# 
# 
# **Qualitative data**, also known as categorical data, is data that describes qualities and/or characteristics. Whereas **quantitative data** is data of measurable values in the form of numbers and counts. 
# 
# * As an example, customer satisfaction surveys and customer demographics are a good example of qualitative data which can be used in business predictions.
# 
# * On the other hand, sales figures over time is a good example of quantitative data which can be used in business predictions. 

# #### Question 3.2
# - Can you provide you observations around why continuous improvement is required, can we not just implement the project and move on to other pressing matters?
# 
# Anwser: 
# 
# In the word of data analytics, it is almost never the case that a project is "done". Very rarely is it the case the data generation for a specific case ceases. In fact, it is almost the case that new data points are being generated. As an example, the data sets examined here by the consultant is almost 2 years old. While it is still valid data, the introduction of data sets from then and up to today will very likely offer new insights that are otherwise completely missed. 
# 
# Further, there are other indirect discoveries that may require a data analyist to reconsider their analysis over time. A perfect example of that is the case of the racial bais highlighted in an algorithm for used by healthcare providers in the United States recently. In light of such a disturbing and impactful discovery, it is critical that analysts go back and re-examine the data with this new information. Perhaps, new results and insights can be extracted. 
# 
# While this may be an extreme case, nonetheless the changing nature of the subject should always be considered by an analyst and communicated clearly to the client. It defines the importances of continuous improvement and the frequency an analyst should be visiting / revisitng the data and their analysis. 

# #### Question 3.3 (double click cell to edit)
# - As a government, we adhere to all data protection requirements and have good governance in place. Does that mean we can ignore data ethics? We only work with aggregated data and therefore will not expose any personal details? (Provide an example of how data ethics could apply to this case; two or three sentences max)
# 
# Anwser:
# 
# Governments must NOT ignore data ethics. Although the privacy of individuals may be protected, is the overall use of the data serving the overall public interest? In the case of Covid and the analysis above, is the use of the data helping identify paterns that are useful for the public good of understanding Covid, its spread, affected populations, uptake in vaccinations, recoveries, etc. 
# In the case of Covid, the anwser to the above may be a lot easer than some other cases. 

# ---
# ---
# >>> # END OF NOTEBOOK
# ---
# ---
