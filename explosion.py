"""
    This class handle the Explosion of the alien ship.
"""
import pygame
from pygame.sprite import Sprite
    
class Explosion(Sprite):
    """Describe the Explosion in Alien Invasion."""
        
    def __init__(self, explosion_anim, center, size):        
        super(Explosion, self).__init__()
               
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50       
        
    def update(self, explosion_anim):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
       
