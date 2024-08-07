from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.reset_position()

    def go_up(self):
        """Moves the turtle going up."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    # Detect if the turtle has reached the top of the screen FINISH_LINE_Y
    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def reset_position(self):
        self.goto(STARTING_POSITION)
