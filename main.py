import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.move)
game_is_on = True

car_list = CarManager()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_list.create_car()
    car_list.move_car()

    # Detect collision with cars.
    for car in car_list.all_cars:
        if car.distance(player) <= 23:
            game_is_on = False
            scoreboard.game_over()

    # Increase Level
    if player.ycor() >= 280:
        car_list.increase_speed()
        player.reset_position()
        scoreboard.increase_level()

screen.exitonclick()
