import numpy as np
weather_info=[
  #1990 91 92
    [14,18,16],
    [19,13,17],
    [18,21,19],
    [16,22,18]
]

w_arr = np.array(weather_info)
#print(w_arr)
print('Rows X cols Count',w_arr.shape)
print('Total elements',w_arr.size)
print('size of each element in bytes',w_arr.itemsize)
print('Total memory occupies',w_arr.nbytes)
print('Data type',w_arr.dtype)
print('no of Dimensions',w_arr.ndim)

print(w_arr[1,0])


