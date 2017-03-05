import turtle
'''
def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(1)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)
	angie.speed(1)

	window.exitonclick()

draw_square()

'''
# Better Answer

def draw_square(some_turtle):
	for i in range(1, 5):
		some_turtle.forward(100)
		some_turtle.right(90)
def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# Create the Turtle Brad - Draw a Square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)
	for i in range (1, 37):
		draw_square(brad)
		brad.right(10)

	# Create the Turtle Angie - Draws a Circle
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)
	angie.speed(1)

	window.exitonclick()

draw_art()








