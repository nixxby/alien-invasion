import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Creates and Manages the behaviour of our Ship"""
	
	def __init__(self,screen,settings):
		"""Initialize ship and it starting position"""

		super().__init__()
		
		self.screen = screen
		self.image = pygame.image.load('alien_invasion/images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect() 
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		self.setting = settings
		self.center = float(self.rect.centerx)
		
		#Ship movement Flags
		self.moving_right = False
		self.moving_left = False
		
	def update_ship(self):
		"""Update ship's position based on movement flags"""
		if self.moving_right:
			if self.rect.right < self.screen_rect.right:
				self.center += self.setting.ship_speed_factor
			
		if self.moving_left:
			if self.rect.left > 0:
				self.center -= self.setting.ship_speed_factor
		
		#update self rect object from float center position
		self.rect.centerx = self.center
		
	def center_ship(self):
		""" Center the ship on screen."""	
		self.center = self.screen_rect.centerx
	
	def blitme(self):
		"""place ship at current location"""
		self.screen.blit(self.image,self.rect)
