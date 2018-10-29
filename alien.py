"""
    Creating the Alien object.
"""
import random

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute.
        random_alien = int(random.random() * 20)
        if random_alien in (3, 5, 7):
            self.image = pygame.image.load('images/purplealien.bmp')
            self.id = 3
        elif random_alien % 2 != 0:
            self.image = pygame.image.load('images/redalien.bmp')
            self.id = 2
        else:
            self.image = pygame.image.load('images/greenalien.bmp')
            self.id = 1
            
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor * 
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        
