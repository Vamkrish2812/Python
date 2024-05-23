from functools import reduce
emp=open('D:\\clean_emp.csv').readlines()
del emp[0]
def count_employees_by_team(data):
  """Counts the number of employees in each team in the CSV data.

  Args:
      data: A list of lists, where each inner list represents a row in the CSV data.

  Returns:
      A dictionary with team names as keys and the number of employees in each team as values.
  """

  team_counts = {}
  for row in data[0:]:  # Skip the header row
    team_name = row.split(',')[-1].strip()  # Replace COLUMN_INDEX with the team name column index
    if team_name in team_counts:
      team_counts[team_name] += 1
    else:
      team_counts[team_name] = 1

  return team_counts

# Assuming your CSV data is loaded into a list called 'emp_data'
team_wise_counts = count_employees_by_team(emp)
print(team_wise_counts)