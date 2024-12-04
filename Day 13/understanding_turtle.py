# from turtle import *
from turtle import Turtle, Screen
import random

dan = Turtle()
dan.shape("turtle")
dan.color("purple")
# timmy_the_turtle.forward (100)
# timmy_the_turtle.right(90 )

# for _ in range(4):
#     dan.forward(100)
#     dan.right(90)


# import heroes
# print(heroes.gen())

# for _ in range (15):
#     dan.forward(10)
#     dan.penup()
#     dan.forward(10)
#     dan.pendown()

# for _ in range (3):
#     dan.forward(60)
#     dan.right(120)
#
# dan.color("blue")
#
# for _ in range (4):
#     dan.forward(60)
#     dan.right(90)
#
# dan.color("green")
#
# for _ in range (5):
#     dan.forward(60)
#     dan.right(72)
#
# dan.color("yellow")
#
# for _ in range (6):
#     dan.forward(60)
#     dan.right(60)
#
# dan.color("orange")
#
# for _ in range (7):
#     dan.forward(60)
#     dan.right(51)
#
# dan.color("red")
#
# for _ in range (8):
#     dan.forward(60)
#     dan.right(45)

color = ["lawn green","yellow", "firebrick", "dark magenta","dark slate blue" , "red"]

for sides in range (3, 9):
    for _ in range (sides):
        dan.forward(60)
        dan.right(360/sides)
    dan.color(random.choice(color))









screen = Screen()
screen.exitonclick()


