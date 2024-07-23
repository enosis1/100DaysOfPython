import random
import turtle as t


def generate_color():
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    return (color[0], color[1], color[2])


def random_movement(turtle):
    directions = [0, 90, 180, 270]
    return turtle.setheading(random.choice(directions))


turtle = t.Turtle()
screen = t.Screen()
turtle.width(10)
screen.colormode(255)
turtle.speed(0)
turtle.hideturtle()

for _ in range(200):
    turtle.pencolor(generate_color())
    turtle.forward(20)
    random_movement(turtle)
