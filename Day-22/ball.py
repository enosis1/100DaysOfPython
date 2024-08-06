from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.width(20)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        """Moves the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bouces the ball"""
        self.y_move *= -1

    def bounce_x(self):
        """Bouces the ball"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_ball(self):
        """Reset the ball"""
        self.goto(0, 0)
        self.bounce_x()
        self.ball_speed = 0.1
