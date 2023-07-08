from turtle import Turtle, Screen

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class MySnake:
    def __init__(self, current_screen):
        """Setting up the game screen and initial snake body."""
        # Creating the Snake body
        self.screen = current_screen
        x_value = 0
        y_value = 0
        self.screen.tracer(0)    # Used to remove the animation on Turtle when tracer(0)
        self.snake_parts = []    # List to store the snake Turtle objects
        for _ in range(3):
            new_part = Turtle("square")
            new_part.color("white")
            new_part.penup()
            new_part.setpos(x_value, y_value)
            self.snake_parts.append(new_part)
            x_value -= 20

    def move_up(self):
        """To turn the set the heading head part to north."""
        if self.snake_parts[0].heading() != DOWN:
            self.snake_parts[0].setheading(UP)

    def move_down(self):
        """To turn the set the heading head part to south."""
        if self.snake_parts[0].heading() != UP:
            self.snake_parts[0].setheading(DOWN)

    def move_left(self):
        """To turn the set the heading head part to east."""
        if self.snake_parts[0].heading() != RIGHT:
            self.snake_parts[0].setheading(LEFT)

    def move_right(self):
        """To turn the set the heading head part to west."""
        if self.snake_parts[0].heading() != LEFT:
            self.snake_parts[0].setheading(RIGHT)

    def add_part(self):
        new_part = Turtle("square")
        new_part.color("white")
        new_part.penup()
        new_part.setpos(self.snake_parts[-1].pos())
        self.snake_parts.append(new_part)

    def snake_movement(self):
        """Method responsible for snake body movement."""
        self.screen.listen()
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")
        for index in range(len(self.snake_parts) - 1, 0, -1):
            pos_of_next_element = self.snake_parts[index - 1].pos()
            self.snake_parts[index].setpos(pos_of_next_element)
        self.snake_parts[0].forward(20)