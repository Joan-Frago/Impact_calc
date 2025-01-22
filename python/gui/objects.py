import pygame
class Square:
	collision_counter = 0
	def __init__(self,position,mass,vel,color,size=50):
		self.position = position
		self.mass = mass
		self.vel = vel
		self.size = size
		self.color = color

	def get_position(self):
		return self.position

	def get_mass(self):
		return self.mass

	def get_vel(self):
		return self.vel

	def move(self, left_limit):
		self.position += self.vel

		if self.position < left_limit:
			self.position = left_limit
			self.vel *= -1

			# update collision counter
			Square.collision_counter += 1

	def surface_square(self, screen_height, screen_width, aWindow):
		square_y = (screen_height // 2 + screen_height // 6) - self.size
		pygame.draw.rect(aWindow, self.color, (self.position, square_y, self.size, self.size))

	def impact(self, other_square):
		if self.position + self.size >= other_square.position and self.position <= other_square.position + other_square.size:
			# Elastic collision formula
			m1, m2 = self.mass, other_square.mass
			v1, v2 = self.vel, other_square.vel

			new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
			new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

			self.vel = new_v1
			other_square.vel = new_v2

			# update collision counter
			Square.collision_counter += 1

class Line:
	@staticmethod
	def new(surface,color,y_position,x_position,width):
		pygame.draw.line(surface, color, y_position, x_position, width)

class Text:
	@staticmethod
	def new(surface,font,text,position,color):
		new_text = font.render(text,True,color)
		surface.blit(new_text, position)
