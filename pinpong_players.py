import turtle


class Player:
    def __init__(self,xxcor):
        self.xxcor = xxcor
        self.segments = []
        self.create_player()
        self.head = self.segments[0]
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.player_heading = -1

    def create_player(self):
        positions = [(self.xxcor, 0), (self.xxcor, 20), (self.xxcor, -20), (self.xxcor, 40), (self.xxcor, -40)]
        for i in range(5):
            segment = turtle.Turtle()
            segment.speed(0)
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(positions[i][0], positions[i][1])
            self.segments.append(segment)
        self.head = self.segments[0]

    def change_up(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(x, y+20)

    def change_down(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y - 40)
        x = self.head.xcor()
        y = self.head.ycor()
        self.head.goto(x, y-20)

    def get_cor_player(self):
        return self.head.xcor(), self.head.ycor()

