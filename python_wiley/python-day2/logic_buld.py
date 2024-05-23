ride_speed=int(input('Enter speed'))
bir=input('Enter y or N')
if(bir=='Y'):
    if(ride_speed-5>80):
        print('Big ticket')
    elif(ride_speed-5>=60 and ride_speed-5<=80):
        print("Small ticket")
    else:
        print('No ticket')
else:
    if(ride_speed>80):
        print('Big ticket')
    elif(ride_speed>=60 and ride_speed<=80):
        print("Small ticket")
    else:
        print('No ticket')