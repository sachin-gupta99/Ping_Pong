import turtle


class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("light green")
        self.shape("square")
        self.setheading(90)
        self.shapesize(1.0, 4.0, 1.0)
        self.pu()
        self.goto(position)

    def up(self):
        if self.ycor() > 250:
            return
        self.forward(20)

    def down(self):
        if self.ycor() < -240:
            return
        self.back(20)
