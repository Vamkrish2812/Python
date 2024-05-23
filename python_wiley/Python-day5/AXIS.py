import numpy as np
weather_info=[
  #1990 91 92
    [14,18,16],
    [19,13,17],
    [18,21,19],
    [16,22,18]
]

w_arr = np.array(weather_info)
#axis 0 (column)
print('Highest in each year',w_arr.max(axis=0))
print('Highest in each month',w_arr.max(axis=1))
print('lowest temp each year',w_arr.min(axis=0))
#axis 1 (Row)
print('lowest temp each month',w_arr.min(axis=1))