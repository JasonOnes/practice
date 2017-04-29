import turtle

jaques = turtle.Turtle()
jaques.color("purple")
window = turtle.Screen()
window.bgcolor("lightgreen")

def star(turtle, num_sides, side_length):
    for side in range(num_sides):
        turtle.forward(side_length)
        turtle.right(180 - 180 /num_sides)

def flag(turtle, num_stars):
    for star_sign in range(num_stars):
        turtle.penup()
        turtle.left(num_stars/360)
        turtle.forward(50)
        turtle.pendown()
        star(turtle, 5, 25)

flag(jaques, 5)
