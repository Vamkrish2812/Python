# vamsi
n=input('Enter the string: ')
b=""
for i in n:
    if(i=='a'):
        b=b+'*'
    else:
        b+=i
print(f'After string modification new string is {b}')