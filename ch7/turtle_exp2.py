import turtle

slowspoke = turtle.Turtle()
slowspoke.shape('turtle')


slowspoke.pencolor('blue')
# slowspoke.penup()
slowspoke.setposition(-120, 0)
# slowspoke.pendown()
slowspoke.circle(50)

slowspoke.pencolor('red')
# slowspoke.penup()
slowspoke.setposition(120,0)
# slowspoke.pendown()
slowspoke.circle(50)

turtle.done()
