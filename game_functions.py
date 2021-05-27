import sys
import pygame

from bullet import Bullet

def check_events(setting,screen,ship,bullets):
	#This loop captures Mouse & Keyboard movements.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,setting,screen,ship,bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			

def check_keydown_events(event,setting,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(setting,screen,ship,bullets)
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def update_screen(setting,screen,ship,bullets):
	screen.fill(setting.bg_color)	#create screen bg color
	for bullet in bullets.sprites():
		bullet.draw()
	ship.blitme()
	pygame.display.flip()

def update_bullets(bullets):
	"""Remove Disappeared bullets from sprites"""
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(setting,screen,ship,bullets):
	"""Fires a bullet if max limit not reached"""
	if len(bullets) <setting.bullets_max:
			new_bullet = Bullet(setting,screen,ship)
			bullets.add(new_bullet)
