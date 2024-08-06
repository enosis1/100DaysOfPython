import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(paddle_r) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_l) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Detect if ball goes past paddle
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < -380:
        scoreboard.r_point()

        ball.reset_ball()

screen.exitonclick()
