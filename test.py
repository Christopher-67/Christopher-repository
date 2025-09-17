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
# equal(200)

# sidelength = 100
# rotate = 90
# triangle(100,90)
# def manySquares(x):
#       y = 10
# for i in range(3):
#       square(y)
#       y = y + 5
#       t.left(5)
# manySquares(60)

# def doublesquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
#         t.degrees = length

# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)

# def circleSquare(lenght, sqaureNum):
#     degrees = 5
#     t.speed = 10
#     for i in range(sqaureNum):
#         square(lenght, 90)
#         t.left(degrees)
#         degrees += 5
       

# circleSquare(100,60)

# t.speed(0)
# for i in range(72):  
#     for j in range(4): 
#         t.forward(100)
#         t.left(90)
#     t.left(5) 

# t.speed(0)
# size = 20 
# for i in range(5):
#     for j in range(4):  
#         t.forward(size)
#         t.left(90)
#     size += 20  

t.speed(0)
size = 10 
for i in range(70): 
    for j in range(4):  
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.right(144)
    t.right(10)   
    size += 5  

# t.speed(0)
# size = 5 
# for i in range(80): 
#     for j in range(3): 
#         t.forward(size)
#         t.left(144)
#         t.forward(size)
#         t.left(144)
#         t.forward(size)
#         t.left(144)
#     t.right(65) 
#     size += 5

turtle.done()