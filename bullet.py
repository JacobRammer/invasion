import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """a class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullrect rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # move the bullet to the top of the window with ship
        self.rect.top = ship.rect.top  # set the bullet to the tip of the ship

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color  # store color
        self.speed_factor = ai_settings.bullet_speed_factor  # store speed

    def update(self):
        """move the bullet up the screen"""

        # update the decimal position of the bullet
        self.y -= self.speed_factor  # -= because the y value decreased at the top of the screen
        # update the rect position
        self.rect.y = self.y  # keep the y value the same

    def draw_bullet(self):
        """draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
