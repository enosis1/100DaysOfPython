import random
from turtle import Screen, Turtle

timmy = Turtle()
screen = Screen()
screen.colormode(255)


def draw_shape(sides):
    timmy.pencolor(generate_color())
    for _ in range(sides):
        timmy.forward(100)
        timmy.left(current_side)


def generate_color():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return (color[0], color[1], color[2])


sides = 3
while sides < 11:
    current_side = 360 / sides
    if screen.colormode() == 255:
        draw_shape(sides)
    sides += 1


screen.exitonclick()
