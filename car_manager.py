from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager:

  def __init__(self):    
    self.CARS = []
    self.car()
    
  
  def car(self):    
    random_chance = random.randint(1, 6)
    if random_chance == 1:
      car = Turtle()
      car.penup()
      car.shape('square')
      car.shapesize(stretch_len=2)
      car.color(random.choice(COLORS))
      random_y = random.randint(-200, 200)
      x_position = 300
      car.goto(x_position, random_y)
      self.CARS.append(car)
    
     

  def move(self):
    for car in self.CARS:      
      car.backward(STARTING_MOVE_DISTANCE)

  
      