class Settings():
    """a class to store all settings for Alien Invasion"""
    def __init__(self):
        """initialize the game's settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240, 255, 255)

        # ship settings
        self.ship_speed_factor = 6.5  # speed of ship in px. originally 1.5

        # bullet settings
        self.bullet_speed_factor = 20  # originally 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # black
        self.bullets_allowed = 3
