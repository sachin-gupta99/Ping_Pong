import turtle


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.pu()
        self.speed(10)
        self.value = 6
        self.move_x = self.value
        self.move_y = self.value
        self.move()

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.move_y *= -1

    def bounce_from_paddle(self):
        self.move_x *= -1

    def refresh(self):
        self.goto(0, 0)
        self.move_x *= -1
        # self.move_y *= -1
