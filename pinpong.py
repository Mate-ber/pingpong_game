import turtle
import time
from pinpong_players import Player1
from pinpong_players import Player2
from pinpong_map import Map
from pinpong_ball import Ball
from pinpong_score import Score


window = turtle.Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)


player1 = Player1()
player2 = Player2()
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
    ball_pos = ball.pos_ball()
    ball_x = ball_pos[0]
    ball_y = ball_pos[1]
    if ball.check_ball_wall():
        ball.change_direction(0)
    else:
        player1_pos = player1.get_cor_player1()
        player1_x = player1_pos[0]
        player1_y = player1_pos[1]

        player2_pos = player2.get_cor_player2()
        player2_x = player2_pos[0]
        player2_y = player2_pos[1]

        if ball_x - 10 == player1_x and (70 >= player1_y - ball_y >= 0 or 70 >= ball_y - player1_y >= 0):
            ball.change_direction(1)
        elif ball_x + 10 == player2_x and (70 >= player2_y - ball_y >= 0 or 70 >= ball_y - player2_y >= 0):
            ball.change_direction(1)
    if ball_x > 360:
        score.increase_scorel()
        ball.goto_start()
    elif ball_x < -360:
        score.increase_scorer()
        ball.goto_start()

    ball.move_ball()
    time.sleep(0.05)


window.mainloop()
