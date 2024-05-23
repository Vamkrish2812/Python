# vamsi
n=int(input())
temp=n
rev=0
last_dig=n%10
while(temp!=0):
    r=temp%10
    rev=(rev*10)+r
    temp=temp//10
fir_dig=rev%10
print(f'sum of first digit and last digit of {n} is {last_dig+fir_dig}')