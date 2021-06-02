class Settings():
	"""A Class to save all Game Settings in one place """
	def __init__(self):
		""" Initialize Game's static Settings"""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (230,230,230)
		
		#Ship settings
		self.ship_limit = 3
		
		#bullet settings
		self.bullet_width = 6
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_max = 3
		
		#Dynamic changes
		self.speed_factor = 1.2
		self.initialize_dynamic_settings()
		
		
	def initialize_dynamic_settings(self):
		"""To initialize dynamic settings"""
		
		self.ship_speed_factor = 0.7
		self.bullet_speed_factor = 1.0
		self.alien_speed_factor = 0.60
		
		self.alien_points = 30
		self.fleet_drop_speed = 10
		self.fleet_direction = 1
		
	def increase_speed(self):
		self.ship_speed_factor *= self.speed_factor
		self.bullet_speed_factor *= self.speed_factor
		self.alien_speed_factor *= self.speed_factor
		self.fleet_drop_speed *= self.speed_factor
		self.alien_points += 10
