import numpy as np
 # 1x+2y=9
 # 3x+4y=24
x=np.array([ [3,6,7],[2,1,8],[1,3,7]])

y=np.array([10,11,22])

# print('Multiplication\n',x*y)
# print('Modulo\n',x%y)
# print('subtraction\n',x-y)
# print('addition\n',x+y)
# print('division\n',x/y)

res=np.linalg.solve(x,y)
print(res)