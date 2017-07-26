import turtle
num_pets = 5 #number of sides in the drawing
for i in range(num_pets):
    turtle.left(360/num_pets)
    turtle.forward(100)
turtle.mainloop()
