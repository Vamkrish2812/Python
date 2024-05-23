# ##while _demo
# import time
# meter=1
# while(meter<=10):
#     print('Now meter is at {}'.format(meter))
#     meter=meter+1
#     time.sleep(1)

import random
cc=random.randint(1,20)
for i in range(6):
    a=int(input("Enter a number to guess: "))
    if(a==cc):
        print("Gotcha! you guessed it right")
        break
    elif(a<cc):
        print("your guess is too Low")
    else:
        print("your guess is too high")
else:
    print('Try later')

