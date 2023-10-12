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
window.listen()
window.onkeypress(player1.change_up, "Up")
window.onkeypress(player1.change_down, "Down")
window.onkeypress(player2.change_up, "w")
window.onkeypress(player2.change_down, "s")

while True:
    window.update()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if ball.check_ball_wall():
        ball.change_direction(0)
    else:
        player1_x = player1.xcor()
        player1_y = player1.ycor()

        player2_x = player2.xcor()
        player2_y = player2.ycor()

        if ball_x - 10 == player1_x and (70 >= player1_y - ball_y >= 0 or 70 >= ball_y - player1_y >= 0):
            ball.change_direction(1)
        elif ball_x + 10 == player2_x and (70 >= player2_y - ball_y >= 0 or 70 >= ball_y - player2_y >= 0):
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
