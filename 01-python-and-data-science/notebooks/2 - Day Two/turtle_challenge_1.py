import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()

# Challenge 1: Squares in a Grid

# YOUR CODE HERE
t.pencolor("green")
t.speed(20)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.left(90)
t.forward(45)
t.left(90)
t.forward(30)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.right(90)
t.forward(90)
t.right(90)
t.forward(30)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)
t.penup()
t.forward(45)
t.pendown()
for i in range(0,4):
    t.right(90)
    t.forward(30)


# DON'T TOUCH THIS
turtle.mainloop()