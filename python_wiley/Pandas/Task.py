import pandas as pd

nba=pd.read_csv('D:\\jamesbond.csv')



#nba.iloc[2]

# nba.iloc[[2,5,9]]

# nba.iloc[:5]

# nba.iloc[22:]

# nba.iloc[2:8]

# nba.iloc[2:21:2]

nba.set_index('Year',inplace=True)

print(nba.loc[1967])