import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()



screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  scoreboard.score_board()  
  # car_manager.car()
  car_manager.move()
  
    
  

  #check if the turtle has reached the finish line
  if player.reach_finish() is True:
    scoreboard.score_increse()
    player.player_reset()


screen.exitonclick()