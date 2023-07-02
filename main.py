from turtle import Turtle, Screen
import time

# Setting up the game screen
my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("Snake-Game")


class SnakePart:
    def __init__(self, current_body, current_screen):
        self.current_body = current_body
        self.current_screen = current_screen

    def move_left(self):
        self.current_body[0].left(90)

    def move_right(self):
        """Ti the turtle back by 10 steps"""
        self.current_body[0].right(90)

    def main_movement(self):
        self.current_screen.update()
        time.sleep(0.1)
        for index in range(len(self.current_body) - 1, 0, -1):
            pos_of_next_element = self.current_body[index - 1].pos()
            self.current_body[index].setpos(pos_of_next_element)
            # Another way to do:
            # new_x = self.current_body[index - 1].xcor()
            # new_y = self.current_body[index - 1].ycor()
            # self.current_body[index].goto(new_x, new_y)
        self.current_body[0].forward(20)


def snake_body():
    # Creating the Snake body
    initial_length = 3
    x_value = 0
    y_value = 0
    my_screen.tracer(1)
    for _ in range(initial_length):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.setpos(x_value, y_value)
        x_value -= 20

    my_screen.listen()
    head_part = my_screen.turtles()[0]

    while True:
        if head_part.xcor() >= 300 or head_part.xcor() <= -300 or head_part.ycor() >= 300 or head_part.ycor() <= -300:
            break
        my_snake = SnakePart(my_screen.turtles(), my_screen)
        my_screen.onkeypress(my_snake.move_left, "w")
        my_screen.onkeypress(my_snake.move_right, "s")
        my_snake.main_movement()

    my_screen.bye()


# Calling the snake game main function for execution
snake_body()
