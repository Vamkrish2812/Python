import numpy as np
# heights=[
#     [160,162,158,164],
#     [155,157,159,161],
#     [170,172,168,171],
#     [165,167,169,166]
# ]

# hei=np.array(heights)

# print(hei.mean(axis=1))

a=np.array([5,7,9,8,6,4,5])
b=np.array([6,3,4,8,9,7,1])
# print(np.maximum(a,b))

# x=[]
# def max(a,b):
#     for i in range(len(a)):
#         if a[i]>b[i]:
#             x.append(a[i])
#         else:
#             x.append(b[i])
#     return x
# print(max(a,b))

z=[]

max=lambda x,y:[x[i] if x[i]>y[i] else y[i] for i in range(len(x))]
# arr[arr%2!=0]=-1
#print(np.setdiff1d(a, b))
print(max(a,b))