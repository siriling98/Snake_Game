from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.write(f"Score = {self.score} 🐢", align="center", font=('Courier', 24, 'normal'))

    def score_increase(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER! 🐍", align="center", font=('Courier', 24, 'normal'))
        self.goto(0, -30)
        self.write(f"Click anywhere on the screen to exit.", align="center", font=('Courier', 8, 'normal'))
