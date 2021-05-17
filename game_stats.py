"""
Tram Nguyen
CPSC 223P-01
Thu May 10, 2021
tnguyen3006@csu.fullerton.edu
"""

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
