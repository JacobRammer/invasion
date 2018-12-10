import pygame
import os
from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set the starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        os.chdir("C:\\Users\\Jacob\\Documents\\invasion")
        # load teh image and set the rect attribute
        self.image = pygame.image.load("images/alien2.bmp")
        # self.image = pygame.transform.scale(self.image, (60, 40))  # scale picture without losing background transpar.
        self.rect = self.image.get_rect()

        # start each new alien near the top  left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move the alien right"""
        self.x += self.ai_settings.alien_speed_factor  * self.ai_settings.fleet_direction # move to the right
        self.rect.x = self.x  # update the rectangle of the moved image

    def check_edges(self):
        """return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:  # right of window (greater than equal to 1200)
            return True
        elif self.rect.left <= 0:  # left of window
            return True
