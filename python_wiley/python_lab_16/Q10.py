from functools import reduce
n=input('Enter number').split(',')
c=""
for i in n:
    c+=i
r=int(c)
count=0
temp=r
for i in c:
    if temp%int(i)==0:
        count+=1
if(count==len(c)):
    print("Happy number")
else:
    print("sad number")