import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """a class to represent a single alien"""

    def __init__(self, ai_settings, screen):
        """initialize the alien and set the starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load teh image and set the rect attribute
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image, (40, 20))  # scale picture without losing background transpar.
        self.rect = self.image.get_rect()

        # start each new alien near the top  left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the alien at its current position"""
        self.screen.blit(self.image, self.rect)
