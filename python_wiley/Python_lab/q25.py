#vamsi
n=input()
num=[1,2,3,4,5,6,7,8,9,0]
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
if(int(n) in num):
    print('It is a digit')
elif(n.lower() in alp):
    print('It is a alphabet')
else:
    print('Others')