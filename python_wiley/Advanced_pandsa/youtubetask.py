import pandas as pd
you=pd.read_csv('D:\\INvideos.csv')

#Total counts of Records
#print(len(you))

#How many Channels are Listed in data
#print(you.channel_title.nunique())

#channel total count
#print(you.channel_title.value_counts())

#print(len(you.video_id)-you.video_id.nunique())

you.drop_duplicates(subset=['video_id'],keep='last',inplace=True)
# print(len(you))


you['publish_time']=pd.to_datetime(you['publish_time'])
you['trending_date']=pd.to_datetime(you['trending_date'],format='%y.%d.%m')
# print(you.dtypes)

# c=you['publish_time'].str.split('-', expand=True)

# you['count']=you[
#     (you.publish_time.dt.year == 2017) &
#     (you.channel_title == 'T-Series')
# ].sort_values(by='views',ascending=False).head(1)['title']

#print(you.sort_values(by='count' ,ascending=False).head(1))

# you['count']=you.pivot_table(index=you.publish_time.dt.month, values='video_id', aggfunc='count')
# print(you.sort_values(by='count' ,ascending=False).head(1))

you['month']=you.publish_time.dt.month
print(you.groupby('month').agg({'views':'sum'}).sort_values(by='views',ascending=False).head(1))