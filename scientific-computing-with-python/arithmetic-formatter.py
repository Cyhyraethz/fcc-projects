import re

def arithmetic_arranger(problems, display='False'):
  split_problems = [] # list of individual components of each problem
  joined_problems = ['', '', '', '', ''] # list of combined components from each problem
  if len(problems) > 5:
    return 'Error: Too many problems.' # error message
  for i in problems:
    i = i.split(' ') # break down each problem into individual components (e.g. operands, operators, dashed line)
    if re.fullmatch('[+-]', i[1]) == None:
      return "Error: Operator must be '+' or '-'." # error message
    if re.fullmatch('\d+', i[0]) == None or re.fullmatch('\d+', i[2]) == None:
      return 'Error: Numbers must only contain digits.' # error message
    if len(i[0]) > 4 or len(i[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.' # error message
    if len(i[0]) >= len(i[2]):
      i.append('-' * (len(i[0]) + 2)) # add dashes to split problems
    elif len(i[0]) < len(i[2]):
      i.append('-' * (len(i[2]) + 2)) # add dashes to split problems
    if i[1] == '+':
      i.append(str(int(i[0]) + int(i[2]))) # add answer to split problems
    elif i[1] == '-':
      i.append(str(int(i[0]) - int(i[2]))) # add answer to split problems
    split_problems.append(i)
  for problem in split_problems: # right align the individual components of each problem by adding whitespace
    problem[1] = problem[1] + ' ' * (len(problem[3]) - len(problem[1]) - len(problem[2])) + problem[2] # combine operator and second operand
    problem[0] = ' ' * (len(problem[3]) - len(problem[0])) + problem[0]
    problem[4] = ' ' * (len(problem[3]) - len(problem[4])) + problem[4]
    for i in range(5): # combine all the individual components from each problem, separated by four spaces
      joined_problems[i] += problem[i]
      joined_problems[i] += '    '
  for i in range(len(joined_problems)):
    joined_problems[i] = joined_problems[i][:-4] # remove excess whitespace from end of combined components
  if display == True: # arrange problems with answers shown
    arranged_problems = f'''{joined_problems[0]}
{joined_problems[1]}
{joined_problems[3]}
{joined_problems[4]}'''
  else: # arrange problems with answers hidden
    arranged_problems = f'''{joined_problems[0]}
{joined_problems[1]}
{joined_problems[3]}'''
  return arranged_problems

print('\nTrue')
print(arithmetic_arranger(['32 + 8', '1 - 3801', '99 + 99', '523 - 49'], True))
print('\nFalse')
print(arithmetic_arranger(['32 + 8', '1 - 3801', '99 + 99', '523 - 49']), '\n')
