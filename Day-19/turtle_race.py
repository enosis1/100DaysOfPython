import random
from turtle import Screen, Turtle


def set_pace(turtle):
    """Sets the pace of a turtle between 0 and 10."""
    return turtle.forward(random.randint(0, 10))


is_racing = True
screen = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen.setup(500, 400)

list_turtles = []
# TURTLE
x = -230
y = -70
for i in range(0, len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setposition(x, y)
    y += 30
    list_turtles.append(new_turtle)


user_choice = screen.textinput(
    "Choose a Turtle", "Out of the rainbow, choose a color of a turtle to root for!"
)

while is_racing:
    for turtle in list_turtles:
        set_pace(turtle)
        if turtle.pos() > (230, 0):
            is_racing = False
            if user_choice == turtle.pencolor():
                print(f"Your turtle: {turtle.pencolor().title()} wins!")
            else:
                print(
                    f"{turtle.pencolor().title()} wins! Your {user_choice.title()} turtle did not win!"
                )

screen.exitonclick()
