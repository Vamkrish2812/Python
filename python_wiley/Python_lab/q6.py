# vamsi
names=[]
n=int(input())
for i in range(n):
    a=input()
    names.append(a)

names.sort()
for i in names:
    print(i,end=" ")
