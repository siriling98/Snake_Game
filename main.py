from turtle import Turtle, Screen
import random

screen = Screen()
color = ['red', 'green', 'blue', 'black']


class Snake:
    def __init__(self, my_turtle):
        self.my_turtle = my_turtle

    def move_left(self):
        self.my_turtle.tiltangle(90)

    def move_right(self):
        """Moves the turtle back by 10 steps"""
        self.my_turtle.tiltangle(-90)
        # pass


def start():
    x = 0
    y = 0
    for i in range(4):
        timmy = Turtle(shape='square')
        timmy.penup()
        timmy.shapesize()
        # timmy.color(color[i])
        timmy.setpos(x, y)
        x -= 20

    my_turtles = screen.turtles()
    screen.listen()
    while True:
        for current_turtle in my_turtles:
            current_turtle.forward(1)

        screen.onkeypress(move_left, "w")
        screen.onkeypress(move_right, "s")


start()
screen.exitonclick()
