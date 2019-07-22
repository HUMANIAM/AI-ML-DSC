"""
recursion is about define something in terms of itself. solve the complex big problem
solving the smaller ones of this problems.
In this program we draw function that draws different orders of koch fractals.
"""
import turtle, pygame, math, time, random

############################# Koch ##################
#####################################################
def koch(tortoise, order, size):
	"""
	make tortoise draw a koch fractal of 'order' and size.
	Leave the turtle face the same direction.
	"""
	# base case
	if order == 0:
		tortoise.forward(size)
	else:
		for angle in [60, -120, 60, 0]:
			koch(tortoise, order-1, size/3)
			tortoise.left(angle)
	pass


def init_screen():
	screen = turtle.Screen()
	turt = turtle.Turtle()
	turt.speed(10)
	return turt, screen


def draw_koch(sides = 3, order = 2, size = 100):
	turt, screen = init_screen()
	angle = 180 - ((sides - 2) * 180 / sides)
	# draw square koch
	for _ in range(sides):
		koch(turt, order, size)
		turt.right(angle)
		# break


	screen.mainloop()
	pass

################################  Tree picture  #############
##############################################################
pygame.init() # prepare the pygame module for use
# Create a new surface and window.
surface_size = 500
w, h = 1024, 1024
main_surface = pygame.display.set_mode((w,h))
my_clock = pygame.time.Clock()
random.seed(time.time())
# rng = random.Random(time())

def random_color():
	r = random.randint(0, 255);
	g = random.randint(0, 255);
	b = random.randint(0, 255);
	color = (r, g, b)
	return color
	pass


def draw_tree(order, theta, size, position, heading, color=(0,0,0), depth=0):
	trunk_ratio = 0.25 # How big is the trunk relative to whole tree?
	trunk = size * trunk_ratio # length of trunk
	dx = trunk * math.cos(heading)
	dy = trunk * math.sin(heading)
	newposition = (position[0] + dx, position[1] + dy)
	pygame.draw.line(main_surface, color, position, newposition)

	if order > 0: 
		""" Draw the sub halves of current edge using dfs technique."""
		color1 = random_color()
		color2 = random_color()

		# make the recursive calls to draw the two subtrees
		newsize = size*(1 - trunk_ratio)
		draw_tree(order-1, theta, newsize, newposition, heading-theta, color1, depth+1)
		draw_tree(order-1, theta, newsize, newposition, heading+theta, color2, depth+1)

 
def gameloop():
	theta = 0
	changeColor = 0
	while True:
		# Handle evente from keyboard, mouse, etc.
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			break;

		# Updates - change the angle
		theta += 0.01

		# Draw everything
		if changeColor == 5 :
			changeColor = 0
			main_surface.fill(random_color())

		draw_tree(13, theta, surface_size*0.9, (w//2, h//2), -math.pi/2)

		pygame.display.flip()
		my_clock.tick(12000)
		changeColor += 1


def main():
	# gameloop()
	draw_koch()

if __name__ == '__main__':
	main()
