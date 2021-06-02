class GameStats():
	"""Track stats for alien invasions within the game"""
	
	def __init__(self,setting):
		self.setting = setting
		self.game_active = False
		self.high_score = 0
		self.reset_stats()
		
	def reset_stats(self):
		"""Initialize stats and change them during the game """
		self.ships_left = self.setting.ship_limit
		self.score = 0
		self.level = 1
		
