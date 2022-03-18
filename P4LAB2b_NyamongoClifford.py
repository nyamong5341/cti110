import turtle
# initial for CAN
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Inital for CN")
Ny = turtle.Turtle()
Ny.pensize(10)
Ny.pencolor("black")
Ny.shape("turtle")

#initial C
Ny.forward(150)
Ny.backward(150)
Ny.right(90)
Ny.forward(150)
Ny.left(90)
Ny.forward(150)

Ny.penup()
Ny.forward(45)
Ny.pendown()

#initial N
Ny.left(90)
Ny.forward(150)
Ny.right(145)
Ny.forward(180)
Ny.left(145)
Ny.forward(150)

#initial A
Ny.penup()
Ny.right(180)
Ny.forward(150)
Ny.left(90)
Ny.forward(45)
Ny.pendown()

Ny.left(65)
Ny.forward(150)
Ny.right(130)
Ny.forward(150)
Ny.penup()
Ny.left(180)
Ny.forward(75)
Ny.pendown()
Ny.left(70)
Ny.forward(70)


wn.mainloop()

