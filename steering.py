import curses
import time

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

def move_left():
	print("left")

def move_right():
	print("right")

try:
	while True:
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_LEFT:
			move_left()
		elif char == curses.KEY_RIGHT:
			move_right()

finally:
	curses.nocbreak()
	screen.keypad(0)
	curses.echo()
	curses.endwin()

