import time
import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

turtle.tracer(0)

s = turtle.Screen()
s.bgcolor("black")
s.setup(800, 600)
s.title("Ping Pong Game")

#Drawing the middle line
t = turtle.Turtle()
t.color("coral")
t.pu()
t.goto((0, -390))
t.hideturtle()
t.setheading(90)
t.pensize(5)
for _ in range(20):
    t.pd()
    t.forward(20)
    t.pu()
    t.forward(20)
t.home()

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-390, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.display_score()

s.listen()

s.onkeypress(left_paddle.up, "w")
s.onkeypress(left_paddle.down, "s")
s.onkeypress(right_paddle.up, "Up")
s.onkeypress(right_paddle.down, "Down")

game = True
while game:
    turtle.update()
    time.sleep(0.02)
    ball.move()

    if abs(ball.ycor()) > 280:
        ball.bounce_from_wall()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -360:
        ball.bounce_from_paddle()

    if ball.xcor() > 380:
        scoreboard.left_score += 1
        scoreboard.display_score()
        ball.refresh()

    if ball.xcor() < -380:
        scoreboard.right_score += 1
        scoreboard.display_score()
        ball.refresh()

    if scoreboard.right_score == 10 or scoreboard.left_score == 10:
        game = False


t.clear()
ball.hideturtle()
if scoreboard.right_score == 10:
    t.write(f"Right Player won", align="center", font=('Times New Roman', 20, 'bold'))
elif scoreboard.left_score == 10:
    t.write(f"Left Player won", align="center", font=('Times New Roman', 20, 'bold'))
turtle.update()

s.exitonclick()
