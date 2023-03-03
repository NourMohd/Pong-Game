from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


difficulty = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(difficulty)

    ##Collision with wall
    ball.collision_with_wall()

    ##Collision with the paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 330:
        ball.ball_bounce()
        difficulty *= 0.9
    if ball.distance(l_paddle) <= 50 and ball.xcor() < -330:
        ball.ball_bounce()
        difficulty *= 0.9

    ##miss the ball by the right paddle
    if ball.xcor() > 360:
        ball.replace_the_ball()
        scoreboard.left_scores()

    ##miss the ball by the left paddle
    if ball.xcor() < -360:
        ball.replace_the_ball()
        scoreboard.right_scores()


    ball.move()


screen.exitonclick()


