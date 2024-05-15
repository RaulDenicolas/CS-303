import random

class Car:
  def __init__(self,name):
    self.name = name  
    self.speed = random.randint(60,100)
    self.max_distance = random.randint(450,550)   
  def __str__(self):
    return 'Car ' + str(self.name) + ' Speed: ' + str(self.speed) + ' Max Distance: ' + str(self.max_distance)

class Race:
  def __init__(self):
    self.distance = 500
  def start_race(self,racers):
    self.racer_list = [] 
    for racer in range(0,racers):
      car = Car('Car ' + str(racer))
      self.racer_list.append(car)
      print(Car(racer))
  def get_winner(self):
    winner = 'No Winner'
    for racer in self.racer_list:
      if racer.max_distance > self.distance:
        if winner == 'No Winner':
          winner = racer
        elif racer.speed > winner.speed:
          winner = racer
    return winner.name

def main():
  indy = Race()
  indy.start_race(18)  
  print('Winner:', indy.get_winner())

if __name__=="__main__":
    main()


