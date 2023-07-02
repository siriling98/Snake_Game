from turtle import Turtle, Screen
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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
        self.screen.tracer(0)              #Stops the annimation which stops the Rotation of the head snake
        for _ in range(3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.setpos(x_value, y_value)
            x_value -= 20

    def move_left(self):
        """To turn the head part left by 90 angle."""
        if self.screen.turtles()[0].heading() != RIGHT:
            self.screen.turtles()[0].setheading(LEFT)

    def move_right(self):
        """To turn the head part right by 90 angle."""
        if self.screen.turtles()[0].heading() != LEFT:
            self.screen.turtles()[0].setheading(RIGHT)

    def move_up(self):
        """To turn the head part right by 90 angle."""
        if self.screen.turtles()[0].heading() != DOWN:
            self.screen.turtles()[0].setheading(UP)

    def move_down(self):
        """To turn the head part right by 90 angle."""
        if self.screen.turtles()[0].heading() != UP:
            self.screen.turtles()[0].setheading(DOWN)

    def snake_movement(self):
        """Method responsible for snake body movement."""
        self.screen.listen()
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        head_part = self.screen.turtles()[0]
        while True:
            if head_part.xcor() >= 300 or head_part.xcor() <= -300 \
                    or head_part.ycor() >= 300 or head_part.ycor() <= -300:
                print("You lost 🐍")
                break
            self.screen.update()
            time.sleep(0.3)      #Puts a delay in the for loop output
            turtle_list = self.screen.turtles()
            for index in range(len(turtle_list) - 1, 0, -1):
                pos_of_next_element = turtle_list[index - 1].pos()
                turtle_list[index].setpos(pos_of_next_element)
            turtle_list[0].forward(20)

        self.screen.bye()

