from turtle import Turtle, Screen

ax = 350
ay = 0

bx = -350
by = 0

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")

screen.bgpic("images/sonicfeet.png")

spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(6, 1)
spelfigur1.color("white")
spelfigur1.penup()
spelfigur1.setposition(ax, ay)
def spelfigur1_up():
    ny_plats1 = spelfigur1.ycor() + 20
    spelfigur1.goto(spelfigur1.xcor(), ny_plats1)
    
def spelfigur1_down():
    ny_plats1 = spelfigur1.ycor() - 20
    spelfigur1.goto(spelfigur1.xcor(), ny_plats1)

spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(6, 1)
spelfigur2.color("white")
spelfigur2.penup()
spelfigur2.setposition(bx, by)
def spelfigur2_up():
    ny_plats2 = spelfigur2.ycor() + 20
    spelfigur2.goto(spelfigur2.xcor(), ny_plats2)
    
def spelfigur2_down():
    ny_plats2 = spelfigur2.ycor() - 20
    spelfigur2.goto(spelfigur2.xcor(), ny_plats2)

bollen = Turtle()
bollen.shape(“circle”)
bollen.color(“white”)


screen.listen()
screen.onkey(spelfigur1_up, "Up")
screen.onkey(spelfigur1_down, "Down")
screen.onkey(spelfigur2_up, "w")
screen.onkey(spelfigur2_down, "s")

screen.exitonclick()
