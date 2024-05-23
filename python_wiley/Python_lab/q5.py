# vamsi
cust=[]
for i in range(2):
    account_number=input('Enter your account number')
    name=input('Enter the name')
    balance=int(input('Enter balance'))
    cust.append((account_number,name,balance))
def less_100(cust_details):
    for i in cust_details:
        if(i[2]<100):
            print(f'acc_no {i[0]} name {i[1]} balance {i[2]}')
 

print(less_100(cust))