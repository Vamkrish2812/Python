import pandas as pd

nba=pd.read_csv('D:\\nba.csv')

texasplayer = nba.Team=='Miami Heat' 
pos=nba.Position='PG'

#print(nba[texasplayer & pos].shape)

# print(nba[(nba.Team=='Boston Celtics') | (nba.Team=='Toronto Raptors')])

# # return non null salary rows
# print(nba[~nba.Salary.isnull()])

# print(nba[nba.Weight.between(183,185)].Name)
# # sorting
# print(nba.sort_values(by='Weight' ,ascending=False))
# nb=nba[(nba.Team=='Miami Heat') & (nba.Position='PG')].nba.sort_values(by='Salary' ,ascending=False)
b=nba[ (nba.Team=='Miami Heat') & (nba.Position=='PG')].sort_values(by='Salary',ascending=False)

print(b)