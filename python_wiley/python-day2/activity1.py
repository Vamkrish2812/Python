s_cart=['orange','peach','apple','kiwi']
prices={
    'orange':1.5,'apple':2,'peach':3,'kiwi':4.5
}
stock={
    'orange':24,
    'apple':0,
    'peach':10,
    'kiwi':5
}
bill=0
for i in s_cart:
    if stock[i]>0:
        bill+=prices[i]
print(bill)
