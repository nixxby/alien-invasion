import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	"""main function to run the game and create a screen instance.""" 
	pygame.init()

	#create an instance of Settings class.
	game_setting = Settings()
	
	screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")	#Give screen caption
	
	#create an instance of Ship Class
	game_ship = Ship(screen,game_setting)
	bullets = Group()
	
	# Main loop that contains the game.
	while True:
		gf.check_events(game_setting,screen,game_ship,bullets)
		game_ship.update_ship()
		bullets.update()
		gf.update_bullets(bullets)
		gf.update_screen(game_setting,screen,game_ship,bullets)


run_game()
