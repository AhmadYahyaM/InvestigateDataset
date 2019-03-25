
## Name: Ahmad Abu Saida

# Project: Investigate a Dataset (TMDb_Movies Dataset)

## Table of Contents
<ul>
<li><a href="#intro">Introduction</a></li>
<li><a href="#wrangling">Data Wrangling</a></li>
<li><a href="#eda">Exploratory Data Analysis</a></li>
<li><a href="#conclusions">Conclusions</a></li>
</ul>

<a id='intro'></a>
## Introduction

## Overview
To complete my Data Analysis project I am using TMDb movies dataset.

This data set contains information about 10866 movies collected from The Movie Database (TMDb), including user ratings and revenue. It consist of 21 columns such as imdb_id, revenue, budget, vote_count etc.

Questions that can analyze from this data set:

    1. Which movies had the most and least profit?
    2. Which movies with largest and lowest budgets?
    3. Which movies with most and least earned revenue?
    4. Which movies with longest and shortest runtime values?
    5. What is the average runtime of all the movies?
    6. In which year we had most numbers of profitable movies?
    7. What kind of movies successful genres?
    8. What is most usual cast?
    9. What is the average budget?
    10. What is average revenue?
    11. What is the average duration of the movie?


```python
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
% matplotlib inline
```

<a id='wrangling'></a>
## Data Wrangling

After observing the dataset and proposed questions for the analysis we will be keeping only relevent data deleting the unused data so that we can make our calculation easy and understandable.

### General Properties


```python
# Load your data and print out a few lines. Perform operations to inspect data
#   types and look for instances of missing or possibly errant data.

#loading the csv file and storing it in the variable "tmbd_data"
tmdb_data = pd.read_csv('tmdb-movies.csv')

#printing first five rows with defined columns of tmdb-movies database
tmdb_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>imdb_id</th>
      <th>popularity</th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>cast</th>
      <th>homepage</th>
      <th>director</th>
      <th>tagline</th>
      <th>...</th>
      <th>overview</th>
      <th>runtime</th>
      <th>genres</th>
      <th>production_companies</th>
      <th>release_date</th>
      <th>vote_count</th>
      <th>vote_average</th>
      <th>release_year</th>
      <th>budget_adj</th>
      <th>revenue_adj</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>135397</td>
      <td>tt0369610</td>
      <td>32.985763</td>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>http://www.jurassicworld.com/</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>...</td>
      <td>Twenty-two years after the events of Jurassic ...</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Universal Studios|Amblin Entertainment|Legenda...</td>
      <td>6/9/15</td>
      <td>5562</td>
      <td>6.5</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>1.392446e+09</td>
    </tr>
    <tr>
      <th>1</th>
      <td>76341</td>
      <td>tt1392190</td>
      <td>28.419936</td>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>http://www.madmaxmovie.com/</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>...</td>
      <td>An apocalyptic story set in the furthest reach...</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>Village Roadshow Pictures|Kennedy Miller Produ...</td>
      <td>5/13/15</td>
      <td>6185</td>
      <td>7.1</td>
      <td>2015</td>
      <td>1.379999e+08</td>
      <td>3.481613e+08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>262500</td>
      <td>tt2908446</td>
      <td>13.112507</td>
      <td>110000000</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>
      <td>http://www.thedivergentseries.movie/#insurgent</td>
      <td>Robert Schwentke</td>
      <td>One Choice Can Destroy You</td>
      <td>...</td>
      <td>Beatrice Prior must confront her inner demons ...</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>Summit Entertainment|Mandeville Films|Red Wago...</td>
      <td>3/18/15</td>
      <td>2480</td>
      <td>6.3</td>
      <td>2015</td>
      <td>1.012000e+08</td>
      <td>2.716190e+08</td>
    </tr>
    <tr>
      <th>3</th>
      <td>140607</td>
      <td>tt2488496</td>
      <td>11.173104</td>
      <td>200000000</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>Harrison Ford|Mark Hamill|Carrie Fisher|Adam D...</td>
      <td>http://www.starwars.com/films/star-wars-episod...</td>
      <td>J.J. Abrams</td>
      <td>Every generation has a story.</td>
      <td>...</td>
      <td>Thirty years after defeating the Galactic Empi...</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>Lucasfilm|Truenorth Productions|Bad Robot</td>
      <td>12/15/15</td>
      <td>5292</td>
      <td>7.5</td>
      <td>2015</td>
      <td>1.839999e+08</td>
      <td>1.902723e+09</td>
    </tr>
    <tr>
      <th>4</th>
      <td>168259</td>
      <td>tt2820852</td>
      <td>9.335014</td>
      <td>190000000</td>
      <td>1506249360</td>
      <td>Furious 7</td>
      <td>Vin Diesel|Paul Walker|Jason Statham|Michelle ...</td>
      <td>http://www.furious7.com/</td>
      <td>James Wan</td>
      <td>Vengeance Hits Home</td>
      <td>...</td>
      <td>Deckard Shaw seeks revenge against Dominic Tor...</td>
      <td>137</td>
      <td>Action|Crime|Thriller</td>
      <td>Universal Pictures|Original Film|Media Rights ...</td>
      <td>4/1/15</td>
      <td>2947</td>
      <td>7.3</td>
      <td>2015</td>
      <td>1.747999e+08</td>
      <td>1.385749e+09</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 21 columns</p>
</div>



## Obsevations from the data set

1.) No unit of currency is mentioned in the dataset. So for my analysis I will take it as dollar as it is the most used international currency.

2.) vote_count is different for all the movies, so we cannot directly conculed the popularity of the movies based on the average vote count

## Data Cleaning (Removing the unused information from the dataset)

## Important observation regarding this process

1.We need to remove unused column such as id, imdb_id, vote_count,

2.production_company, keywords, homepage etc.

3.Removing the duplicacy in the rows(if any).

4.Some movies in the database have zero budget or zero revenue, that is there 

5.value has not been recorded so we will be discarding such entries

6.Changing release date column into date format.

7.Replacing zero with NAN in runtime column.

8.Changing format of budget and revenue column.

## 1. Removing Unused columns

Columns that we need to delete are - id, imdb_id, popularity, budget_adj, revenue_adj, homepage, keywords, overview, production_companies, vote_count and vote_average.


```python
#creating a list of columb to be deleted
del_col=[ 'id', 'imdb_id', 'popularity', 'budget_adj', 'revenue_adj', 'homepage', 'keywords', 'overview', 'production_companies', 'vote_count', 'vote_average']

#deleting the columns
tmdb_data= tmdb_data.drop(del_col,1)

#previewing the new dataset
tmdb_data.head(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>cast</th>
      <th>director</th>
      <th>tagline</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>150000000</td>
      <td>1513528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>6/9/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150000000</td>
      <td>378436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>5/13/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>110000000</td>
      <td>295238201</td>
      <td>Insurgent</td>
      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>
      <td>Robert Schwentke</td>
      <td>One Choice Can Destroy You</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>3/18/15</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>200000000</td>
      <td>2068178225</td>
      <td>Star Wars: The Force Awakens</td>
      <td>Harrison Ford|Mark Hamill|Carrie Fisher|Adam D...</td>
      <td>J.J. Abrams</td>
      <td>Every generation has a story.</td>
      <td>136</td>
      <td>Action|Adventure|Science Fiction|Fantasy</td>
      <td>12/15/15</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



## 2. Removing the duplicates in the rows(if any)

Lets see how many entries we have in the database


```python
rows, col = tmdb_data.shape
#We need to reduce the count of row by one as contain header row also.
print('There are {} total entries of movies and {} no.of columns in it.'.format(rows-1, col))
```

    There are 10865 total entries of movies and 10 no.of columns in it.


Now removing the duplicate rows if any!


```python
tmdb_data.drop_duplicates(keep ='first', inplace=True)
rows, col = tmdb_data.shape

print('There are now {} total entries of movies and {} no.of columns in it.'.format(rows-1, col))
```

    There are now 10864 total entries of movies and 10 no.of columns in it.


So there was a duplicate row and it has been removed now.

## 3. Removing 0's from budget and the revenue columns


```python
# creating a seperate list of revenue and budget column
temp_list=['budget', 'revenue']

#this will replace all the value from '0' to NAN in the list
tmdb_data[temp_list] = tmdb_data[temp_list].replace(0, np.NAN)

#Removing all the row which has NaN value in temp_list 
tmdb_data.dropna(subset = temp_list, inplace = True)

rows, col = tmdb_data.shape
print('So after removing such entries, we now have only {} no.of movies.'.format(rows-1))
```

    So after removing such entries, we now have only 3853 no.of movies.


## 4. Changing the release date column into standard date format


```python
tmdb_data.release_date = pd.to_datetime(tmdb_data['release_date'])
```


```python
# printing the changed dataset
tmdb_data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>budget</th>
      <th>revenue</th>
      <th>original_title</th>
      <th>cast</th>
      <th>director</th>
      <th>tagline</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>150000000.0</td>
      <td>1.513529e+09</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-06-09</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150000000.0</td>
      <td>3.784364e+08</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-05-13</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>110000000.0</td>
      <td>2.952382e+08</td>
      <td>Insurgent</td>
      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>
      <td>Robert Schwentke</td>
      <td>One Choice Can Destroy You</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>2015-03-18</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



## 5. Replacing zero with NAN in runtime column.


```python
#replacing 0 with NaN of runtime column in the dataset
tmdb_data['runtime'] =tmdb_data['runtime'].replace(0, np.NAN)
```

## 6. Changing format of budget and revenue column

Checking the current format of columns in the dataset


```python
#printing the data type of the data set
tmdb_data.dtypes
```




    budget                   float64
    revenue                  float64
    original_title            object
    cast                      object
    director                  object
    tagline                   object
    runtime                    int64
    genres                    object
    release_date      datetime64[ns]
    release_year               int64
    dtype: object




```python
change_type=['budget', 'revenue']
#changing data type
tmdb_data[change_type]=tmdb_data[change_type].applymap(np.int64)
#printing the changed information
tmdb_data.dtypes
```




    budget                     int64
    revenue                    int64
    original_title            object
    cast                      object
    director                  object
    tagline                   object
    runtime                    int64
    genres                    object
    release_date      datetime64[ns]
    release_year               int64
    dtype: object



<a id='eda'></a>
## Exploratory Data Analysis

## 1. Calculating the profit of the each movie


```python
#insert function with three parameters(index of the column in the dataset, name of the column, value to be inserted)
tmdb_data.insert(2,'profit_earned',tmdb_data['revenue']-tmdb_data['budget'])

#previewing the changes in the dataset
tmdb_data.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>budget</th>
      <th>revenue</th>
      <th>profit_earned</th>
      <th>original_title</th>
      <th>cast</th>
      <th>director</th>
      <th>tagline</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>150000000</td>
      <td>1513528810</td>
      <td>1363528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-06-09</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>1</th>
      <td>150000000</td>
      <td>378436354</td>
      <td>228436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-05-13</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>



## Research Question 1 : Which movies had the most and least profit?


```python
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
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1386</th>
      <th>2244</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>budget</th>
      <td>237000000</td>
      <td>425000000</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>2781505847</td>
      <td>11087569</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>2544505847</td>
      <td>-413912431</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>Avatar</td>
      <td>The Warrior's Way</td>
    </tr>
    <tr>
      <th>cast</th>
      <td>Sam Worthington|Zoe Saldana|Sigourney Weaver|S...</td>
      <td>Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...</td>
    </tr>
    <tr>
      <th>director</th>
      <td>James Cameron</td>
      <td>Sngmoo Lee</td>
    </tr>
    <tr>
      <th>tagline</th>
      <td>Enter the World of Pandora.</td>
      <td>Assassin. Hero. Legend.</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>162</td>
      <td>100</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Action|Adventure|Fantasy|Science Fiction</td>
      <td>Adventure|Fantasy|Action|Western|Thriller</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2009-12-10 00:00:00</td>
      <td>2010-12-02 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2009</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>



- Column with id 1386 shows the highest earned profit i.e 2,544,505,847 

- Whereas the column with id 2244 shows the lowest earned profit i.e 413,912,431

## Research Question 2 : Which movies with largest and lowest budgets?


```python
# we will call the same function **calculate(column)** again for this analysis
calculate('budget')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2244</th>
      <th>2618</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>budget</th>
      <td>425000000</td>
      <td>1</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>11087569</td>
      <td>100</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>-413912431</td>
      <td>99</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>The Warrior's Way</td>
      <td>Lost &amp; Found</td>
    </tr>
    <tr>
      <th>cast</th>
      <td>Kate Bosworth|Jang Dong-gun|Geoffrey Rush|Dann...</td>
      <td>David Spade|Sophie Marceau|Ever Carradine|Step...</td>
    </tr>
    <tr>
      <th>director</th>
      <td>Sngmoo Lee</td>
      <td>Jeff Pollack</td>
    </tr>
    <tr>
      <th>tagline</th>
      <td>Assassin. Hero. Legend.</td>
      <td>A comedy about a guy who would do anything to ...</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>100</td>
      <td>95</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Adventure|Fantasy|Action|Western|Thriller</td>
      <td>Comedy|Romance</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2010-12-02 00:00:00</td>
      <td>1999-04-23 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2010</td>
      <td>1999</td>
    </tr>
  </tbody>
</table>
</div>



- Column with id 2244 shows the largest budget i.e 425,000,000 dollar

- Whereas the column with id 2618 shows the smallest budget i.e 1 dollar

## Research Question 3 : Which movies with most and least earned revenue?


```python
# we will call the same function **calculate(column)** again for this analysis
calculate('revenue')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1386</th>
      <th>5067</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>budget</th>
      <td>237000000</td>
      <td>6000000</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>2781505847</td>
      <td>2</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>2544505847</td>
      <td>-5999998</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>Avatar</td>
      <td>Shattered Glass</td>
    </tr>
    <tr>
      <th>cast</th>
      <td>Sam Worthington|Zoe Saldana|Sigourney Weaver|S...</td>
      <td>Hayden Christensen|Peter Sarsgaard|ChloÃ« Sevi...</td>
    </tr>
    <tr>
      <th>director</th>
      <td>James Cameron</td>
      <td>Billy Ray</td>
    </tr>
    <tr>
      <th>tagline</th>
      <td>Enter the World of Pandora.</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>162</td>
      <td>94</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Action|Adventure|Fantasy|Science Fiction</td>
      <td>Drama|History</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2009-12-10 00:00:00</td>
      <td>2003-11-14 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2009</td>
      <td>2003</td>
    </tr>
  </tbody>
</table>
</div>



- Column with id 1386 shows the largest revenue earned i.e 2,781,505,847 dollar

- Whereas the column with id 5067 shows the smallest revenue earned i.e 2 dollar

## Research Question 4 : Which movies with longest and shortest runtime values?


```python
# we will call the same function **calculate(column)** again for this analysis
calculate('runtime')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2107</th>
      <th>5162</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>budget</th>
      <td>18000000</td>
      <td>10</td>
    </tr>
    <tr>
      <th>revenue</th>
      <td>871279</td>
      <td>5</td>
    </tr>
    <tr>
      <th>profit_earned</th>
      <td>-17128721</td>
      <td>-5</td>
    </tr>
    <tr>
      <th>original_title</th>
      <td>Carlos</td>
      <td>Kid's Story</td>
    </tr>
    <tr>
      <th>cast</th>
      <td>Edgar RamÃ­rez|Alexander Scheer|Fadi Abi Samra...</td>
      <td>Clayton Watson|Keanu Reeves|Carrie-Anne Moss|K...</td>
    </tr>
    <tr>
      <th>director</th>
      <td>Olivier Assayas</td>
      <td>Shinichiro Watanabe</td>
    </tr>
    <tr>
      <th>tagline</th>
      <td>The man who hijacked the world</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>runtime</th>
      <td>338</td>
      <td>15</td>
    </tr>
    <tr>
      <th>genres</th>
      <td>Crime|Drama|Thriller|History</td>
      <td>Science Fiction|Animation</td>
    </tr>
    <tr>
      <th>release_date</th>
      <td>2010-05-19 00:00:00</td>
      <td>2003-06-02 00:00:00</td>
    </tr>
    <tr>
      <th>release_year</th>
      <td>2010</td>
      <td>2003</td>
    </tr>
  </tbody>
</table>
</div>



- Column with id 2107 shows the longest runtime i.e 338 minutes

- Whereas the column with id 5162 shows the shortest runtime i.e 15 minutes

## Research Question 5 : What is the average runtime of all the movies?


```python
# defining a function to find average of a column
def avg_fun(column):
    return tmdb_data[column].mean()
```


```python
#calling above function
avg_fun('runtime')
```




    109.22029060716139



So the average runtime a movie is 109 minutes. Lets analyse it in a visual form i.e. by graphical approach.


```python
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
```


![png](output_46_0.png)


- The distribution of the above formed graph is positively skewed or right skewed! Most of the movies are timed between 80 to 115 minutes. Almost 1000 and more numbers of movies fall in this criteria.

## Lets analyse more about runtime of the movie using different kind of plots i.e Box Plot and Data Point Plot


```python
import seaborn as sns
#The First plot is box plot of the runtime of the movies 
plt.figure(figsize=(9,7), dpi = 105)

#using seaborn to generate the boxplot
sns.boxplot(tmdb_data['runtime'], linewidth = 3)
#diplaying the plot
plt.show()
```


![png](output_49_0.png)



```python
#getting specific runtime 
tmdb_data['runtime'].describe()
```




    count    3854.000000
    mean      109.220291
    std        19.922820
    min        15.000000
    25%        95.000000
    50%       106.000000
    75%       119.000000
    max       338.000000
    Name: runtime, dtype: float64



The plot generated above give a visual of complete distribution of runtime of movies by plotting the points againts their respective position in the ditribution

Coming to our first plot i.e. box-plot, It gives us an overall idea of how spreaded the ditribution is in case of runtime of the movies. we also get the outliners her if you carefully observe the plot.

By looking at both the plot and calculations, we can conclude that..

- 25% of movies have a runtime of less than 95 minutes
- 50% of movies have a runtime of less than 109 minutes. (median)
- 75% of movies have a runtime of less than 119 minutes

## Research Question 6 : Which year we had most numbers of profitable movies?


```python
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
```


![png](output_53_0.png)



```python
#To find that which year made the highest profit?
profits_year.idxmax()
```




    2015



- So we can conclude both graphically as well as by calculations that year 2015 was the year where movies made the highest profit.

- We are now done with analysing the given dataset.We will now find characteristics of profitable movies.

## With respect to the profitable movies
Before moving further we need to clean our data again. We will be considering only those movies who have earned a significant amount of profit.

## So lets fix this amount to 100 million dollar.


```python
#selecting the movies having profit $50M or more
profit_data = tmdb_data[tmdb_data['profit_earned'] >= 100000000]

#reindexing new data
profit_data.index = range(len(profit_data))

#we will start from 1 instead of 0
profit_data.index = profit_data.index + 1

#printing the changed dataset
profit_data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>budget</th>
      <th>revenue</th>
      <th>profit_earned</th>
      <th>original_title</th>
      <th>cast</th>
      <th>director</th>
      <th>tagline</th>
      <th>runtime</th>
      <th>genres</th>
      <th>release_date</th>
      <th>release_year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>150000000</td>
      <td>1513528810</td>
      <td>1363528810</td>
      <td>Jurassic World</td>
      <td>Chris Pratt|Bryce Dallas Howard|Irrfan Khan|Vi...</td>
      <td>Colin Trevorrow</td>
      <td>The park is open.</td>
      <td>124</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-06-09</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>2</th>
      <td>150000000</td>
      <td>378436354</td>
      <td>228436354</td>
      <td>Mad Max: Fury Road</td>
      <td>Tom Hardy|Charlize Theron|Hugh Keays-Byrne|Nic...</td>
      <td>George Miller</td>
      <td>What a Lovely Day.</td>
      <td>120</td>
      <td>Action|Adventure|Science Fiction|Thriller</td>
      <td>2015-05-13</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>3</th>
      <td>110000000</td>
      <td>295238201</td>
      <td>185238201</td>
      <td>Insurgent</td>
      <td>Shailene Woodley|Theo James|Kate Winslet|Ansel...</td>
      <td>Robert Schwentke</td>
      <td>One Choice Can Destroy You</td>
      <td>119</td>
      <td>Adventure|Science Fiction|Thriller</td>
      <td>2015-03-18</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>
</div>




```python
#counting the no.of rows in the new data base
len(profit_data)
```




    826



So our dataset is reduced to 826 from 3853

## Research Question 7 : What kind of movies successful genres?


```python
#function which will take any column as argument from and keep its track 
def data(column):
    #will take a column, and separate the string by '|'
    data = profit_data[column].str.cat(sep = '|')
    
    #giving pandas series and storing the values separately
    data = pd.Series(data.split('|'))
    
    #arranging in descending order
    count = data.value_counts(ascending = False)
    
    return count
```


```python
#variable to store the retured value
count = data('genres')
#printing top 5 values
count.head()
```




    Action       317
    Comedy       299
    Adventure    278
    Drama        264
    Thriller     233
    dtype: int64



- Lets to a graphical analysis of the above collected data.


```python
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
```


![png](output_64_0.png)


## Research Question 8 : What is most usual cast?

We will call the same function data (column) again for this analysis.


```python
#variable to store the retured value
count = data('cast')
#printing top 5 values
count.head()
```




    Tom Cruise            23
    Tom Hanks             19
    Brad Pitt             18
    Adam Sandler          17
    Sylvester Stallone    16
    dtype: int64



- Tom Cruise is on the top with total 23 cast followed by Tom Hanks with 19 Brad Pitt with 18.

## Research Question 9 : What is the average budget?


```python
#New function to find average 
def profit_avg(column):
    return profit_data[column].mean()
```


```python
# calling the above function for budget
profit_avg('budget')
```




    74469572.77602905



- So the movies having profit of 100 million dollar and more have an average budget of 74 million dollar.

## Research Question 10 : What is average revenue?


```python
# calling the above function for revenue
profit_avg('revenue')
```




    345328046.81961256



- So the movies having profit of 100 million dollar and more have an average revenue of 345 million dollar.

## Research Question 11 : What is the average duration of the movie?


```python
# calling the above function for 
profit_avg('runtime')
```




    115.62832929782083



- So the movies having profit of 100 million dollar and more have an average duration of 115 minutes.

## Conclusions

This was a very interesting data analysis. After this analysis we can conclude following:

## For a Movie to be in successful criteria

Average Budget must be around 74 millon dollar
Average duration of the movie must be 115 minutes
Any one of these should be in the cast :Tom Cruise, Tom Hanks, Brad Pitt, Adam Sendler, Sylvester Stallone.
Genre must be : Action,  Comedy, Adventure, Drama, Thriller.
By doing all this the movie might be one of the hits and hence can earn an average revenue of around 345 million dollar.

Limitations: This analysis was done considering the movies which had a significant amount of profit of around 100 million dollar. This might not be completely error free but by following these suggestion one can increase the probability of a movie to become a hit. Moreover we are not sure if the data provided to us is completel corect and up-to-date. As mentioned before the budget and revenue column do not have currency unit, it might be possible different movies have budget in different currency according to the country they are produce in. So a disparity arises here which can state the complete analysis wrong. Dropping the rows with missing values also affected the overall analysis.

## Reference: Udacity file data


```python

```


```python

```
