import turtle               # import the turtle library
window = turtle.Screen()    # create a window
bubba = turtle.Turtle()     # create bubba var that is an instance of turtle

# set direction you want turtle to run, turn left, 90 degrees...
# start direcion is center screen, pointed to the right...
bubba.left(90)

bubba.forward(100)          # set length you want bubba to run, 100pts
bubba.right(90)             # change direction right, 90 degrees
bubba.circle(10)            # draw a circle 10pts wide.


for i in range(1,24):
    bubba.left(15)
    bubba.forward(50)
    bubba.left(157)
    bubba.forward(50)

#tidy up window



window.exitonclick()        # allow program to exit, when you click the window

