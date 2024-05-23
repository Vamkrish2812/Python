import pandas as pd
emp=pd.read_csv('D:\\employee.csv')
#print(emp.Salary.mean())

emp['Start Date']=pd.to_datetime(emp['Start Date'])

emp['Last Login Time']=pd.to_datetime(emp['Last Login Time'])

emp['Senior Management'] =emp['Senior Management'].astype(bool)

print(emp.dtypes)

print(emp.Gender.unique())

print(emp.Team.unique())

print(emp.Gender.value_counts())

nb=emp.Gender.value_counts(normalize=True).plot(kind='pie')

nb.show()