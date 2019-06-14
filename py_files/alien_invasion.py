import pygame
from settings import Settings
from ship import Ship, Ship2
import game_functions as gf
from game_functions import play_music
from time import sleep
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    play_music()

    #  Initialize game and create a screen object
    pygame.init()  # always needs to be at the beginning
    pygame.display.set_caption("Alien Invasion")  # name the windows in the top left corner

    # create objects

    ai_settings = Settings()
    # create an instance to store game statistics
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # create screen settings
    # TODO change window icon
    #   allow window to be resized
    sb = Scoreboard(ai_settings, screen, stats)
    # make a ship
    ship = Ship2(ai_settings, screen)  # using Ship2
    # make a group to store bullets in
    bullets = Group()  # Groups from import
    # make a group to store aliens
    aliens = Group()
    play_button = Button(ai_settings, screen, "Play")

    # end object creations

    """
    Create a fleet of aliens behind the play button.
    """
    gf.create_fleet(ai_settings, screen, ship, aliens)  # create a fleet of aliens may need to delete
    # event = pygame.event.get()
    if pygame.event == pygame.K_SPACE:
        stats.reset_stats
        stats.game_active = True
    # start main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # checks for KB/M activity

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            sleep(.0001)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)  # update sprite movement
        sleep(.015)  # limit while execution to limit CPU usage (seconds)


run_game()
