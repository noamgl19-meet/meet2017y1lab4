import turtle
turtle.penup()
x = 0

while x<300:
    y = x**2/300  #x**2 is the same as x*x
    turtle.goto(x, y)
    x = x + 1
while x>-300:
    y = x**2/300  #x**2 is the same as x*x
    turtle.pendown()
    turtle.goto(x, y)
    x = x - 1
turtle.mainloop()
