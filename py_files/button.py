import pygame.font


class Button():
    """initialize button attributes"""

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set the dimensions and properties of the button
        self.width, self.height = 200, 50  # width and height of the button
        self.button_color = (0, 255, 0)  # color of the button (green)
        self.text_color = (255, 255, 255)  # color of the text (black)
        self.font = pygame.font.SysFont(None, 48)  # None = default font

        # build the button's rect object and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # create the button at (0,0)
        self.rect.center = self.screen_rect.center  # center on the screen

        # the button message needs to prepped only once
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """turn msg into a rendered image and center the text on the button"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)  # turns text to image. T/F: AA
        self.msg_image_rect = self.msg_image.get_rect()  # create rect for image text
        self.msg_image_rect.center = self.rect.center  # center the text image

    def draw_button(self):
        """draw blank button then draw message"""
        self.screen.fill(self.button_color, self.rect)  # draw button
        self.screen.blit(self.msg_image, self.msg_image_rect)  # draw text on button
