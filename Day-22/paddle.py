from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        """Creates the paddle."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)
        self.points = 0

    def go_up(self):
        """make the paddle go up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """make the paddle go up"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

