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
  def transfer(self, amount, category):
    if self.check_funds(amount):
      for instance in instances:
        if instance.category == category:
          self.withdraw(amount, f'Transfer to {instance.category}')
          instance.deposit(amount, f'Transfer from {self.category}')
          return True
  def check_funds(self, amount):
    if amount > self.balance:
      return False
    else:
      return True



# def create_spend_chart(categories):
#   print(categories)



food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55) #####
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)