import sys
import pygame

from time import sleep
from alien_invasion.bullet import Bullet
from alien_invasion.alien import Alien

def check_events(setting,screen,ship,aliens,bullets,stats,play_button,board):
	#This loop captures Mouse & Keyboard movements.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,setting,screen,ship,bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
			
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(setting,screen,stats,board, play_button, ship, aliens, bullets, mouse_x, mouse_y)
			
def check_play_button(setting,screen,stats,board, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		setting.initialize_dynamic_settings()
		pygame.mouse.set_visible(False)
		stats.game_active = True
		stats.reset_stats()
		
		board.prep_level()
		board.prep_score()
		board.prep_high_score()
		board.prep_ship()
		
		aliens.empty()
		bullets.empty()
			
def check_keydown_events(event,setting,screen,ship,bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(setting,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		
def check_keyup_events(event,ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
		
def update_screen(setting,screen,stats,ship,bullets,aliens,button,board):
	screen.fill(setting.bg_color)	#create screen bg color
	for bullet in bullets.sprites():
		bullet.draw()
	ship.blitme()
	aliens.draw(screen)
	board.show_score()
	
	if not stats.game_active: 
		button.draw_button()
		
	pygame.display.flip()


def create_fleet(setting,screen,ship,aliens,stats):
	"""Create a full fleet of Aliens"""
	
	alien = Alien(screen,setting,stats)
	number_aliens_x = get_number_aliens_x(setting,alien.rect.width)
	number_rows = get_number_rows(setting,ship.rect.height,alien.rect.height)
	
	for row_num in range(number_rows):
		for num in range(number_aliens_x):
			create_alien(screen,setting,num,row_num,aliens,stats)

def get_number_rows(setting,ship_height,a_height):
	available_height = setting.screen_height - ship_height -(3*a_height)
	number_rows = int(available_height / (2*a_height))
	return number_rows
	
def get_number_aliens_x(setting,a_width):
	available_x = setting.screen_width - a_width
	number_aliens_x =int( available_x / (2 * a_width) )
	return number_aliens_x

def create_alien(screen,setting,num,row_num,aliens,stats):
	alien = Alien(screen,setting,stats)
	alien.x = (0.5*alien.rect.width) + (num*1.7* alien.rect.width)
	alien.rect.y = alien.rect.height + (row_num*2 * alien.rect.height)
	alien.rect.x = alien.x
	aliens.add(alien)
	
def check_fleet_edges(setting,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			drop_and_change_direction(setting,aliens)
			break
			
def drop_and_change_direction(setting,aliens):
	""" Drop the rows simulataneously and change direction of fleet"""
	for alien in aliens.sprites():
		alien.rect.y += setting.fleet_drop_speed
	setting.fleet_direction *= -1

def update_aliens(setting,screen,ship,aliens,bullets,stats,board):
	"""Update position of aliens in realtime"""
	check_fleet_edges(setting,aliens)
	aliens.update()
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(setting,screen,ship,aliens,bullets,stats,board)
		
	#Incase the aliens reach bottom of the screen.
	check_bottom(setting,screen,ship,aliens,bullets,stats,board)
	
def check_bottom(setting,screen,ship,aliens,bullets,stats,board):
	"""To check if any alien has reached bottom of window"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(setting,screen,ship,aliens,bullets,stats,board)
			break
		
def ship_hit(setting,screen,ship,aliens,bullets,stats,board):
	""" Act on ShipĀlien Collisions"""
	
	if stats.ships_left > 0:
		stats.ships_left -= 1
		board.prep_ship()
		
		#Clear aliens,bullets and ship and create new fleet.
		aliens.empty()
		bullets.empty()
		
		create_fleet(setting,screen,ship,aliens,stats)
		ship.center_ship()
		sleep(2)
		
	else:
		pygame.mouse.set_visible(True)
		stats.game_active = False

def update_bullets(setting, screen, stats, ship, aliens, bullets,board):
	"""Remove Disappeared bullets from sprites"""
	# Get rid of bullets that have disappeared.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_ab_collisions(setting, screen,stats, ship, aliens, bullets,board)
		
		
def check_high_score(stats,board):
	"""Check if current score> high score"""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		board.prep_high_score()

def check_ab_collisions(setting, screen, stats, ship, aliens, bullets,board):
	"""Check for collisions with aliens and remove both"""
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if collisions:
		for aliens in collisions.values():
			stats.score += setting.alien_points * len(aliens)
			board.prep_score()
		check_high_score(stats,board)

	if len(aliens) == 0:
		bullets.empty()
		setting.increase_speed()
		
		board.prep_level()
		stats.level += 1
		
		create_fleet(setting,screen,ship,aliens,stats)


def fire_bullet(setting,screen,ship,bullets):
	"""Fires a bullet if max limit not reached"""
	if len(bullets) <setting.bullets_max:
			new_bullet = Bullet(setting,screen,ship)
			bullets.add(new_bullet)
