import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_events(ai_settings, screen, ship, bullets):
    # watch for keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if player clicks on quit
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # if key is pressed
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update images on the screen and flip to the new screen"""

    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # blit means draw
    aliens.draw(screen)  # blit means draw

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to key presses"""
    # TODO add WASD capabilities

    if event.key == pygame.K_RIGHT:  # right arrow press
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  # left arrow press
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # if space is pressed
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # exit the game when q is pressed
        # TODO after adding WASD, change this button
        sys.exit()


def check_keyup_events(event, ship):
    """responds to key releases"""
    # TODO add WASD capabilities

    if event.key == pygame.K_RIGHT:  # right arrow release
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:  # left arrow released
        ship.moving_left = False


def play_music():
    """play music"""
    # TODO add credits for music usage

    pygame.mixer.pre_init(44100, -16, 2, 4096)  # start mixer with default pygame parameters

    pygame.init()
    pygame.mixer.music.load("music/track1.mp3")
    pygame.mixer.music.set_volume(.05)  # from 0 to 1
    pygame.mixer.music.play(-1)  # loop music


def update_bullets(bullets):
    """update position of bullets and get rid of bullets that have gone off screen"""

    # update bullet positions
    bullets.update()
    # get rid of bullets that have gone off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached"""
    # create a new bullet and add it to the bullet group
    new_bullet = Bullet(ai_settings, screen, ship)
    if len(bullets) < ai_settings.bullets_allowed:
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens):
    """create a fleet of aliens"""
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to 1 alien width
    alien = Alien(ai_settings, screen)  # get the size of the alien
    alien_width = alien.rect.width  # get the width of the image rect and store it
    available_space_x = ai_settings.screen_width - 2 * alien_width  # calculate the horizontal space available for alien
    numbers_aliens_x = int(available_space_x / (2 * alien_width))  # calculate how many whole aliens can fit

    # create the first row of aliens
    for alien_number in range(numbers_aliens_x):
        # TODO optimize this loop
        # create an alien and place it in a row
        alien = Alien(ai_settings, screen)  # create new alien
        alien.x = alien_width + 2 * alien_width * alien_number  # set x-cord
        alien.rect.x = alien.x
        aliens.add(alien)
        print(numbers_aliens_x)

