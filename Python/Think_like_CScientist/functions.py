"""
def fn_name(params):
	body

1- docstring for documentation: after the signature of the function we use docstring doc to 
	state what is this function do and help programmer to know more about our function parms
	def f(args) : triple quote your docstring

"""
import turtle 
def draw_multicolor_square(animal, size):
	"""given animal and size we draw a square with different color sides"""
	for color in ["red", "purple", "black", "blue"]:
		animal.color(color)
		animal.forward(size)
		animal.left(90)

def newWindow(title, color):
	"""Given title color the function return a new window with these properties"""
	window = turtle.Screen()
	window.bgcolor(color)
	window.title(title)
	return window

def newTurtle(pensize, speed):
	"""Given pensize, speed newTurtle create new turtle"""
	turt = turtle.Turtle()
	turt.pensize(pensize)
	turt.speed(speed)
	return turt

def angle90Degree(turt, sideLength):
	"""given length of the 90 dgreee anglee we draw the square. if you want 
	angle be 90 + epsisonAngle pass it. if not pass it with zero"""
	turt.backward(sideLength)
	turt.right(90)
	turt.forward(sideLength)
	turt.right(90)

# create window and turtle
window = newWindow("play game", "lightgreen")
tess = newTurtle(3, 10)

size, increment, deviationAngle = 10, 10, 2
for _ in range(10):
	angle90Degree(tess, size)
	size += increment
	angle90Degree(tess, size)
	size += increment
	tess.left(deviationAngle)
# for _ in range(100):
# 	draw_multicolor_square(tess, size)
# 	size += 5
# 	tess.forward(5)
# 	tess.right(5)
	

window.mainloop()