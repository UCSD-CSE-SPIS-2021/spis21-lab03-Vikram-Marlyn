# Anonymous turtle is something Python provides that can be controlled without ever being actually created
# The difference between turtle and Turtle() is that turtle is a Python library and Turtle() is a special function that creates a new Turtle object
#my_turtle.setpos(0,100)

import turtle

def draw_V(the_turtle, size): 
  
  """ Draw my firt initial with the given size """
  the_turtle.speed(1)
  the_turtle.left(115)
  the_turtle.forward(100*size)
  the_turtle.backward(100*size)
  the_turtle.right(55)
  the_turtle.forward(100*size)
 
  
  

turtle1 = turtle.Turtle()
draw_V(turtle1,1)


turtle2 = turtle.Turtle()
turtle2.speed(1)
turtle2.penup()
turtle2.setpos(-100,0)
turtle2.pendown()
draw_V(turtle2, 0.5)
