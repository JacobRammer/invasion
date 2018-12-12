import pygame.font


class Scoreboard():
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

        # prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """turn the score into an image"""
        score_str = str(self.stats.score)  # convert score to string
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)  # turn score_str into an image

        # display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20  # 20 pixels from the rightmost edge
        self.score_rect.top = 20  # 20 px from top of screen

    def show_score(self):
        """draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
