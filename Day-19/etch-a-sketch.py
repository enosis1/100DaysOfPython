from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def look_left():
    tim.left(10)

def look_right():
    tim.right(10)

def clear_screen():
    tim.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(look_left, "a")
screen.onkey(look_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
