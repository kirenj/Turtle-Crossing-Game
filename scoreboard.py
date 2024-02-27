from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard (Turtle):

  def __init__(self):
    super().__init__()
    self.penup()
    self.color('black')
    self.hideturtle()
    
    self.score = 0

  def score_board(self):
    self.clear()
    self.goto(x=-250, y= 260)
    self.write(f"Level: {self.score}", align='center', font=FONT)

  def score_increse(self):
    self.score += 1

  def game_over(self):
      self.clear()
      self.write("GAME OVER", align='center', font=FONT)
    
