#from functools import reduce
emp=open('D:\\clean_emp.csv').readlines()
del emp[0]

def c_m(data):
  team_salaries = {}
  for row in data:
    team_name = row.split(',')[-1].strip()  
    salary = float(row.split(',')[-4].strip())  
    if team_name in team_salaries:
      team_salaries[team_name].append(salary)
    else:
      team_salaries[team_name] = [salary]

  m_sa = {}
  for team, salaries in team_salaries.items():
    m_sa[team] = sum(salaries) / len(salaries)

  return m_sa

# Assuming your CSV data is loaded into a list called 'emp_data'
mean_salaries_by_team = c_m(emp)
print(mean_salaries_by_team)
