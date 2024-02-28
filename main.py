import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.onkey(player.up, "Up")


game_is_on = True

while game_is_on:
  time.sleep(0.1)
  screen.update()
  scoreboard.score_board()  
  car_manager.car()
  car_manager.move() 

  #check if the turtle has reached the finish line
  if player.reach_finish() is True:
    scoreboard.score_increse()
    player.player_reset()

  # Check if the turtle has hit the cars
  for i in car_manager.CARS:
    if i.distance(player) < 15:
      scoreboard.game_over()
      game_is_on = False

 
  
screen.exitonclick()