import time
import numpy as np

size=1000000

l1=range(size)
l2=range(size)

A1=np.arange(size)
A2=np.arange(size)

start=time.time()
result=[x+y for x,y in zip(l1,l2)]
stop=time.time()

print('Python took ',(stop-start)*1000, 'ms')

start=time.time()
result=A1+A2
stop=time.time()

print((stop-start)*1000)