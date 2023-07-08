from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(r.randint(-14, 14) * 20, r.randint(-14, 14) * 20)
        # self.goto(280, 60)

    def food_collision(self):
        self.goto(r.randint(-14, 14) * 20, r.randint(-14, 14) * 20)