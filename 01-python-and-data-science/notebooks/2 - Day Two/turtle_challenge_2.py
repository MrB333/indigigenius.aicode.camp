import turtle

window = turtle.Screen()
window.setup(width=800, height=800)

t = turtle.Turtle()
t.color("white")
t.penup
t.setposition(-210, 210)
t.color("brown")
t.pendown
t.circle(60, extent=360)

t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
t.setposition(-210, 0)
t.color("brown")
t.pendown
t.circle(60, extent=360)

t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
t.setposition(-210, -210)
t.color("white")
t.pendown
t.circle(60, extent=360)

t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
t.forward(210)
t.color("brown")
t.pendown
t.circle(60, extent=360)
t.color("white")
t.penup
# Challenge 2: Circles in a Grid with One Missing

# YOUR CODE HERE


# DON'T TOUCH THIS
turtle.mainloop()