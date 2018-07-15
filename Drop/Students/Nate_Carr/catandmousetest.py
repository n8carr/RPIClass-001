import turtle
import time

boxsize = 200
caught = False
score = 0



def up():
    # tells mouse to go forward
    mouse.forward(10)
    checkbound()

def back():
    # tells mouse to go backward
    mouse.backward(10)
    checkbound()

def left():
    # tells mouse to turn left
    mouse.left(45)


def right():
    # tells mouse to turn right
    mouse.right(45)

def quitTurtles():
    window.bye()


def checkbound():
    #stop the mouse from leaving square, set by box size
    global boxsize
    if mouse.xcor() > boxsize:
        mouse.goto(boxsize, mouse.ycor())
    if mouse.xcor() < -boxsize:
        mouse.goto(-boxsize, mouse.ycor())
    if mouse.ycor() > boxsize:
        mouse.goto(mouse.xcor(), boxsize)
    if mouse.ycor() < -boxsize:
        mouse.goto(mouse.xcor(), -boxsize)

# screen setup
window = turtle.Screen()
mouse = turtle.Turtle()
cat = turtle.Turtle()
mouse.penup()
mouse.penup()
mouse.goto(100,100)

# key listener
window.onkey(up, "w")
window.onkey(left, "a")
window.onkey(back, "s")
window.onkey(right, "d")
window.onkey(quitTurtles, "Escape")

# set difficulty
difficulty = window.numinput("Difficulty", "Enter a difficulty from easy (1) to hard(5) ", minval=1, maxval=5)

# now script starts listening to our commands
window.listen()

#main loop
while not caught:
    cat.setheading(cat.towards(mouse))
    



