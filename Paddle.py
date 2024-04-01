from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() <= 230:
            self.goto(self.xcor(), self.ycor()+20)

    def down(self):
        if self.ycor() >= -220:
            self.goto(self.xcor(), self.ycor()-20)