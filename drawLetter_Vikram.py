# Vikram - Draw my first initial

import turtle

def draw_V(the_turtle): 

  """ Draw my firt initial """

  the_turtle.speed(1)
  the_turtle.left(115)
  the_turtle.forward(100)
  the_turtle.backward(100)
  the_turtle.right(55)
  the_turtle.forward(100)
  
  

turtle1 = turtle.Turtle()
draw_V(turtle1)



turtle2 = turtle.Turtle()
turtle2.speed(1)
turtle2.penup()
turtle2.setpos(-100,0)
turtle2.pendown()
draw_V(turtle2)








