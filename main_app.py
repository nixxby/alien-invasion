import pygame
from pygame.sprite import Group

from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from alien_invasion.game_stats import GameStats as GS
from alien_invasion.scoreboard import Scoreboard
from alien_invasion.button import Button

import alien_invasion.game_functions as gf

def run_game():
	"""main function to run the game and create a screen instance.""" 
	pygame.init()

	#create an instance of Settings class.
	game_setting = Settings()
	
	screen = pygame.display.set_mode((game_setting.screen_width,game_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")	#Give screen caption
	
	stats = GS(game_setting)
	board = Scoreboard(game_setting,screen,stats)
	
	#create an instance of Ship Class,Bullets & Aliens Group & fleet
	game_ship = Ship(screen,game_setting)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(game_setting,screen,game_ship,aliens,stats)
	play_button = Button(game_setting,screen,"Play")
	
	# Main loop that contains the game.
	while True:
		gf.check_events(game_setting,screen,game_ship,aliens,bullets,stats,play_button,board)
		
		if stats.game_active:
			game_ship.update_ship()
			bullets.update()
			gf.update_bullets(game_setting, screen, stats, game_ship, aliens, bullets,board)
			gf.update_aliens(game_setting,screen,game_ship,aliens,bullets,stats,board)
			
		gf.update_screen(game_setting,screen,stats,game_ship,bullets,aliens,play_button,board)


run_game()
