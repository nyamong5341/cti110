import turtle
# Draw a square and a triangle using for loop or while loop
wn = turtle.Screen()
wn.bgcolor("light pink")
wn.title("Triangle and Square")
Ny = turtle.Turtle()
Ny.pensize(10)
Ny.pencolor("black")
Ny.shape("turtle")
for i in range (4):
    Ny.forward(150)
    Ny.left(90)

Ny.penup()
Ny.forward(200)
Ny.pendown()


for i in range(3):
    Ny.forward(150)
    Ny.left(120)



wn.mainloop()


