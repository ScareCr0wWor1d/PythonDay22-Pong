from turtle import Turtle
FONT = ('consolas', 50, 'bold')
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.updatesb(0,0)

    def updatesb(self, pts1, pts2):
        self.clear()
        self.goto(-50, 220)
        self.write(pts2, font=FONT, align=ALIGN)
        self.goto(50, 220)
        self.write(pts1, font=FONT, align=ALIGN)
    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("Game Over", font=FONT, align='center')

    def addpts(self):
        self.point1 += 1
        self.clear()
        self.updatesb()
