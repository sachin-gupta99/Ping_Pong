import turtle
from ball import Ball
from paddle import Paddle

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.setposition((0, 250))
        self.pd()
        self.color("white")
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0

    def display_score(self):
        self.clear()
        self.write(f"{self.left_score}\t\t{self.right_score}", align="center", font=('Times New Roman', 30, 'bold'))
