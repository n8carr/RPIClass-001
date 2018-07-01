import turtle

window = turtle.Screen()
artuin = turtle.Turtle()

# Draw stem
artuin.color("green","black")
artuin.left(90)
artuin.forward(100)
artuin.right(90)

# Draw center
artuin.color("black","black")
artuin.begin_fill()
artuin.circle(10)
artuin.end_fill()

# Draw leaves
for i in range(1,24):
    if artuin.color() == ("red","black"):
        artuin.color("orange","black")
    elif artuin.color() == ("orange","black"):
        artuin.color("yellow","black")
    else:
        artuin.color("red","black")
    artuin.left(15)
    artuin.forward(50)
    artuin.left(157)
    artuin.forward(50)

# Hide the turtle
artuin.hideturtle()

# Tidy up window
window.exitonclick()

