import turtle

class Snake(turtle.Turtle):
	"""docstring for Snake"""
	turt, screen = None, None
	def __init__(self):
		super(Snake, self).__init__()
		self.initGame()
	
	def initGame(self):
		self.screen = turtle.Screen()
		self.screen.onkey(self.move, "Up")
		self.screen.onclick(self.goto)
		self.speed(8)
		self.screen.listen()

	def move(self):
		self.forward(20)
		self.left(20)

	def done(self):
		turtle.done()


		
def main():
	snakegame = Snake()
	snakegame.done()
if __name__ == '__main__':
	main()