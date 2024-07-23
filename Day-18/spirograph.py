import random
import turtle as t


def generate_color():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return (color[0], color[1], color[2])


tim = t.Turtle()
screen = t.Screen()
screen.colormode(255)
tim.speed(0)

for i in range(90):
    tim.pencolor(generate_color())
    tim.circle(150)
    tim.left(4)


screen.exitonclick()
