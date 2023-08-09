from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)
paddle1 = Paddle()
paddle1.setposition(380, 0)

paddle2 = Paddle()
paddle2.setposition(-380, 0)

ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "s")
screen.onkey(paddle2.down, "z")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 340 or ball.distance(paddle2) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # If the collision is missed by the paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()
