import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# turnoff tracer
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_pressed = False


def display_for_game_start():
    turtle.hideturtle()
    turtle.color("white")
    turtle.write(f"Press [space] to continue or [q] exit", align="center", font=("Arial", 16, "normal"))


def game_stop():
    turtle.bye()


def key_pressed():
    global is_pressed
    is_pressed = False
    game_start()


def game_start():
    turtle.clear()
    global is_pressed
    game_on = True
    while game_on:
        if is_pressed:
            break
        screen.update()
        # for delaying
        time.sleep(0.1)
        snake.move()

        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            scoreboard.reset()
            snake.reset()
            display_for_game_start()
            is_pressed = True
            break

        # head colliding the body
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                scoreboard.reset()
                snake.reset()
                display_for_game_start()
                is_pressed = True
                break


display_for_game_start()
screen.onkey(key_pressed, "space")
screen.onkey(game_stop, "q")
screen.listen()

turtle.mainloop()
