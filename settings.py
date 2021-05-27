class Settings():
	"""A Class to save all Game Settings in one place """
	def __init__(self):
		""" Initialize Game Settings"""
		self.screen_width = 900
		self.screen_height = 600
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 0.75
		
		self.bullet_speed_factor = 0.375
		self.bullet_width = 6
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		
		self.bullets_max = 3
