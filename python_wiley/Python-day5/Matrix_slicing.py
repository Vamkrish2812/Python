import numpy as np
one_arr=np.arange(1,31)
two_arr=one_arr.reshape(5,6)
# First is row_index next is col index
# print(two_arr[:,3])
# print(two_arr[1,:])

# print(two_arr[1:4,:2])

# print(two_arr[0:4,4:])

# print(two_arr[2:,1:5])

#flatten
flat_arr=two_arr.flatten()
#Negation 
print(flat_arr[~flat_arr%2==0])

print(flat_arr[(flat_arr%7==0) | (flat_arr%9==0)])