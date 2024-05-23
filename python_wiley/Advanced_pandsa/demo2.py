import pandas as pd

nba=pd.read_csv('D:\\fortune1000.csv')

#print(nba)

print(len(nba))

print(nba.Sector.nunique())

# print(nba.Sector.unique())


#print(nba.Sector.value_counts())

# c=nba['Location'].str.split(',', expand=True)

# print(c[1].value_counts())

nba.drop_duplicates(inplace=True)

print(len(nba))