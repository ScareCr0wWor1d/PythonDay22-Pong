from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = 0.01
        self.x = 2
        self.y = 1
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)

    def move(self):
        if self.ycor() >= 290 or self.ycor() <= -285:
            self.bounce_y()
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
        time.sleep(self.speed)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.speed *= 0.9

    def ball_out(self):
        if self.xcor() > 360:
            pass
        elif self.xcor() < 360:
            pass

    def playball(self):
        self.goto(0, 0)
        time.sleep(1)
        self.x *= -1
        self.speed = 0.01
