import turtle
from turtle import *
t = Turtle()


t.shape('turtle')

# """ t.forward(200)

# def message(input):
#      print(input)
# message("Hello Class")

# def square(x):
#      t.forward(x)
#      t.left(90)
#      t.forward(x)
#      t.left(90) 
#      t.forward(x)
#      t.left(90)
#      t.forward(x)
#      t.left(90)
# square(200)

# def equal(x):
#      t.forward(x)
#      t.left(120)
#      t.forward(x)
#      t.left(120)
#      t.forward(x)
# equal(200)

# def right():
#      t.forward(100)
#      t.left(90)
#      t.forward(100)
#      t.left(135)
#      t,forward(142)
# right()

# def rectangle(x):
#      t.forward(100)
#      t.left(90)
#      t.forward(125)
#      t.left(90) 
#      t.forward(100)
#      t.left(90)
#      t.forward(125)
#      t.left(90)
# rectangle(300)

# def equal(x):
#      t.forward(x)
#      t.left(90)
#      t.forward(x)
#      t.left(90)
#      t.forward(x)
# equal(200) """

# sidelength = 100
# rotate = 90
# def square(x,y):
#  for i in range(4):
#      t.forward(x)
#      t.left(y)
# triangle(100,90)
# def manySquares(x):
#       y = 10
# for i in range(3):
#       square(y)
#       y = y + 5
#       t.left(5)
# manySquares(60)

def doublesquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doublesquares(5)

turtle.done()