""" 
    This is a class use to hold initial settings information.
"""
import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        # self.alien_speed_factor *= self.speedup_scale        
        # self.alien_points = int(self.alien_points * self.score_scale)
        if  self.bullet_speed_factor < 8:
            self.bullet_speed_factor *= self.speedup_scale
    
    def increase_bullets_allowed(self):
        """Increase number of bullet allowed."""
        if self.bullets_allowed < 6:
            self.bullets_allowed += 1
        
    def increase_bullet_size(self):
        """Increase bullet size width and height."""
        self.bullet_width += 1
        self.bullet_height += 1
        
    def upgrade_weapon(self, rgb):
        """Change the bullet color and reset the width, height."""
        self.bullet_color = rgb
        self.bullet_width = 6
        self.bullet_height = 30
