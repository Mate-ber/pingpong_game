import turtle


class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.penup()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.speed(0)
        self.ball.left(45)
        self.x_dir = 1
        self.y_dir = 1

    def move_ball(self):
        x = self.ball.xcor()
        y = self.ball.ycor()
        self.ball.goto(x+10*self.x_dir, y+10*self.y_dir)

    def change_direction(self, wall_paddle):
        if wall_paddle == 0:
            self.y_dir *= -1
        else:
            self.x_dir *= -1

    def check_ball_wall(self):
        y = self.ball.ycor()
        if y > 290 or y < -290:
            return True
        return False

    def pos_ball(self):
        return self.ball.xcor(), self.ball.ycor()

    def goto_start(self):
        self.ball.goto(0, 0)
        self.ball.left(45)
