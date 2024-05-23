# vamsi
n=int(input())
b=[]
for i in range(n):
    title=input("Enter the title: ")
    author=input('Enter the title: ')
    publisher=input('Enter the publisher: ')
    cost=int(input('Enter the cost: '))
    Accesion_number=i
    b.append((title,author,publisher,cost,Accesion_number))
x=input('Enter author name to find book')
for i in b:
    if(i[1]==x):
        print(i)
y=input('Enter publisher name to find book')
for j in b:
    if(i[2]==y):
        print(i)
for k in b:
    if(i[3]>=500):
        print(i)
for l in b:
    print(b)



