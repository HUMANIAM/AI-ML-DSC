"""
The turtles are fun, but the real purpose of the chapter is to teach ourselves a little more Python, and to develop
our theme of computational thinking, or thinking like a computer scientist.
"""

import turtle
import curses
from random import randint
from curses import wrapper  
from time import time, sleep
from curses.textpad import Textbox, rectangle

# init curses. screen is a window object
"""stdscr = curses.initscr()"""		

# turn off automatic echoing of keys to the screen
"""curses.noecho()"""

# response to the entered keys instantly without pressing the enter key.
"""curses.cbreak()"""

# deal with pressed keys in more expressive way like KEY_LEFT, KEY_HOME
"""stdscr.keypad(True)"""

# Terminate the curses functionality
""""
curses.nocbreak()
stdscr.keypad(False)
curses.echo()"""

# restore the terminal to its original operating mode.
"""curses.endwin()"""

def create_screen(begin_x, begin_y, width, height):
	"""create a screen starts at (x, y) with specific width and height."""
	return curses.newwin(height, width, begin_y, begin_x)

def move_left(turt, angle, dis, col):
	"""first set direction then move"""
	turt.color(col)
	turt.left(angle)
	turt.forward(dis)


def spiral_movement(turt, colors):
	"""make spiral movement with turtl from the center"""
	screenWidth = (turtle.Screen().screensize())[0]
	to = screenWidth
	j, c = 0, 0

	for i in range(1, to, 5):
		move_left(turt, 60, i, 'black')
		move_left(turt, 60, i, colors[c])
		j += 1
		if j == 2 :
			j = 0
			c += 1
			if c == 4 : c = 0
			

def play_with_turtle(turt):
	colors = ["yellow", "red", "purple", "blue"]
	spiral_movement(turt, colors)

def move_randomly(turt):
	"""move the turtle randomly in the four directions left-top-right-down with differnet
	 values. do that for 20 seconds"""
	directions = {0: 'left', 1: 'top', 2:'right', 3:'bottom'}
	start_time = int(time())

	while int(time()) - start_time < 100 :
		dir = randint(0, 3)						# random direction
		displacement = randint(50, 100)			# random displacement
		if directions[dir] is 'left':
			turt.left(displacement)

		elif directions[dir] is 'top':
			turt.forward(displacement)

		elif directions[dir] is 'right':
			turt.right(displacement)

		else:
			turt.backward(displacement)

def turtle_game(stdscr):
	"""moving the turtle randomly in different directions"""
	window = turtle.Screen()
	window.bgcolor("lightgreen") # Set the window background color
	window.title("Hello, Tess!") # Set the window title

	alex = turtle.Turtle()
	alex.color("blue") # Tell tess to change her color
	alex.pensize(2) # Tell tess to set her pen width
	alex.speed(8)
	play_with_turtle(alex)
	window.mainloop()

def main(stdscr):
	# play turtule game.
	turtle_game(stdscr)


if __name__ == '__main__':
	"""terminate the app in correct way if any crashes happen during the running time
		so the original state of the terminal will be like before the curses app run.
		wrapper alse makes all the initialization described above."""
	wrapper(main)
