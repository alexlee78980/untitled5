from turtle import Turtle, Screen
from pong.paddle import Paddle
from pong.ball import Ball
from pong.scoreboard import ScoreBoard
import time


def pong_start():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("pong")
    screen.tracer(0)

    lpaddle = Paddle(350)
    rpaddle = Paddle(-350)
    scoreboard = ScoreBoard()
    ball = Ball()
    screen.listen()
    screen.onkey(lpaddle.go_up, "Up")
    screen.onkey(lpaddle.go_down, "Down")
    screen.onkey(rpaddle.go_up, "w")
    screen.onkey(rpaddle.go_down, "s")
    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.move_speed)
        if ball.y_pos > 280 or ball.y_pos < -280:
            ball.bounce_y()
        if ball.distance(lpaddle) < 50 and ball.xcor() > 320 or ball.distance(rpaddle) < 50 and ball.xcor() < -320:
            ball.bounce_x()
        if ball.xcor() > 400 or ball.xcor() < -400:
            if ball.xcor() > 400:
                scoreboard.left_scored()
            else:
                scoreboard.right_scored()
            ball.point()
        if scoreboard.l_score == 11 or scoreboard.r_score == 11:
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
            scoreboard.goto(0, -80)
            if scoreboard.l_score == 11:
                scoreboard.write("Left Player wins", align="center", font=("Courier", 40, "normal"))
            if scoreboard.r_score == 11:
                scoreboard.write("Right Player wins", align="center", font=("Courier", 40, "normal"))
            game_is_on = False
    screen.exitonclick()
