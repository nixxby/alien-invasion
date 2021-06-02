import pygame.font
from pygame.sprite import Group

from alien_invasion.ship import Ship 

class Scoreboard():
	"""To report live score in a scoreboard"""
	
	def __init__(self,setting,screen,stats):
		"""Initialize scoreboard attributes"""
		self.screen = screen
		self.setting = setting
		self.stats = stats
		self.screen_rect = screen.get_rect()
		
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		
		self.prep_ship()
		self.prep_score()
		self.prep_high_score()
		self.prep_level()

	def prep_high_score(self):
		self.rounded_high_score = int(round(self.stats.high_score,-1))
		self.high_score_str = "{:,}".format(self.rounded_score)
		self.high_score_img = self.font.render(self.high_score_str,True,self.text_color,self.setting.bg_color)
		
		self.high_score_rect = self.high_score_img.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = 20
		
	def prep_score(self):
		"""Turns score into a rendered img on screen"""
		self.rounded_score = int(round(self.stats.score,-1))
		self.score_str = "{:,}".format(self.rounded_score)
		self.score_img = self.font.render(self.score_str,True,self.text_color,self.setting.bg_color)
		
		self.score_rect = self.score_img.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_level(self):
		"""Display level on screen"""
		self.level_str = str(self.stats.level)
		self.level_img = self.font.render(self.level_str,True,self.text_color,self.setting.bg_color)
		
		self.level_rect = self.level_img.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ship(self):
		"""Display ships available on top left"""
		self.ships = Group()
		for ship_num in range(self.stats.ships_left):
			ship = Ship(self.screen,self.setting)
			ship.rect.x = ship.rect.width * ship_num +10
			ship.rect.y = 10
			self.ships.add(ship)
		

	def show_score(self):
		"""display scoreboard & levelboard on screen"""
		self.screen.blit(self.score_img,self.score_rect)
		self.screen.blit(self.high_score_img,self.high_score_rect)
		self.screen.blit(self.level_img,self.level_rect)
		self.ships.draw(self.screen)
