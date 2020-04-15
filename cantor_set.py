import turtle  # importing our graphical library
turtle.speed(10)  # Set speed of drawing
turtle.hideturtle()  # Disable default turtle object
s = turtle.Screen()  # Create a graphic window
s.bgcolor("black")  # Set background color
turtle.pencolor("red")  # Set drawing pen color
turtle.pensize(5) #Set drawing pen size to 5 (For better visualization)
s.title("Cantor Set Fractal By Smaranjit Ghose")  # Set Title



def cantor_set(x, y, length):
  if(length > 1):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(length)
    turtle.up()
    y = y-10
    turtle.goto(x, y)
    turtle.down()
    cantor_set(x, y, length/3)
    cantor_set(x+length*2/3, y, length/3)


cantor_set(-250, 0, 500)
