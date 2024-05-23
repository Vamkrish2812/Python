google=open('D:\\google_stock_price.csv').readlines()
del google[0]
# print(len(google))

# from functools import reduce
gstock=list(map(float,google))
# #print(gstock[5])
# print(reduce(lambda x,y: x if x>y else y,gstock))
# print(reduce(lambda x,y: x if x<y else y,gstock))
# gstock.sort()
# midindex=len(gstock)//2
# median=(gstock[midindex-1]+gstock[midindex])/2
# print(median)

n=list(filter(lambda x:x>500,gstock))
print('excellent:',len(n))
r=list(filter(lambda x:x<=500 and x>=220,gstock))
print('satisfactory:',len(r))
y=list(filter(lambda x:x<220,gstock))
print('ok:',len(y))

