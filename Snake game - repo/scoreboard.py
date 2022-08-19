from mimetypes import init
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()
        self.points = 0
        self.write(arg=f"Score: {self.points}", move=False, align="center", font=('Courier', 14, 'normal'))
    
    def score(self):
        self.clear()
        self.points+=1
        self.write(arg=f"Score: {self.points}", move=False, align="center", font=('Courier', 14, 'normal'))

    def  game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game over", move=False, align="center", font=('Courier', 14, 'normal'))

        
    
