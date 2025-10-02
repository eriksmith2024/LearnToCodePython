import turtle

slowspoke = turtle.Turtle()
slowspoke.shape('turtle')
slowspoke.color('blue')

pokey = turtle.Turtle()
pokey.shape('turtle')
pokey.color('red')

def make_sqaure(the_turtle):
    for i in range(0,4):
        the_turtle.forward(100)
        the_turtle.right(90)

def make_spiral(the_turtle):
    for i in range (0,36):
        make_sqaure(the_turtle)
        the_turtle.right(10)

# make_sqaure(slowspoke)
# pokey.right(45)
# make_sqaure(pokey)

make_spiral(slowspoke)
pokey.right(5)
make_spiral(pokey)


turtle.done()
