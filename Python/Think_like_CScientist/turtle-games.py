import turtle
from turtle import *

def f():
	fd(50); lt(20)
class MyTurtle(turtle.Turtle):
	def glow(self,x,y):
		self.goto(x, y)
		self.fillcolor("red")
	def unglow(self,x,y):
		self.fillcolor("")

	def done(self):
		turtle.done()

screen = turtle.Screen()
screen.onkey(f, "Up")

turt = MyTurtle()
turt.onclick(turt.glow)     # clicking on turtle turns fillcolor red,
turt.onrelease(turt.unglow) # releasing turns it to transparent.
screen.onclick(turt.goto)
screen.listen()
turt.done()
