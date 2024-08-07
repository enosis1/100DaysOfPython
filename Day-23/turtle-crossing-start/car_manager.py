import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # Create cars that are 20px high by 40px wide that are randomly generated along the y-axis

    # No cars should be generated in the top and bottom 50px of the screen
    def generate_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        random_y = random.randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)

    # If player has reached the top of the screen increase the speed of the cars
    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
