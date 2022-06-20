# lse_da_covid_analysis
LSE Covid Analysis with Python


Week 2
General Observations
The Data doesn't have a specified index; rather a sequence number.

Out of a total 5727 cases in Gibraltar, 4907 were hospitalized, 4670 recovered, and 97 died.

The number of hospitalization in Gibraltar is extremely high relative to the number of total cases.

The DataFrame has 8 missing values: 2 in the deaths column, 2 in the cases column, 2 in the recovered column, and 2 in the hospitalised column. However, as determined below, the data belongs to 2 instances on 2020-09-21 and 2020-09-22 in Bermuda. The reason for the missing data is likely due to the Tropical Storm Teddy, which hit Bermuda on the 21st of September. Teddy's centre was located offshore approximately 310 km south-east of Bermuda main island, with maximum sustained wind of 165 km/h.

More people have taken the first dose of vaccination than the second.

Week 3 
General Observations
The total number of cases across the United Kingdom is 1.627917e+09.
Vaccine update reduced between the first and the second vaccine doses with 2,118,019 less people taking the second dose.
Gibraltar had the highest number of individuals who received the first dose but not the second; 264,745 less people received the second dose.
The general trend in vaccination starts slow with first doses; speeds up with some second doses (a few compared to the first doses). However, as expected, first doses start to reduce while second doses pick up drastically.
All in all though, over time, the amount of vaccinations seem to slow down towards the end of the data set with the second doses. This could be a result of the data sample stopping before people receive their second dose.
