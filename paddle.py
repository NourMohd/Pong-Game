from turtle import Turtle
DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(UP)
        self.goto(position)




    def up(self):
        self.setheading(UP)
        self.forward(DISTANCE)

    def down(self):
        self.setheading(DOWN)
        self.forward(DISTANCE)



