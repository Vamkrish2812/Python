import pandas as pd

nba=pd.read_csv('D:\\fortune1000.csv')

print(nba)


c=nba.groupby('Sector')

# #print(c.get_group('Wholesalers: Health Care'))

n=c.agg({'Employees': 'sum'})

print(n)