import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class for a Bullet fired from ship"""
	def __init__(self,setting,screen,ship):
		"""Initialize a bullet """
		super().__init__()
		
		self.screen = screen
		self.rect = pygame.Rect(0,0,setting.bullet_width,setting.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)
		
		self.speed = setting.bullet_speed_factor
		self.color = setting.bullet_color

	def update(self):
		"""moves bullet upwards"""
		self.y -= self.speed
		self.rect.y =  self.y

	def draw(self):
		"""Draws bullet on screen"""
		pygame.draw.rect(self.screen,self.color,self.rect)
