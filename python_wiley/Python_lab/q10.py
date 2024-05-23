str=input('Enter the string')
b=""
c=['a','e','i','o','u']
for i in str:
    if(i.lower() not in c):
        b=b+i
print(b)