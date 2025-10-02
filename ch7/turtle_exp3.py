import turtle

slowspoke = turtle.Turtle()
slowspoke.shape('turtle')


def make_shape(t, sides):
    angle = 360/sides
    for i in range (0, sides):
        t.forward(100)
        t.right(angle)

make_shape(slowspoke, 3)
make_shape(slowspoke, 5)
make_shape(slowspoke, 8)
make_shape(slowspoke,10)


turtle.done()
