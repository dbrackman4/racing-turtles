import turtle
import random

turtle.mode("logo")
num_turtles = 8
turtles = []
speeds = []
colors = ['red', 'yellow', 'blue', 'green', 'magenta', 'brown', 'purple', 'lime']
names = ["Big Red", "Banana", "Sapphire", "The Machine", "Bubblegum", "Desmond", "Violet", "Skittle"]
screen = turtle.Screen()
drawTurtle = turtle.Turtle()
drawTurtle.hideturtle()
drawTurtle.penup()
drawTurtle.speed(0)

def drawSquare(t, length):  #Draws a square of length "length" with turtle "t" where top right corner is turtles initial location
    drawTurtle.begin_fill()
    for _ in range(4):
        t.forward(length)
        t.right(90)
    drawTurtle.end_fill()

def drawFinishLine():
    drawTurtle.goto(-375, 500)
    drawTurtle.right(90)

    drawTurtle.fillcolor("white")
    drawTurtle.begin_fill()
    for _ in range(2):
        drawTurtle.forward(750)
        drawTurtle.right(90)
        drawTurtle.forward(50)
        drawTurtle.right(90)
    drawTurtle.end_fill()
    drawTurtle.fillcolor("black")
    for _ in range(15):
        drawSquare(drawTurtle, 25)
        drawTurtle.forward(25)
        drawTurtle.right(90)
        drawTurtle.forward(25)
        drawTurtle.left(90)
        drawSquare(drawTurtle, 25)
        drawTurtle.forward(25)
        drawTurtle.left(90)
        drawTurtle.forward(25)
        drawTurtle.right(90)

def drawGround():
    drawTurtle.fillcolor("tan")
    drawTurtle.goto(-375, 450)
    drawTurtle.begin_fill()
    for _ in range(2):
        drawTurtle.forward(750)
        drawTurtle.right(90)
        drawTurtle.forward(950)
        drawTurtle.right(90)
    drawTurtle.end_fill()

    
def initializeTurtles():
    
    for i in range(num_turtles):
        #create turtle objects
        turtles.append(turtle.Turtle())
        #set turtle "speeds"
        turtles[i].speed(10)
        speeds.append(random.uniform(0, 5))
        #set turtle shape to turtle
        turtles[i].shape("turtle")
        #set turtle colors
        turtles[i].color(colors[i])
        #set turtle names
        setattr(turtles[i], "name", names[i])
        #set starting positions
        turtles[i].penup()
        turtles[i].goto(-350 + (i) * 100, -400)
        turtles[i].pendown()
        turtles[i].pensize(3)

def raceTurtles():
    finished = False
    while not finished:
        for i in range(num_turtles):
            turtles[i].forward(speeds[i] + random.uniform(0, 5))
            if checkEndCondition(i):
                finished = True

def checkEndCondition(i):
    if turtles[i].ycor() >= 475:
        return True
    return False


def main():
    screen.screensize(1000, 1000)
    screen.bgcolor("light gray")

    drawFinishLine()
    drawGround()
    initializeTurtles()
    raceTurtles()

    screen.exitonclick()
    

main()