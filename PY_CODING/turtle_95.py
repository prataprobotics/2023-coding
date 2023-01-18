import turtle
# Create and customise the screen
window = turtle.Screen()
window.bgcolor('dark salmon')
window.tracer(0)
# Create and customise the turtle
player = turtle.Turtle()
player.shape('turtle')
player.color('turquoise')
player.penup()

# Define the functions to make the turtle turn by the required angle
def turn_left():
    player.color('light green')
    player.left(10)


def turn_right():
    player.color('light blue')
    player.right(10)


# Create the key bindings
window.onkeypress(turn_left, "Left")
window.onkeypress(turn_right, "Right")
window.listen()
# Main loop which makes the turtle move forward contiunously, forever
while True:
    player.forward(0.5)
    window.update()

# turtle.done() This line is no longer needed now there's a while True loop