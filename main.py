from turtle import Screen
from scoreboard import ScoreBoard
import time
import snake as s
import food as f


screen = Screen()
X_COR = 600
Y_COR = 750
screen.setup(width=X_COR, height=Y_COR)
screen.bgcolor("black")
screen.title("Snake-Game")
# Calling the snake game main function for execution
new_snake = s.MySnake(screen)
head_part = screen.turtles()[0]
snake_body = []
for i in screen.turtles():
    snake_body.append(i)
my_food = f.Food()
scoreboard = ScoreBoard()
game_speed = 0.3

while True:
    if head_part.xcor() >= (X_COR/2) or head_part.xcor() <= -(X_COR/2) \
            or head_part.ycor() >= ((Y_COR/2)-150) or head_part.ycor() <= -((Y_COR/2)-150):
        scoreboard.game_over()
        screen.exitonclick()

    screen.update()
    time.sleep(game_speed)  # Used to make the loop sleep i.e. make snake movement slow

    if head_part.distance(my_food) < 15:    # Checks if the snake head pixel is less that 15 pixel to the food
        my_food.food_collision()            # To randomize the food object again
        new_snake.add_part(snake_body)
        scoreboard.score_increase()

        if game_speed > 0.1:
            game_speed -= 0.1
    else:
        new_snake.snake_movement()

    for body in snake_body:
        if body == head_part:
            pass
        elif head_part.distance(body) < 10:
            scoreboard.game_over()
            screen.exitonclick()


