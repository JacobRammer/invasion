import pygame


class Ship:
    def __init__(self, screen):
        """initialize the ship and set its starting position"""
        self.screen = screen

        # load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")  # load ship image
        self.rect = self.image.get_rect()  # rect is a rectangle (google it) places at origin (top left)
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx  # center on x axis (modifying line 10)
        self.rect.bottom = self.screen_rect.bottom  # place sprite at bottom of window (modify line 10)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        if self.moving_right:  # if right key is pressed
            self.rect.centerx += 1

        if self.moving_left:  # if left arrow key is pressed
            self.rect.centerx -= 1

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)  # blit means draw. define image and position


class Ship2:
    def __init__(self, ai_settings, screen):
        """initialize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship's image and get its rect
        self.image = pygame.image.load("images/ship2.bmp")  # load ship image
        self.image = pygame.transform.scale(self.image, (60, 100))  # scale picture without losing background transpar.
        self.rect = self.image.get_rect()  # get the size of the image
        self.screen_rect = screen.get_rect()

        # set position of ship
        self.rect.centerx = self.screen_rect.centerx  # center x
        self.rect.bottom = self.screen_rect.bottom # place image on bottom

        # store decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on the movement flag"""
        # update the ships center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:  # if right arrow key is pressed
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:  # if left arrow key is pressed
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """center the ship on screen"""
        self.center = self.screen_rect.centerx
