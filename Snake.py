from turtle import Turtle, Screen
import time


class MySnake:
    def __init__(self):
        """Setting up the game screen and initial snake body."""
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake-Game")
        # Creating the Snake body
        x_value = 0
        y_value = 0
        self.screen.tracer(1)
        for _ in range(3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.setpos(x_value, y_value)
            x_value -= 20

    def move_left(self):
        """To turn the head part left by 90 angle."""
        self.screen.turtles()[0].left(90)

    def move_right(self):
        """To turn the head part right by 90 angle."""
        self.screen.turtles()[0].right(90)

    def snake_movement(self):
        """Method responsible for snake body movement."""
        self.screen.listen()
        head_part = self.screen.turtles()[0]
        while True:
            if head_part.xcor() >= 300 or head_part.xcor() <= -300 \
                    or head_part.ycor() >= 300 or head_part.ycor() <= -300:
                break
            self.screen.onkeypress(self.move_left, "w")
            self.screen.onkeypress(self.move_right, "s")
            self.screen.update()
            time.sleep(0.1)
            turtle_list = self.screen.turtles()
            for index in range(len(turtle_list) - 1, 0, -1):
                pos_of_next_element = turtle_list[index - 1].pos()
                turtle_list[index].setpos(pos_of_next_element)
            turtle_list[0].forward(20)

        self.screen.bye()

