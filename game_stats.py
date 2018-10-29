"""
    This class track the game statistics as player interactive with teh game.
"""

class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize Statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an active state.
        self.game_active = False
        self.game_pause = False
        self.game_won = False
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        # Maximum Game Play Level
        self.game_max_level = 10
        self.high_score = self.load_current_high_score()
        self.green_alien_destroyed = 0
        self.red_alien_destroyed = 0
        self.purple_alien_destroyed = 0

    def load_current_high_score(self):
        """Load the current highest score that was saved in a data file."""
        high_score = ''
        with open('game_data/current_high_score.txt') as score_data:
            high_score = score_data.read()
            high_score = int(high_score.strip())
        return high_score
