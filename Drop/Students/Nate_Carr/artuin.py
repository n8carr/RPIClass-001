import turtle

window = turtle.Screen()
bubba = turtle.Turtle()

# Draw stem
bubba.color("green","black")
bubba.left(90)
bubba.forward(100)
bubba.right(90)

# Draw center
bubba.color("yellow","yellow")
bubba.begin_fill()
bubba.circle(10)
bubba.end_fill()

# Draw leaves
for i in range(1,100):
    if bubba.color() == ("red","yellow"):
        bubba.color("orange","yellow")
    elif bubba.color() == ("orange","yellow"):
        bubba.color("blue","yellow")
    else:
        bubba.color("red","yellow")
    bubba.left(15)
    bubba.forward(50)
    bubba.left(157)
    bubba.forward(50)

# Hide the turtle
bubba.hideturtle()

# Tidy up window
window.exitonclick()

