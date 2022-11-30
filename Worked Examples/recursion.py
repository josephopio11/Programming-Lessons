from turtle import *

import time

MIN_BRANCH_LEN = 5


def draw_tree(size):
    # time.sleep(0.1)

    if size > MIN_BRANCH_LEN:
        turtle.forward(size)
        turtle.right(30)
        draw_tree(size/1.8)
        turtle.left(50)
        draw_tree(size/1.2)

        turtle.right(20)
        turtle.penup()
        turtle.backward(size)
        turtle.pendown()


turtle = Turtle()

turtle.penup()
turtle.goto(0,-120)
turtle.left(90)
turtle.pendown()
draw_tree(140)
