# vamsi
n=int(input())
temp=n
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print(f'Sum of digits of {temp} is {sum}')
