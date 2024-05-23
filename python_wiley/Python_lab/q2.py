# vamsi
n=int(input())
b=[]
for i in range(n):
    a=int(input())
    b.append(a)
b.sort()
print(f'Min number is {b[0]} and max is {b[-1]}')