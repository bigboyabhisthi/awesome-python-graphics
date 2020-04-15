import turtle  # importing our graphical library
import math  # importing our mathematical function library
turtle.speed(10)  # Set speed of drawing
turtle.hideturtle()  # Disable default turtle object
s = turtle.Screen()  # Create a graphic window
s.bgcolor("black")  # Set background color
s.title("Logarithmic Spiral By Smaranjit Ghose")  # Set Title


def logarithmic_spiral(a, b):
    '''
    The function to draw the Logarithmic Spiral
    '''
    turtle.up()
    turtle.setpos(0, 0)
    turtle.down()
    colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"] # a list of colors of rainbow
    c = 0 # an index value to determine the color every time
    for i in range(0, 3000, 5):
      turtle.pencolor(colors[c]) #Set drawing pen color
      t = math.radians(i)
      x = a*math.exp(b*t)*math.cos(t)
      y = a*math.exp(b*t)*math.sin(t)
      turtle.setpos(x, y)
      c = (c+1)%7

logarithmic_spiral(0.20, 0.20)
