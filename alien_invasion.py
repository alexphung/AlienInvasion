import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
from game_won import GameWon
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode(
                (
                    ai_settings.screen_width,
                    ai_settings.screen_height
                )
            )
    pygame.display.set_caption("Alien Invasion")
    
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")
    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    aliens = Group()
    
    # Make explosion animation
    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = [] 
    
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load("images/" + filename).convert()
        img.set_colorkey((0,0,0))
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
    
    # Make explosion animation     
    explosion_sprites = Group()
    
    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)    
    
    # Start the main loop for the game.
    while True:       
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, 
            ship, aliens, bullets)
            
        if not stats.game_won: 
            if stats.game_active and not stats.game_pause:        
                ship.update()	    	         
                gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                    aliens, bullets, explosion_anim, explosion_sprites)
                gf.update_aliens(ai_settings, screen, stats, sb, ship, 
                    aliens, bullets)            
                explosion_sprites.update(explosion_anim)                
            # Redraw the screen during each pass through the loop.
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
                bullets, play_button, explosion_sprites)
        else:
            # Create a game won screen.    
            game_won = GameWon(screen)
            game_won.draw_message()
            # Make the most recently draw screen visible.
            pygame.display.flip()
            
        
          
run_game()
