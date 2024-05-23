emp=open('D:\\clean_emp.csv').readlines()
#print(emp)
del emp[0]
f=lambda x:sum(1 for i in emp if i.split(',')[-2].strip()=='True')
print(f's_m = {(f(emp)/len(emp))*100}')