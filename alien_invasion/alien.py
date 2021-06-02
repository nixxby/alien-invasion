import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Create a class for Alien Fleet"""
	
	def __init__(self,screen,setting,stats):
		"""initialize alien features"""
		super().__init__()
		self.setting = setting
		self.screen = screen
		
		if stats.level<4:
			self.image = pygame.image.load('alien_invasion/images/alien1.bmp')
		elif stats.level<6 : 
			self.image = pygame.image.load('alien_invasion/images/alien2.bmp')
		else:
			self.image = pygame.image.load('alien_invasion/images/alien3.bmp')
		self.rect = self.image.get_rect()
		
		self.rect.x = self.rect.width / 2
		self.rect.y = self.rect.height / 2
		
		self.x = float(self.rect.x)
		
	def update(self):
		self.x += self.setting.alien_speed_factor * self.setting.fleet_direction
		self.rect.x = self.x

	def check_edges(self):
		"""Checks if alien fleet has hit right or left edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.left<=0 or self.rect.right>= screen_rect.right:
			return True

	def blitme(self):
		"""place ship at current location"""
		self.screen.blit(self.image,self.rect)
