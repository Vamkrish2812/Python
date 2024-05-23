from functools import reduce
n=int(input("Enter the number of player"))
b=[]
if n<=11:
    for i in range(n):
        c=int(input("Enter the score of {} player".format(i+1)))
        b.append(c)
    s=reduce(lambda x,y:x+y ,b)
    print(f'Team score is {s}')
else:
    print(-1)
