import turtle
turtle.Screen().bgcolor("red")
star=turtle.Turtle()
#first triangle for star
star.forward(200)
star.left(120)
star.forward(200)
star.left(120)
star.forward(200)
#going to location
star.penup()
star.right(150)
star.forward(100)
#second triangle for star
star.pendown()
star.right(90)
star.forward(200)
star.right(120)
star.forward(200)
star.right(120)
star.forward(200)
turtle.done()