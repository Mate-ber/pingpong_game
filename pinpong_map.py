import turtle


class Map:
    def __init__(self):
        self.centre = turtle.Turtle()
        self.centre.pencolor("white")
        self.centre.pensize(4)
        self.centre.penup()
        self.centre.goto(0,400)
        self.centre.right(90)
        self.create_centre()

    def create_centre(self):
        for _ in range(50):
            self.centre.forward(10)
            self.centre.penup()
            self.centre.forward(10)
            self.centre.pendown()

