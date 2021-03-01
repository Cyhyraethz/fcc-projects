class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = list()
    self.balance = 0
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
      self.withdraw(amount, f'Transfer to {name.category}')
      name.deposit(amount, f'Transfer from {self.category}')
      return True
    else:
      return False
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
  chart = 'Percentage spent by category\n'
  percent = 100
  while percent >= 0:
    next_line = f'{percent}| '
    chart += ' ' * (5 - len(next_line)) + next_line
    for percentage in percentages:
      if percentages.get(percentage) >= percent:
        chart += 'o  '
      else:
        chart += '   '
    if percent > 0:
      chart += '\n'
    percent -= 10
  if len(categories) > 0:
    chart += '\n    -' + '-' * (len(percentages) * 3)
    length = 0
    for category in categories:
      if len(category.category) > length:
        length = len(category.category)
    for i in range(length):
      chart += '\n     '
      for category in categories:
        try:
          chart += f'{category.category[i]}  '
        except:
          chart += '   '
  return chart
