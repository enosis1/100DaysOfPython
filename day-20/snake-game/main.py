import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# TODO: Create a snake body
snake = Snake()
# TODO: Move the snake

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail


screen.exitonclick()
