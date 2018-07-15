import turtle

window = turtle.Screen()
bubba = turtle.Turtle()

# Draw stem
bubba.color("green","black")
bubba.left(90)
bubba.forward(100)
bubba.right(90)

# Draw center
bubba.color("black","black")
bubba.begin_fill()
bubba.circle(10)
bubba.end_fill()

# Draw leaves
for i in range(1,24):
    if bubba.color() == ("red","black"):
        bubba.color("orange","black")
    elif bubba.color() == ("orange","black"):
        bubba.color("blue","black")
    else:
        bubba.color("red","black")
    bubba.left(15)
    bubba.forward(50)
    bubba.left(157)
    bubba.forward(50)

# Hide the turtle
bubba.hideturtle()

# Tidy up window
window.exitonclick()

