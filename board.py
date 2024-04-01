from turtle import Turtle
FONT = ('consolas', 50, 'bold')
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.drawline()
        self.updatesb(0, 0)

    def updatesb(self, pts1, pts2):
        self.clear()
        self.goto(-50, 220)
        self.write(pts2, font=FONT, align=ALIGN)
        self.goto(50, 220)
        self.write(pts1, font=FONT, align=ALIGN)

    def game_over(self, joueur):
        self.goto(0, -50)
        self.color('red')
        self.write("Game Over", font=FONT, align=ALIGN)
        self.goto(0, 50)
        self.write(f"Player {joueur} gagne", font=FONT, align=ALIGN)

    def drawline(self):
        self.goto(0, -280)
        self.left(90)
        self.pensize(10)
        for i in range(10):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
