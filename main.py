import turtle as t
import Paddle
import ball
import board

PTSMAX = 7

pts1 = 0
pts2 = 0


ecran = t.Screen()
ecran.setup(800, 600)
ecran.bgcolor('black')
ecran.title("Pong")
ecran.tracer(0)

ligne = t.Turtle()
ligne.penup()
ligne.color("white")
ligne.pensize(5)
ligne.left(90)
ligne.goto(0, -300)
for i in range(-350, 300, 40):
    ligne.pendown()
    ligne.forward(20)
    ligne.penup()
    ligne.forward(20)

paddleR = Paddle.Paddle((350, 0))
paddleL = Paddle.Paddle((-350, 0))
balle = ball.Ball()
tableau = board.Scoreboard()

t.listen()

t.onkeypress(paddleR.up, 'Up')
t.onkeypress(paddleR.down, 'Down')
t.onkeypress(paddleL.up, 'w')
t.onkeypress(paddleL.down, 's')

game_on = True

while game_on:
    ecran.update()
    balle.move()
    if balle.distance(paddleR) < 50 and balle.xcor() > 335:
        balle.bounce_x()
    if balle.distance(paddleL) < 50 and balle.xcor() < -335:
        balle.bounce_x()
    if balle.xcor() > 380:
        balle.playball()
        pts2 += 1
    elif balle.xcor() < -380:
        balle.playball()
        pts1 += 1
    tableau.updatesb(pts1, pts2)
    if pts1 == PTSMAX:
        tableau.game_over(1)
        game_on = False
    elif pts2 == PTSMAX:
        tableau.game_over(2)
        game_on = False

ecran.exitonclick()
