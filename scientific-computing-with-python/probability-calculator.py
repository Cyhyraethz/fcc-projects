import random
import copy

class Hat:
  def __init__(self, **balls):
    self.contents = list()
    for color, quantity in balls.items():
      for i in range(quantity):
        self.contents.append(color)
  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      return self.contents
    else:
      result = list()
      content = self.contents[:]
      for i in range(num_balls):
        index = random.choice(range(len(self.contents)))
        result.append(self.contents[index])
        del self.contents[index]
      return result

def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
  num_expected_draws = 0
  for i in range(num_experiments):
    expected = True
    copied_hat = copy.deepcopy(hat)
    balls_drawn = copied_hat.draw(num_balls_drawn)
    for ball in expected_balls:
      if balls_drawn.count(ball) < expected_balls.get(ball):
        expected = False
    if expected == True:
      num_expected_draws += 1
  return num_expected_draws / num_experiments
