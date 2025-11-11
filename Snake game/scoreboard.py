from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write("Score = 0 ", move=False, align= "center", font=("Arial", 12, "normal"))

    def update_score(self, score):
        self.clear()
        self.write(f"Score ={score}", move=False, align= "center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))
