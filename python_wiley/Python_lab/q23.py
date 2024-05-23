# vamsi
print('1.Calculate length of string')
print('2.Reverse a given string')
print('3.Concatenation of one string to another')
print('4.Copy one String into another')
print('5.Compare two string.')
n=int(input('Enter the option to perform operation: '))
str=input('Enter the string to perform operation: ')
if(n==1):
    print(f'length of string {str} is {len(str)}')
elif(n==2):
    c=""
    for i in range(len(str)):
        c+=str[len(str)-1-i]
    print(c)
elif(n==3):
    z=input('Enter the string to be concatenated')
    print(f'concatenation of two strings {str} and {z} is {str+z}')
elif(n==4):
    x=""
    for i in str:
        x=x.join(i)
    print(f'String {str} is copied into {x}')
else:
    v=input('Enter the string to be compared: ')
    if(str==v):
        print('Enter string is same of original string')
    
    