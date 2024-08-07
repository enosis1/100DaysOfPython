import random
import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player that starts at the bottom of the screen
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Listen for "Up" keypress to move the turtle north
screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = random.randint(1, 6)
    if random_chance == 1:
        car_manager.generate_car()
    car_manager.move()

    # Detect collision with the turtle and the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.at_finish_line():
        player.reset_position()
        scoreboard.increase_score()
        car_manager.increase_speed()

screen.exitonclick()
