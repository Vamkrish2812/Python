import pandas as pd
import numpy as np
responseTime = [10,29,18,42,55]
# r_arr=np.array(responseTime)
# print(np.max(r_arr))

my_series = pd.Series(responseTime)

nba=pd.read_csv('D:\\nba.csv')

#cs=pd.read_html('www.google.com')

# rows * columns
print(nba.shape)
# column name
print(nba.columns)
# object-string data type --- data types
print(nba.dtypes)
# gives the analytical data
print(nba.describe())
# clear info about data frame
print(nba.info())
# tells in each column how many null values are there
print(nba.isna().sum())
# gives first 5 rows
print(nba.head())
# single column -- two columns
print(nba['Name'])
print(nba.Name)
# creating new column and assigning value
nba['my sport']='basketball'
# del column
del nba['my sport']
# Accesing multiple columns
show_list=['Name','College','Salary']
print(nba[show_list].head(3))