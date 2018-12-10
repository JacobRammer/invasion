class Settings():
    """a class to store all settings for Alien Invasion"""
    def __init__(self):
        """initialize the game's settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed_factor = 6.5  # speed of ship in px. originally 1.5

        # bullet settings
        self.bullet_speed_factor = 20  # originally 1
        self.bullet_width = 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # black
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed_factor = 1
        # move aliens down on edge collide
        self.fleet_drop_speed = 10  # drop distance in px
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
