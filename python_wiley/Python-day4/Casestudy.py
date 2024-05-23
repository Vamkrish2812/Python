emp=open('D:\\clean_emp.csv').readlines()
#print(emp)
del emp[0]
def find_u_t(data):
  teams = []
  for row in data:
    team_name = row.split(',')[8].strip() 
    if team_name not in teams:
      teams.append(team_name)

  return teams

unique_teams = find_u_t(emp)
print(unique_teams)