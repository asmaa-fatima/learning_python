from turtle import Turtle, Screen
import random

dan = Turtle()
screen = Screen()
screen.colormode(255)
# color = ["lawn green","yellow", "firebrick", "dark magenta","dark slate blue" , "red"]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

angles = [90,180,270,360]
dan.width(10)

dan.speed(10)

for _ in range (500):
    dan.forward(20)
    dan.setheading(random.choice(angles))
    dan.color(random_color())








screen.exitonclick()