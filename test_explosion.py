"""
   Test run for animating an explosion.
"""
import sys
import random
from time import sleep

import pygame
from pygame.sprite import Group

from explosion import Explosion

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BG_COLOR = (230, 230, 230)
CENTER = (200, 200)

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    screen = pygame.display.set_mode(
                (
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )
    
    pygame.display.set_caption("Explosion")
    
    # Make explosion animation
    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = [] 
    
    for i in range(9):
        filename = 'regularExplosion0{}.png'.format(i)
        img = pygame.image.load("images/" + filename).convert()
        img.set_colorkey(BG_COLOR)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
        
    explosion_sprites = Group()
    # ~ random_explosion = int(random.random() * 20)
    # ~ if random_explosion in (1, 3, 5, 7):            
        # ~ expl = Explosion(explosion_anim, CENTER, 'lg')
        # ~ explosion_sprites.add(expl) 
 
    # Start the main loop for the game.
    running = True
    while running:        
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN :
                if event.key == pygame.K_e:                    
                    expl = Explosion(explosion_anim, CENTER, 'lg')
                    explosion_sprites.add(expl)
                    
                
        explosion_sprites.update(explosion_anim)
        explosion_sprites.draw(screen)        
        # Make the most recently draw screen visible.
        pygame.display.flip()
        
          
run_game()
