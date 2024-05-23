import numpy as np
distance_travelled=[120,210,140,360,280]
# storing list into array
d_array=np.array(distance_travelled)
print('Longest_distance',d_array.max())
print('shortest_distance',d_array.min())
print('Total_distance',d_array.sum())
print('Avg_distance',d_array.mean())
# It is a function of np
print('median_distance',np.median(d_array))
print('standard_deviation',d_array.std())
# Vectorization
s=list(map(lambda e:e/2,distance_travelled))
print(s)
print(d_array/2)



