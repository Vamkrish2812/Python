import pandas as pd
data={
    'Region' : ['North','South','East','West','North','South','East','West'],
    'Product' : ['A','A','A','A','B','B','B','B'],
    'Month' : ['Jan','Jan','Jan','Jan','Feb','Feb','Feb','Feb'],
    'Sales' : [250, 150,200,100,300,400,350,200]
}

df= pd.DataFrame( data )
pivot_df=df.pivot(index='Month',columns='Region',values='Sales',aggfunc='mean')
print(pivot_df)

