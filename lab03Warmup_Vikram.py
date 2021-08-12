# Vikram - A program to draw the first letter of your name

import turtle

def draw_picture(the_turtle):

    ''' Draw a simple picture using a turtle '''

    the_turtle.speed(1)

    the_turtle.forward(100)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(90)    



my_turtle = turtle.Turtle()  # Create a new Turtle object

draw_picture(my_turtle)      # make the new Turtle draw the shape

turtle1 = turtle.Turtle()

turtle2 = turtle.Turtle()

turtle1.speed(1)

turtle2.speed(2)

turtle1.setpos(-50, -50)

turtle2.setpos(200, 100)

turtle1.forward(100)

turtle2.left(90)

turtle2.forward(100)


#turtle.forward(distance)

#turtle.fd(distance)

#Parameters: distance – a number (integer or float)

#Move the turtle forward by the specified distance, in the direction the turtle is headed.