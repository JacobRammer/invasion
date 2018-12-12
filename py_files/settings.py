class Settings():
    """a class to store all settings for Alien Invasion"""

    def __init__(self):
        """initialize the game's static settings"""

        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_limit = 2  # 3 lives

        # bullet settings
        self.bullet_width = 2  # originally 2
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # black
        self.bullets_allowed = 3

        # move aliens down on edge collide
        self.fleet_drop_speed = 10  # drop distance in px

        # how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initialize settings that change throughout the game"""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 15

        # alien settings
        self.alien_speed_factor = 3

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
