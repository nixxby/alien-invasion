import pygame.font

class Button():
	"""Play button displayed in the beginning"""
	
	def __init__(self,setting,screen,msg):
		"""Set Button Attributes"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		
		self.width, self.height = 150, 75
		self.button_color = (255,0,0)
		self.font_color = (255,255,255)
		self.font = pygame.font.SysFont(None,45)
		
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery +100
		
		self.prep_msg(msg)
		

	def prep_msg(self,msg):
		"""Turn msg text into a msg image and center it over button."""
		self.msg_img = self.font.render(msg,True,self.font_color,self.button_color)
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center
		
	def draw_button(self):
		"""Draw the button and place img_msg over it."""
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_img,self.msg_img_rect)
