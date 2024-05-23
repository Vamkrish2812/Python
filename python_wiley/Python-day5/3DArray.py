import numpy as np
reportcard=[
    [
        [42,39,54],
        [56,87,35],
        [54,65,44]
    ],
    [
        [55,66,92],
        [45,64,88],
        [74,89,69]
    ]
]

reportarr=np.array(reportcard)
# print(reportarr)
# print('Rows X cols Count',reportarr.shape)
# print('Total elements',reportarr.size)
# print('size of each element in bytes',reportarr.itemsize)
# print('Total memory occupies',reportarr.nbytes)
# print('Data type',reportarr.dtype)
# print('no of Dimensions',reportarr.ndim)

# print(reportarr[0,0,0])

# print(reportarr[1,2,1])

# s_m=np.arange(1,11)
# sample=np.zeros((5,5))
# sample1=np.ones((5,5))
# sample2=np.full((5,5),9)
# sample3=np.eye(5,5)
# print(sample3)

x=np.zeros((3,3))
y=np.zeros((3,3))

print(np.hstack((x,y)))
print(np.vstack((x,y)))
