#!venv310/bin/python

import pygame
import os
import sys

from objects import Square, Line, Text

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 600

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Impact calculation")
FPS = 60

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Other
LINE_POS_Y = HEIGHT // 2 + HEIGHT // 6

def draw_window(square_left,square_right):
	try:
		window.fill(BLACK)
		# Horizontal line
		Line.new(surface=window,color=WHITE,y_position=(0, LINE_POS_Y),x_position=(WIDTH, LINE_POS_Y),width=2)
		# Vertical line
		Line.new(surface=window,color=WHITE,y_position=(0 + WIDTH // 8, 0),x_position=(0 + WIDTH // 8, HEIGHT),width=2)

		square_left.surface_square(screen_height=HEIGHT,screen_width=WIDTH,aWindow=window)
		square_right.surface_square(screen_height=HEIGHT,screen_width=WIDTH,aWindow=window)

		# Collision counter
		counter_text = f"{Square.collision_counter}"
		Text.new(window, font, counter_text, (WIDTH // 2 - 80, 20), YELLOW)

	except Exception as e:
		print(f"Error in draw function: {e}")
		sys.exit()

	pygame.display.update()

if __name__ == "__main__":
	right_square_mass = 100
	right_square_vel = -2
	right_square_size = 100

	vertical_line_x_pos = WIDTH // 8

	font = pygame.font.Font(None,50)

	# Define initial squares
	square_right = Square(position=WIDTH - WIDTH // 6,mass=right_square_mass,vel=right_square_vel,size=right_square_size,color=WHITE)
	square_left = Square(position=vertical_line_x_pos + WIDTH // 10,mass=1,vel=0,size=50,color=WHITE)


	# game cycle
	try:
		run = True
		clock = pygame.time.Clock()
		while run:
			clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

				# here we check for events, like keys pressed

			# Update square positions
			square_right.move(vertical_line_x_pos)
			square_left.move(vertical_line_x_pos)

			# Check for impacts
			square_right.impact(square_left)

			# Draw function
			draw_window(square_left,square_right)

	except KeyboardInterrupt:
		run = False
		sys.exit()

	except Exception as e:
		print(f"Error in game cycle: {e}")
		run = False
		sys.exit()


	sys.exit()
