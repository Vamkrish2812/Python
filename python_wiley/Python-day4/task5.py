from functools import reduce
emp=open('D:\\clean_emp.csv').readlines()
del emp[0]
d=[]
for i in emp:
    if(i.split(',')[-1].strip()=='Marketing' and i.split(',')[2].strip()=='Female'):
        d.append(i)
#print(emp)

m=reduce(lambda x,y: x if int(x.split(',')[-4].strip())>int(y.split(',')[-4].strip()) else y ,d)
print(m)
