import pandas as pd

nba=pd.read_csv('D:\\nba.csv')

# print(nba.isna().sum())

# nba.dropna(how='any',inplace=True)
# print(len(nba))

# print(nba.isna().sum())

# print(nba.Salary.mean())

#nba.Salary.fillna(round(nba.Salary.mean(),2),inplace=True)

nba.College.fillna('Others',inplace=True)


print(len(nba[(nba.College=='Others')]))