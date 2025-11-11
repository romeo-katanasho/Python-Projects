from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("green")
my_screen.title("Snake game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

game_is_on = True
score = 0
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        snake.extend()
        scoreboard.update_score(score)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

my_screen.exitonclick()
