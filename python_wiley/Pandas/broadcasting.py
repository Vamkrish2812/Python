import pandas as pd

nba=pd.read_csv('D:\\food.csv')
nba1=pd.read_csv('D:\\nba.csv')

def tomill(weight):
    return f'{0.45*weight} Kg.'

nba1['Weight(in kg)']=nba1.Weight.apply(tomill)

#print(nba.sort_values(by='Spend',ascending=False))

#print(nba[(nba.Frequency=='Daily') & (nba.City=='New York')].sort_values(by='Spend',ascending=False))

print(nba1)

