import turtle
import random


class Player(turtle.Turtle):
    def __init__(self,xxcor):
        super().__init__()
        self.xxcor = xxcor
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.xxcor, 0)

    def change_up(self):
        if self.ycor() + 20 < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def change_down(self):
        if self.ycor() - 20 > -250:
            self.goto(self.xcor(), self.ycor() - 20)

    def change_Ai(self, piv):
        self.goto(self.xcor(), self.ycor() + (random.randint(1, 25) * piv))

