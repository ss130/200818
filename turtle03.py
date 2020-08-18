import turtle
b=turtle.Turtle()

b.color('white')
b.shape('turtle')

a=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
a.color('white')
a.shape('turtle')
for i in range(1,360):
    a.right(2)
    a.forward(2)
    b.left(2)
    b.forward(2)