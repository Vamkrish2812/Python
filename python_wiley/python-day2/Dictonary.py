# lang={'en':'english','hi':'hindi','fr':'french'}
# print(lang)
usa={}
usa['Ar']='Arkansas'
usa['Tx']='Texas'
usa['Al']='Alabama'
usa.update({'Ca': 'California','Il':'Illinois', 'Hi':'Hawai'})
print(usa)
# del
del usa['Il']
print(usa['Tx'])
print(usa.get('Txx','Oops!Key not found'))
print(usa.keys())
print(usa.items())
for key in usa:
    print(key , usa[key])
for k,v in usa.items():
    print(k,v)