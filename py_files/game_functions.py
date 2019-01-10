import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


# TODO make aliens shoot bullets at ship
#   add total kill counter

# sb = scoreboard


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """look for keyboard events"""

    # watch for keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if player clicks on quit
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # if key is pressed
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # detect when mouse button is pressed
            mouse_x, mouse_y = pygame.mouse.get_pos()  # get position of the cursor
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                              bullets, mouse_x, mouse_y)  # call function to check if cursor is on button


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """update images on the screen and flip to the new screen"""

    # redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()  # blit means draw
    aliens.draw(screen)  # blit means draw

    # redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    sb.show_score()  # draw the score information

    # draw the play button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """respond to key presses"""

    # TODO add WASD capabilities
    #   Sound FX for shooting, crashes, etc. (new function for FX)
    #   add "P" as play key

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


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update position of bullets and get rid of bullets that have gone off screen"""

    # update bullet positions
    bullets.update()
    # get rid of bullets that have gone off screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            sleep(.02)

    # check for bullet collision events
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """respond to bullets and alien collisions"""

    # check for alien-bullet collision
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # if bullet-alien collision true, delete both

    if collisions:  # bullet - alien collide
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)  # to make sure all collisions are scored
            sb.prep_score()
            sleep(.01)
        check_high_score(stats, sb)

    # check to see if all aliens have been destroyed
    if len(aliens) == 0:
        # destroy existing bullets, speed up the game, and create new alien fleet & start new level
        bullets.empty()  # delete bullets on screen
        ai_settings.increase_speed()  # increase speed when aliens destroyed

        # increase level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)  # create new fleet


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


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update the positions of all aliens in the fleet then drop"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # look fro aliens hitting the bottom of the screen
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # alien-ship collision
    if pygame.sprite.spritecollideany(ship, aliens):  # if any alien collides with the ship
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """shift if aliens touch edge of screen"""

    sleep(.00001)
    for alien in aliens.sprites():  # loop through all aliens on screen
        if alien.check_edges():  # if alien is touching edge
            change_fleet_direction(ai_settings, aliens)  # change the fleet direction
            break


def change_fleet_direction(ai_settings, aliens):
    """drop the entire fleet and change the direction"""
    for alien in aliens.sprites():  # loop through all aliens
        alien.rect.y += ai_settings.fleet_drop_speed  # and drop them
    ai_settings.fleet_direction *= -1  # reverse the direction


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """respond to shit being hit by an alien"""

    if stats.ships_left > 0:
        # if ship hit, take one away from ship_limit
        stats.ships_left -= 1

        # update scoreboard
        sb.prep_ships()

        aliens.empty()  # delete aliens from screen
        bullets.empty()  # delete bullets from screen

        # create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # pause
        sleep(.05)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)  # make cursor visible


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """check if any of the aliens have reached the bottom of the screen"""

    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # treat this the same as if the ship got hit
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)  # reset screen
            break


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """start a new game when the player clicks on the button"""

    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)  # True if button clicked. Else: False
    if button_clicked and not stats.game_active:  # if button clicked is true and game is not active
        stats.reset_stats()  # reset the player statistics
        stats.game_active = True  # set status True to start game

        # reset the scoreboard images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        pygame.mouse.set_visible(False)  # hide the cursor once the game starts
        ai_settings.initialize_dynamic_settings()  # reset the game's settings

        # empty the screen from previous sessions
        aliens.empty()
        bullets.empty()

        # create a new fleet and center the ship
        create_fleet(ai_settings, screen, ship, aliens)  # create a new alien fleet
        ship.center_ship()  # center the ship


def check_high_score(stats, sb):
    """check to see if there's a new high score"""

    if stats.score > stats.high_score:  # check current score against high score
        stats.high_score = stats.score  # change high score
        sb.prep_high_score()
