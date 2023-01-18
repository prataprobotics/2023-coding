
#https://www.geeksforgeeks.org/turtle-programming-python/

# Python program to draw square
# using Turtle Programming
import turtle

skk = turtle.Turtle()

player = turtle.Turtle()
player.shape('turtle')
player.color('turquoise')

for i in range(4):
    player.forward(100)
    player.right(90)

turtle.done()
