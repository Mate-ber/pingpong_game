import turtle
import time
from pinpong_players import Player
from pinpong_map import Map
from pinpong_ball import Ball
from pinpong_score import Score


window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


player1 = Player(-360)
player2 = Player(360)
_map = Map()
ball = Ball()
score = Score()
# window.listen()
# window.onkeypress(player1.change_up, "w")
# window.onkeypress(player1.change_down, "s")

while True:
    window.update()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if abs(player2.ycor() - ball_y) > 60:
        if player2.ycor() > ball_y:
            player2.change_Ai(-1)
        else:
            player2.change_Ai(1)
    if abs(player1.ycor() - ball_y) > 60:
        if player1.ycor() > ball_y:
            player1.change_Ai(-1)
        else:
            player1.change_Ai(1)

    if ball.check_ball_wall():
        ball.change_direction(0)
    else:
        if ball_x - 10 == player1.xcor() and (70 >= player1.ycor() - ball_y >= 0 or 70 >= ball_y - player1.ycor() >= 0):
            ball.change_direction(1)
        elif ball_x + 10 == player2.xcor() and (70 >= player2.ycor() - ball_y >= 0 or 70 >= ball_y - player2.ycor() >= 0):
            ball.change_direction(1)
    if ball_x > 370:
        score.increase_scorel()
        ball.goto_start()
    elif ball_x < -370:
        score.increase_scorer()
        ball.goto_start()

    ball.move_ball()
    time.sleep(0.05)


window.mainloop()
