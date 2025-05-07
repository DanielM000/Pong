from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")

screen.bgpic("images/sonicfeet.png")

spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(6, 1)
spelfigur1.color("white")

screen.exitonclick()