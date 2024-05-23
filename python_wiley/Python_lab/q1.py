# Vamsi
a=int(input('Enter four digit number'))
zc=0
ec=0
oc=0
while(a!=0):
    r=a%10
    if(r==0):
        zc+=1
    elif(r%2==0 and r!=0):
        ec+=1
    else:
        oc+=1
    a=a//10
print('No of zeroes {}'.format(zc))
print('No of even digit {}'.format(ec))
print('No of odd digit {}'.format(oc))