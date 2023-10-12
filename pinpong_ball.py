import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_dir = 1
        self.y_dir = 1

    def move_ball(self):
        self.goto(self.xcor()+10*self.x_dir, self.ycor()+10*self.y_dir)

    def change_direction(self, wall_paddle):
        if wall_paddle == 0:
            self.y_dir *= -1
        else:
            self.x_dir *= -1

    def check_ball_wall(self):
        if self.ycor() > 290 or self.ycor() < -290:
            return True
        return False

    def goto_start(self):
        self.goto(0, 0)
        self.left(45)
