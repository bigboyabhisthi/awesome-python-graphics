import turtle  # importing our graphical library
import math #importing our mathematical function library
turtle.speed(10)  # Set speed of drawing
turtle.hideturtle()  # Disable default turtle object
s = turtle.Screen()  # Create a graphic window
s.bgcolor("black")  # Set background color
turtle.pencolor("red")  # Set drawing color
s.title("Tree Fractal By Smaranjit Ghose")  # Set Title
turtle.left(90)


def tree_fractal(d,angle):
  '''
  The function to draw the Tree Fractal
  '''
  if d > 5:
    turtle.forward(d)
    turtle.right(angle)
    tree_fractal(d/math.sqrt(2),angle)
    turtle.left(2*angle)
    tree_fractal(d/math.sqrt(2),angle)
    turtle.right(angle)
    turtle.backward(d)


tree_fractal(100,20)
