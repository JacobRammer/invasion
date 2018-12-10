import sys
import pygame
from bullet import Bullet
from alien import Alien
import os


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
    os.chdir("C:\\Users\\Jacob\\Documents\\invasion")

    pygame.mixer.pre_init(44100, -16, 2, 4096)  # start mixer with default pygame parameters

    pygame.init()
    pygame.mixer.music.load("music/track1.mp3")
    pygame.mixer.music.set_volume(.05)  # from 0 to 1
    pygame.mixer.music.play(-1)  # loop music


def update_bullets(aliens, bullets):
    """update position of bullets and get rid of bullets that have gone off screen"""

    # update bullet positions
    bullets.update()
    # get rid of bullets that have gone off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # check for alien-bullet collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # if bullet collision true


def fire_bullet(ai_settings, screen, ship, bullets):
    """fire a bullet if limit not reached"""
    # create a new bullet and add it to the bullet group
    new_bullet = Bullet(ai_settings, screen, ship)
    if len(bullets) < ai_settings.bullets_allowed:
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """create a fleet of aliens"""
    # create an alien and find the number of aliens in a row
    # spacing between each alien is equal to 1 alien width
    alien = Alien(ai_settings, screen)  # get the size of the alien
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # calculate how many whole aliens can fit
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """determine the number of aliens that fit into a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width  # calculate the horizontal space available for alien
    numbers_aliens_x = int(available_space_x / (2 * alien_width))  # calculate how many whole aliens can fit

    return numbers_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and place in in the row"""
    alien = Alien(ai_settings, screen)  # get the size of the alien
    alien_width = alien.rect.width  # get the width of the image rect and store it
    alien.x = alien_width + 2 * alien_width * alien_number  # set x-cord
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    """determine the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows


def update_aliens(ai_settings, aliens):
    """update the positions of all aliens in the fleet then drop"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


def check_fleet_edges(ai_settings, aliens):
    """shift if aliens touch edge of screen"""
    for alien in aliens.sprites():  # loop through all aliens on screen
        if alien.check_edges():  # if alien is touching edge
            change_fleet_direction(ai_settings, aliens)  # change the fleet direction
            break


def change_fleet_direction(ai_settings, aliens):
    """drop the entire fleet and change the direction"""
    for alien in aliens.sprites():  # loop through all aliens
        alien.rect.y += ai_settings.fleet_drop_speed  # and drop them
    ai_settings.fleet_direction *= -1  # reverse the direction
