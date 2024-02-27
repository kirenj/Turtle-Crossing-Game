from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
POSITIONS = [(300, 20), (300, -20), (300, 60), (300, -60)]
# CARS = []


class CarManager:

  def __init__(self):
    # super().__init__()       
    # self.car()
    # self.move()
    self.CARS = []
    self.car()
    
  
  def car(self):
    # global CARS
    # time.sleep(0.5)
    for i in POSITIONS:
      car = Turtle()
      car.penup()
      car.shape('square')
      car.shapesize(stretch_len=2)
      car.color(random.choice(COLORS))
      car.goto(i)
      self.CARS.append(car)
    # self.move()
     

  def move(self):
    for car in self.CARS:
      car.setheading(180)
      car.forward(STARTING_MOVE_DISTANCE)