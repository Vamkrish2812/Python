# print(list(map(lambda x:x*x ,[1,2,3,4])))
# print(set(map(lambda x:x*x ,[1,2,3,4])))
# print(tuple(map(lambda x:x*x ,[1,2,3,4])))
# sal=[5500,8700,9400,4300,8900,4400]
# f=lambda f:f+(0.16*f)

# print(list(map(f,sal)))

# ans=filter(lambda n:n%2==0,[1,3,4,5,6,7,8])
# print(list(ans))

# colors=['red','orange','maroon','indigo','cyan']
# print(list(filter(lambda )))

# garbage=[100,True,200,False,300,'hello']
# print(list(filter(lambda x:type(x)==int,garbage)))
from functools import reduce
scores=[4,1,2,6,5,3,9]
minstock=reduce(lambda x,y: x if x>y else y ,scores)
print(minstock)