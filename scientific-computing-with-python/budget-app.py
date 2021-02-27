instances = list()

class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = list()
    self.balance = 0
    instances.append(self)
  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})
    self.balance += amount
  def withdraw(self, amount, description=''):
    if self.check_funds(amount):
      self.ledger.append({'amount': -amount, 'description': description})
      self.balance -= amount
      return True
    else:
      return False
  def get_balance(self):
    return self.balance
  def transfer(self, amount, name):
    if self.check_funds(amount):
      for instance in instances:
        if instance.category == name.category:
          self.withdraw(amount, f'Transfer to {instance.category}')
          instance.deposit(amount, f'Transfer from {self.category}')
          return True
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True
  def __str__(self):
    def add_decimals(string):
      if '.' not in string:
        string += '.00'
      else:
        index = string.index('.')
        decimals = len(string[index + 1:])
        if decimals < 2:
          string += '0'
      return string
    total = 0
    output = ''
    length = int(((30 - len(self.category)) / 2))
    title = '*' * length + self.category + '*' * length
    if len(title) < 30:
      title += '*'
    output += title
    for entry in self.ledger:
      amount_string = add_decimals(str(entry['amount']))
      spaces = 30 - len(entry['description'][:23]) - len(amount_string)
      output += '\n' + entry['description'][:23] + ' ' * spaces + amount_string
      total += entry['amount']
    total_string = add_decimals(str(total))
    output += '\n' + 'Total: ' + total_string
    return output



def create_spend_chart(categories):
  spent = dict()
  total_spent = 0
  percentages = dict()
  for category in categories:
    if category.category not in spent:
      spent[category.category] = 0
    for entry in category.ledger:
      if entry['amount'] < 0:
        spent[category.category] -= entry['amount']
        total_spent -= entry['amount']
        spent[category.category] = round(spent[category.category], 2)
        total_spent = round(total_spent, 2)
  for category in categories:
    percentages[category.category] = int(spent[category.category] / total_spent * 10) * 10
  chart = 'percentages spent by category\n'
  percent = 100
  while percent >= 0:
    next_line = f'{percent}| '
    chart += ' ' * (5 - len(next_line)) + next_line
    for percentage in percentages:
      if percentages.get(percentage) >= percent:
        chart += 'o  '
    if percent > 0:
      chart += '\n'
    percent -= 10
  if len(percentages) > 0:
    chart += '\n    -'
  chart += '-' * (len(percentages) * 3)
  example_chart = '''Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g'''
  return chart


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(create_spend_chart([food, clothing, auto]))
