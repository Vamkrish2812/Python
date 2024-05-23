# vamsi
basepay=int(input('Enter the basepay '))
if(basepay>=5000):
    hra=(0.15*basepay)
    da=(1.50*basepay)
    print('hra is {}'.format(hra))
    print('DA is {}'.format(da))
    print('grosspay is {}'.format(basepay+hra+da))
else:
    hra=(0.10*basepay)
    da=(1.10*basepay)
    print('hra is {}'.format(hra))
    print('DA is {}'.format(da))
    print('grosspay is {}'.format(basepay+hra+da))
