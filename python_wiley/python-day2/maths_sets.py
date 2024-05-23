marketingTeam={'rishi','shakeer','vaishnavi','fardeen','prasanna'}
salesTeam={'shakeer','jayashankar','rajendra','fardeen','vamsi'}
# Employees work for both teams
print(marketingTeam.intersection(salesTeam))
print(marketingTeam & salesTeam)
# Employee working for only marketing team
print(marketingTeam-salesTeam)
print(marketingTeam.difference(salesTeam))
# Employees from both teams
print(marketingTeam.union(salesTeam))
print(marketingTeam|salesTeam)
# Employees from both team who works only for their team
print(marketingTeam.symmetric_difference(salesTeam))
print(marketingTeam^salesTeam)

