"""
    This object will managed the sound effect of Alien Invasion.
"""
import pygame

class AiSound():
    """
    This sound class object will provide the various sound effects
    for different event that happen during the game.
    """
    
    def __init__(self):
        """Initialize and load the different sound effects."""
        self.blasting = pygame.mixer.Sound('game_sounds/weapon_player.wav')
        self.alien_approaching = pygame.mixer.Sound('game_sounds/alien.wav')
        self.alien_exploding = pygame.mixer.Sound(
                                    'game_sounds/explosion_enemy.wav')
        
        # Set the volume for each type of sound.
        self.alien_approaching.set_volume(0.4)
        self.blasting.set_volume(0.5)
        self.alien_exploding.set_volume(0.2)
        
        # ~ self.blasting.fadeout(500)
        # ~ self.alien_approaching.fadeout(500)
        # ~ self.alien_exploding.fadeout(500)
    
    def play_blasting(self):
        """Play the ship firing sound effect."""
        self.blasting.play()
        self.alien_exploding.stop()

    def play_alien(self):
        """Play the alien enemy sound effect."""
        self.alien_approaching.play()
        self.alein_exploding.stop()
        self.blasting.stop()
                
    def play_enemy_exploding(self):
        """Play the sound of an alien exploding."""
        self.alien_exploding.play()
        self.blasting.stop()
