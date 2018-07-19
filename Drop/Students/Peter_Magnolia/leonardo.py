import turtle
window = turtle.Screen()
leonardo = turtle.Turtle()
leonardo.left(90)
leonardo.forward(100)
leonardo.right(90)
leonardo.circle(10)
for i in range(1,24):
    leonardo.left(15)
    leonardo.forward(50)
    leonardo.left(157)
    leonardo.forward(50)
window.exitonclick()
