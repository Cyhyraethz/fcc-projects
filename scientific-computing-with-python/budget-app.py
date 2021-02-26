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



# def create_spend_chart(categories):
#   print(categories)



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

print(food)
