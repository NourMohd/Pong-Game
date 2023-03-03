from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def collision_with_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1


    def ball_bounce(self):
        self.x_move *= -1


    def replace_the_ball(self):
        self.home()
        self.x_move *= -1




