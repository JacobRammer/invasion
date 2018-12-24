import pygame.font
from pygame.sprite import Group
from ship import Ship2_Lives


class Scoreboard:
    """a class to report scoring information"""

    def __init__(self, ai_settings, screen, stats):
        """initialize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # fonts settings for score information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)  # default font

        # prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn the score into an image"""

        rounded_score = int(round(self.stats.score, -1))  # round to the nearest 10th value
        score_str = "{:,}".format(rounded_score)  # add commas to the score printed on screen
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)  # turn score_str into an image

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 20 pixels from the rightmost edge
        self.score_rect.top = 20  # 20 px from top of screen

    def show_score(self):
        """draw score and ships to the screen"""

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # draw ships
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """turn the high score into a rendered image"""

        high_score = int(round(self.stats.high_score, -1))  # round high score to nearest 10th value
        high_score_str = "{:,}".format(high_score)  # format score with commas
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()  # get rect of high score
        self.high_score_rect.centerx = self.screen_rect.centerx  # center high score on x axis
        self.high_score_rect.top = self.score_rect.top  # move high score to the top of the screen

    def prep_level(self):
        """turn the level into a rendered image"""

        # TODO fix ship score clipping

        # create an image from stats.level (game_stats)
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        # position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right  # set to the right
        self.level_rect.top = self.score_rect.bottom + 10  # 10 px below the score

    def prep_ships(self):
        """show how many ships are left"""

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):  # from settings.py
            ship = Ship2_Lives(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
