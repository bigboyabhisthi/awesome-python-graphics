import turtle  # importing our graphical library
turtle.speed(10)  # Set speed of drawing
turtle.hideturtle()  # Disable default turtle object
s = turtle.Screen()  # Create a graphic window
s.bgcolor("black")  # Set background color
turtle.pencolor("red")  # Set drawing color
s.title("Dragon Curve By Smaranjit Ghose")  # Set Title


def dragon_curve(l, n):
  '''
  The function to draw the Dragon curve
  '''
  def x(n):
    if n == 0:
      return
    x(n-1)
    turtle.right(90)
    y(n-1)
    turtle.forward(l)

  def y(n):
    if n == 0:
      return
    turtle.forward(l)
    x(n-1)
    turtle.left(90)
    y(n-1)
  turtle.fd(l)
  x(n)


dragon_curve(5, 15)
