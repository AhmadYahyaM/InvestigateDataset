#!/usr/bin/env python
# coding: utf-8

# ## Name: Ahmad Abu Saida

# # Project: Investigate a Dataset (TMDb_Movies Dataset)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ## Overview
# To complete my Data Analysis project I am using TMDb movies dataset.
# 
# This data set contains information about 10866 movies collected from The Movie Database (TMDb), including user ratings and revenue. It consist of 21 columns such as imdb_id, revenue, budget, vote_count etc.
# 
# Questions that can analyze from this data set:
# 
#     1. Which movies had the most and least profit?
#     2. Which movies with largest and lowest budgets?
#     3. Which movies with most and least earned revenue?
#     4. Which movies with longest and shortest runtime values?
#     5. What is the average runtime of all the movies?
#     6. In which year we had most numbers of profitable movies?
#     7. What kind of movies successful genres?
#     8. What is most usual cast?
#     9. What is the average budget?
#     10. What is average revenue?
#     11. What is the average duration of the movie?

# In[3]:


# Use this cell to set up import statements for all of the packages that you
#   plan to use.

# Remember to include a 'magic word' so that your visualizations are plotted
#   inline with the notebook. See this page for more:
#   http://ipython.readthedocs.io/en/stable/interactive/magics.html

#importing important files 
import pandas as pd
import numpy as np
import csv
from datetime import datetime
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# After observing the dataset and proposed questions for the analysis we will be keeping only relevent data deleting the unused data so that we can make our calculation easy and understandable.
# 
# ### General Properties

# In[4]:


# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.

#loading the csv file and storing it in the variable "tmbd_data"
tmdb_data = pd.read_csv('tmdb-movies.csv')

#printing first five rows with defined columns of tmdb-movies database
tmdb_data.head()


# ## Obsevations from the data set
# 
# 1.) No unit of currency is mentioned in the dataset. So for my analysis I will take it as dollar as it is the most used international currency.
# 
# 2.) vote_count is different for all the movies, so we cannot directly conculed the popularity of the movies based on the average vote count

# ## Data Cleaning (Removing the unused information from the dataset)

# ## Important observation regarding this process
# 
# 1.We need to remove unused column such as id, imdb_id, vote_count,
# 
# 2.production_company, keywords, homepage etc.
# 
# 3.Removing the duplicacy in the rows(if any).
# 
# 4.Some movies in the database have zero budget or zero revenue, that is there 
# 
# 5.value has not been recorded so we will be discarding such entries
# 
# 6.Changing release date column into date format.
# 
# 7.Replacing zero with NAN in runtime column.
# 
# 8.Changing format of budget and revenue column.

# ## 1. Removing Unused columns
# 
# Columns that we need to delete are - id, imdb_id, popularity, budget_adj, revenue_adj, homepage, keywords, overview, production_companies, vote_count and vote_average.

# In[5]:


#creating a list of columb to be deleted
del_col=[ 'id', 'imdb_id', 'popularity', 'budget_adj', 'revenue_adj', 'homepage', 'keywords', 'overview', 'production_companies', 'vote_count', 'vote_average']

#deleting the columns
tmdb_data= tmdb_data.drop(del_col,1)

#previewing the new dataset
tmdb_data.head(4)


# ## 2. Removing the duplicates in the rows(if any)
# 
# Lets see how many entries we have in the database

# In[6]:


rows, col = tmdb_data.shape
#We need to reduce the count of row by one as contain header row also.
print('There are {} total entries of movies and {} no.of columns in it.'.format(rows-1, col))


# Now removing the duplicate rows if any!

# In[7]:


tmdb_data.drop_duplicates(keep ='first', inplace=True)
rows, col = tmdb_data.shape

print('There are now {} total entries of movies and {} no.of columns in it.'.format(rows-1, col))


# So there was a duplicate row and it has been removed now.

# ## 3. Removing 0's from budget and the revenue columns

# In[8]:


# creating a seperate list of revenue and budget column
temp_list=['budget', 'revenue']

#this will replace all the value from '0' to NAN in the list
tmdb_data[temp_list] = tmdb_data[temp_list].replace(0, np.NAN)

#Removing all the row which has NaN value in temp_list 
tmdb_data.dropna(subset = temp_list, inplace = True)

rows, col = tmdb_data.shape
print('So after removing such entries, we now have only {} no.of movies.'.format(rows-1))


# ## 4. Changing the release date column into standard date format

# In[9]:


tmdb_data.release_date = pd.to_datetime(tmdb_data['release_date'])


# In[10]:


# printing the changed dataset
tmdb_data.head(3)


# ## 5. Replacing zero with NAN in runtime column.

# In[11]:


#replacing 0 with NaN of runtime column in the dataset
tmdb_data['runtime'] =tmdb_data['runtime'].replace(0, np.NAN)


# ## 6. Changing format of budget and revenue column

# Checking the current format of columns in the dataset

# In[12]:


#printing the data type of the data set
tmdb_data.dtypes


# In[13]:


change_type=['budget', 'revenue']
#changing data type
tmdb_data[change_type]=tmdb_data[change_type].applymap(np.int64)
#printing the changed information
tmdb_data.dtypes


# <a id='eda'></a>
# ## Exploratory Data Analysis

# ## 1. Calculating the profit of the each movie

# In[14]:


#insert function with three parameters(index of the column in the dataset, name of the column, value to be inserted)
tmdb_data.insert(2,'profit_earned',tmdb_data['revenue']-tmdb_data['budget'])

#previewing the changes in the dataset
tmdb_data.head(2)


# ## Research Question 1 : Which movies had the most and least profit?

# In[15]:


import pprint
#defining the function
def calculate(column):
    #for highest earned profit
    high= tmdb_data[column].idxmax()
    high_details=pd.DataFrame(tmdb_data.loc[high])
    
    #for lowest earned profit
    low= tmdb_data[column].idxmin()
    low_details=pd.DataFrame(tmdb_data.loc[low])
    
    #collectin data in one place
    info=pd.concat([high_details, low_details], axis=1)
    
    return info

#calling the function
calculate('profit_earned')


# - Column with id 1386 shows the highest earned profit i.e 2,544,505,847 
# 
# - Whereas the column with id 2244 shows the lowest earned profit i.e 413,912,431

# ## Research Question 2 : Which movies with largest and lowest budgets?

# In[16]:


# we will call the same function **calculate(column)** again for this analysis
calculate('budget')


# - Column with id 2244 shows the largest budget i.e 425,000,000 dollar
# 
# - Whereas the column with id 2618 shows the smallest budget i.e 1 dollar

# ## Research Question 3 : Which movies with most and least earned revenue?

# In[17]:


# we will call the same function **calculate(column)** again for this analysis
calculate('revenue')


# - Column with id 1386 shows the largest revenue earned i.e 2,781,505,847 dollar
# 
# - Whereas the column with id 5067 shows the smallest revenue earned i.e 2 dollar

# ## Research Question 4 : Which movies with longest and shortest runtime values?

# In[18]:


# we will call the same function **calculate(column)** again for this analysis
calculate('runtime')


# - Column with id 2107 shows the longest runtime i.e 338 minutes
# 
# - Whereas the column with id 5162 shows the shortest runtime i.e 15 minutes

# ## Research Question 5 : What is the average runtime of all the movies?

# In[19]:


# defining a function to find average of a column
def avg_fun(column):
    return tmdb_data[column].mean()


# In[20]:


#calling above function
avg_fun('runtime')


# So the average runtime a movie is 109 minutes. Lets analyse it in a visual form i.e. by graphical approach.

# In[21]:


#plotting a histogram of runtime of movies

#giving the figure size(width, height)
plt.figure(figsize=(9,5), dpi = 100)

#On x-axis 
plt.xlabel('Runtime of the Movies', fontsize = 14)
#On y-axis 
plt.ylabel('Nos.of Movies in the Dataset', fontsize=14)
#Name of the graph
plt.title('Runtime of all the movies', fontsize=14)

#giving a histogram plot
plt.hist(tmdb_data['runtime'], rwidth = 0.9, bins =35)
#displays the plot
plt.show()


# - The distribution of the above formed graph is positively skewed or right skewed! Most of the movies are timed between 80 to 115 minutes. Almost 1000 and more numbers of movies fall in this criteria.

# ## Lets analyse more about runtime of the movie using different kind of plots i.e Box Plot and Data Point Plot

# In[22]:


import seaborn as sns
#The First plot is box plot of the runtime of the movies 
plt.figure(figsize=(9,7), dpi = 105)

#using seaborn to generate the boxplot
sns.boxplot(tmdb_data['runtime'], linewidth = 3)
#diplaying the plot
plt.show()


# In[23]:


#getting specific runtime 
tmdb_data['runtime'].describe()


# The plot generated above give a visual of complete distribution of runtime of movies by plotting the points againts their respective position in the ditribution
# 
# Coming to our first plot i.e. box-plot, It gives us an overall idea of how spreaded the ditribution is in case of runtime of the movies. we also get the outliners her if you carefully observe the plot.
# 
# By looking at both the plot and calculations, we can conclude that..
# 
# - 25% of movies have a runtime of less than 95 minutes
# - 50% of movies have a runtime of less than 109 minutes. (median)
# - 75% of movies have a runtime of less than 119 minutes

# ## Research Question 6 : Which year we had most numbers of profitable movies?

# In[24]:


#We will be using Line plot for this analysis
#Since we want to know the profits of movies for every year therefore we have to sum up all the movies of a particular year

profits_year = tmdb_data.groupby('release_year')['profit_earned'].sum()

#figure size(width, height)
plt.figure(figsize=(12,6), dpi = 130)

#on x-axis
plt.xlabel('Release Year of Movies in the data set', fontsize = 12)
#on y-axis
plt.ylabel('Profits earned by Movies', fontsize = 12)
#title of the line plot
plt.title('Representing Total Profits earned by all movies Vs Year of their release.')

#plotting the graph
plt.plot(profits_year)

#displaying the line plot
plt.show()


# In[25]:


#To find that which year made the highest profit?
profits_year.idxmax()


# - So we can conclude both graphically as well as by calculations that year 2015 was the year where movies made the highest profit.
# 
# - We are now done with analysing the given dataset.We will now find characteristics of profitable movies.

# ## With respect to the profitable movies
# Before moving further we need to clean our data again. We will be considering only those movies who have earned a significant amount of profit.
# 
# ## So lets fix this amount to 100 million dollar.

# In[26]:


#selecting the movies having profit $50M or more
profit_data = tmdb_data[tmdb_data['profit_earned'] >= 100000000]

#reindexing new data
profit_data.index = range(len(profit_data))

#we will start from 1 instead of 0
profit_data.index = profit_data.index + 1

#printing the changed dataset
profit_data.head(3)


# In[27]:


#counting the no.of rows in the new data base
len(profit_data)


# So our dataset is reduced to 826 from 3853

# ## Research Question 7 : What kind of movies successful genres?

# In[28]:


#function which will take any column as argument from and keep its track 
def data(column):
    #will take a column, and separate the string by '|'
    data = profit_data[column].str.cat(sep = '|')
    
    #giving pandas series and storing the values separately
    data = pd.Series(data.split('|'))
    
    #arranging in descending order
    count = data.value_counts(ascending = False)
    
    return count


# In[29]:


#variable to store the retured value
count = data('genres')
#printing top 5 values
count.head()


# - Lets to a graphical analysis of the above collected data.

# In[30]:


#lets plot the points in descending order top to bottom as we have data in same format.
count.sort_values(ascending = True, inplace = True)

#ploting
lt = count.plot.barh(color = '#00FF00', fontsize = 12)

#title
lt.set(title = 'Frequent Used Genres in Profitable Movies')

# on x axis
lt.set_xlabel('Nos.of Movies in the dataset', color = 'black', fontsize = '13')

#figure size(width, height)
lt.figure.set_size_inches(12, 9)

#ploting the graph
plt.show()


# ## Research Question 8 : What is most usual cast?

# We will call the same function data (column) again for this analysis.

# In[31]:


#variable to store the retured value
count = data('cast')
#printing top 5 values
count.head()


# - Tom Cruise is on the top with total 23 cast followed by Tom Hanks with 19 Brad Pitt with 18.

# ## Research Question 9 : What is the average budget?

# In[32]:


#New function to find average 
def profit_avg(column):
    return profit_data[column].mean()


# In[33]:


# calling the above function for budget
profit_avg('budget')


# - So the movies having profit of 100 million dollar and more have an average budget of 74 million dollar.

# ## Research Question 10 : What is average revenue?

# In[34]:


# calling the above function for revenue
profit_avg('revenue')


# - So the movies having profit of 100 million dollar and more have an average revenue of 345 million dollar.

# ## Research Question 11 : What is the average duration of the movie?

# In[35]:


# calling the above function for 
profit_avg('runtime')


# - So the movies having profit of 100 million dollar and more have an average duration of 115 minutes.

# ## Conclusions
# 
# This was a very interesting data analysis. After this analysis we can conclude following:
# 
# ## For a Movie to be in successful criteria
# 
# Average Budget must be around 74 millon dollar
# Average duration of the movie must be 115 minutes
# Any one of these should be in the cast :Tom Cruise, Tom Hanks, Brad Pitt, Adam Sendler, Sylvester Stallone.
# Genre must be : Action,  Comedy, Adventure, Drama, Thriller.
# By doing all this the movie might be one of the hits and hence can earn an average revenue of around 345 million dollar.
# 
# Limitations: This analysis was done considering the movies which had a significant amount of profit of around 100 million dollar. This might not be completely error free but by following these suggestion one can increase the probability of a movie to become a hit. Moreover we are not sure if the data provided to us is completel corect and up-to-date. As mentioned before the budget and revenue column do not have currency unit, it might be possible different movies have budget in different currency according to the country they are produce in. So a disparity arises here which can state the complete analysis wrong. Dropping the rows with missing values also affected the overall analysis.

# ## Reference: Udacity file data

# In[ ]:





# In[ ]:




