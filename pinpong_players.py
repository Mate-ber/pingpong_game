import turtle


class Player1:
    def __init__(self):
        self.segments = []
        self.create_player1()
        self.head = self.segments[0]
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.player1_heading = -1

    def create_player1(self):
        positions = [(-360, 0), (-360, 20), (-360, -20), (-360, 40), (-360, -40)]
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

    def get_cor_player1(self):
        return self.head.xcor(), self.head.ycor()


class Player2:
    def __init__(self):
        self.segments = []
        self.create_player2()
        self.head = self.segments[0]
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.player2_heading = -1

    def create_player2(self):
        positions = [(360, 0), (360, 20), (360, -20), (360, 40), (360, -40)]
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

    def get_cor_player2(self):
        return self.head.xcor(), self.head.ycor()
