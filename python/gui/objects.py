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
		try:
			return self.position
		except Exception as e:
			print(f"Error in get_position function: {e}")

	def get_mass(self):
		try:
			return self.mass
		except Exception as e:
			print(f"Error in get_mass function: {e}")

	def get_vel(self):
		try:
			return self.vel
		except Exception as e:
			print(f"Error in get_vel function: {e}")

	def move(self, left_limit):
		try:
			step = max(1000, int(abs(self.vel) // 1000))
			for _ in range(step):
				self.position += self.vel / step

				if self.position < left_limit:
					self.position = left_limit
					self.vel *= -1

					# update collision counter
					Square.collision_counter += 1
		except Exception as e:
			print(f"Error in move function: {e}")

	def surface_square(self, screen_height, screen_width, aWindow):
		try:
			square_y = (screen_height // 2 + screen_height // 6) - self.size
			pygame.draw.rect(aWindow, self.color, (self.position, square_y, self.size, self.size))
		except Exception as e:
			print(f"Error in surface_square function: {e}")

	def impact(self, other_square):
		try:
			next_pos_self = self.position + self.vel
			next_pos_other = other_square.position + other_square.vel

			if next_pos_self + self.size >= next_pos_other and next_pos_self <= next_pos_other + other_square.size:
				# Elastic collision formula
				m1, m2 = self.mass, other_square.mass
				v1, v2 = self.vel, other_square.vel

				new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
				new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

				self.vel = new_v1
				other_square.vel = new_v2

				# update collision counter
				Square.collision_counter += 1
		except Exception as e:
			print(f"Error in impact function: {e}")

class Line:
	@staticmethod
	def new(surface,color,y_position,x_position,width):
		try:
			pygame.draw.line(surface, color, y_position, x_position, width)
		except Exception as e:
			print(f"Error in Line::new function: {e}")

class Text:
	@staticmethod
	def new(surface,font,text,position,color):
		try:
			new_text = font.render(text,True,color)
			surface.blit(new_text, position)
		except Exception as e:
			print(f"Error in Text::new function: {e}")
