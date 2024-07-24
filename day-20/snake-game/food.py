import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        """Food!!"""
        super().__init__()
        self.shape("circle")
        self.food = Turtle()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Reset food position when snake collides with food"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
