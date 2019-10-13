import turtle
import math 

loic = turtle.Turtle()
loic.color ('pink')
loic.pensize(2)
loic.speed(1000000)
loic.shape('turtle')

def shape():
    loic.forward(100)
    loic.right(45)
    loic.forward(100)
    loic.right(135)
    loic.forward(100)
    loic.right(45)
    loic.forward(100)
    loic.right(5)


for i in range (1, 49):
    shape()
loic.forward(300)