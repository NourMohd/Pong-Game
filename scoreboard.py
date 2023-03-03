from turtle import Turtle
from paddle import Paddle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def middle_line(self):
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.setheading(270)
        for _ in range(50):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()


    def update_scoreboard(self):
        self.middle_line()
        self.penup()
        self.goto(-80, 220)
        self.write(f"{self.l_score}", False, "center", font=('Arial', 60, 'normal'))
        self.goto(80, 220)
        self.write(f"{self.r_score}", False, "center", font=('Arial', 60, 'normal'))

    def right_scores(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()


    def left_scores(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()



