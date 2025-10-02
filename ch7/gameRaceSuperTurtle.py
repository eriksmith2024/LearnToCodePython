import turtle
import random
import os

turtles = []

class SuperTurtle(turtle.Turtle):
    def forward(self, distance):
        cheat_distance = distance + 25
        turtle.Turtle.forward(self, cheat_distance)
    
class SlowTurtle(turtle.Turtle):
    def forward(self, distance):
        doyle_distance = distance -25
        turtle.Turtle.forward(self, doyle_distance)

def setup():
    global turtles
    startline = -625
    screen = turtle.Screen()
    screen.setup(1290, 720)

    # Build full path to pavement.gif in same folder as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(script_dir, "pavement.gif")
    print("Loading background from:", bg_path)  # debug

    screen.bgpic(bg_path)

    turtle_ycor = [-40, -20, 0, 20, 40]
    turtle_color = ['blue', 'red', 'purple', 'yellow', 'green']

    for i in range(0,len(turtle_ycor)):
        if i == 1:
            new_turtle = SuperTurtle()
        elif i == 3:
            new_turtle = SlowTurtle()
        else:
            new_turtle = turtle.Turtle()
      
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.setpos(startline, turtle_ycor[i])
        new_turtle.color(turtle_color[i])
        turtles.append(new_turtle)

def race():
    global turtles
    winner = False
    finishline = 590

    while not winner:
        for current_turtle in turtles:
            move = random.randint(10,50)
            current_turtle.forward(move)

            xcor = current_turtle.xcor()
            if (xcor >= finishline):
                winner = True
                winner_color = current_turtle.color()
                print('The winner is', winner_color[0])

setup()

race()

turtle.done()
