import pygame
from settings import Settings
from ship import Ship, Ship2
import game_functions as gf
from game_functions import play_music
import time
from pygame.sprite import Group


# left off at page 298

def run_game():
    play_music()

    #  Initialize game and create a screen object
    pygame.init()  # always needs to be at the beginning
    pygame.display.set_caption("Alien Invasion")  # name the windows in the top left corner

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # create screen settings
    # TODO change window icon

    # make a ship
    ship = Ship2(ai_settings, screen)  # using Ship2
    # make a group to store bullets in
    bullets = Group()  # Groups from import
    # make a group to store aliens
    aliens = Group()

    # start main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # checks for KB/M activity
        # create a fleet of aliens
        gf.create_fleet(ai_settings, screen, aliens)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # update sprite movement
        time.sleep(.01)  # limit while execution to limit CPU usage (seconds)


run_game()
