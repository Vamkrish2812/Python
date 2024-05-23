import sys
import numpy as np
print(sys.getsizeof(5),'bytes')

distance_travelled=[120,210,140,360,280]
# storing list into array
d_array=np.array(distance_travelled)

print(d_array.itemsize,'bytes')