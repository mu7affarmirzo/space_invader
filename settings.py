import pygame
class Settings():
	"""docstring for Settings"""
	def __init__(self):
		
		self.screen_width = 1050
		self.screen_height = 650
		self.bg_color = (230, 230, 230)
		self.ship_speed_factor = 1.5

		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 15

		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		