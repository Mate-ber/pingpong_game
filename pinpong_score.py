import turtle


class Score:
    def __init__(self):
        self.score_l = 0
        self.score_r = 0
        self.title = turtle.Turtle()
        self.title.color("white")
        self.title.speed(0)
        self.title.hideturtle()
        self.title.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.title.clear()
        self.title.write(f"Player1: {self.score_l}  Player2:{self.score_r}", align="center", font=("Courier", 24, "normal"))

    def increase_scorel(self):
        self.score_l += 1
        self.update_score()

    def increase_scorer(self):
        self.score_r +=1
        self.update_score()
