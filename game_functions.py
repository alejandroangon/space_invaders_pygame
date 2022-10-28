import sys;
import pygame;
from bullet import Bullet;
from alien import Alien;
from time import sleep

from scoreboard import Scoreboard

def check_events_keydown(event, ai_config, screen, ship, bullets):
    """Reply to keydown """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  True;
    elif event.key == pygame.K_SPACE:
        shoot(ai_config,screen,ship,bullets);
    elif event.key == pygame.K_q:
        sys.exit();
        
    
def check_events_keyup(event, ship):
    """Reply to keydown """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left =  False;

def check_events(ai_config, screen,statistics,scoreboard,play_button,ship,aliens, bullets):
    """ reply to mouse/keyboards actions """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();

        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event,ai_config,screen,ship,bullets);

        elif event.type == pygame.KEYUP:
            check_events_keyup(event,ship);
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = pygame.mouse.get_pos();
            check_play_button(ai_config,screen,statistics,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y);

def check_play_button(ai_config,screen,statistics,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """Start a new game if player clicks button"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not statistics.game_active:
        # Restart game stats
        ai_config.dynamic_settings_init();
        # Hide cursor
        pygame.mouse.set_visible(False)
        #Restart game statistics
        statistics.reset_stats();
        statistics.game_active = True;

        #Reset scoreboard images
        scoreboard.set_score();
        scoreboard.set_highest_score();
        scoreboard.set_level();
        scoreboard.set_ships();

        # Empty aliens and bullets list
        aliens.empty();
        bullets.empty();

        #Create a new fleet
        create_ufos(ai_config,screen,ship,aliens);
        ship.center_ship();

def refresh_screen(ai_config, screen,statistics, scoreboard, ship, aliens, bullets, play_button):
    """ Refresh images on screen and send to new screen """
    screen.fill(ai_config.bgColor); 
    # Draws again all bullets behind ship and ufos
    for bullet in bullets.sprites():
        bullet.draw_bullet();
    ship.blitme();
    aliens.draw(screen);

    #Draw scoreboard information
    scoreboard.display_score();

    #Draw play button if game isn't active
    if not statistics.game_active:
        play_button.draw_button();

        #display lastest drawn screen
    pygame.display.flip();


def update_bullets(ai_config,screen,statistics,scoreboard,ship,aliens,bullets):
    """ update bullets position and delete """
    bullets.update();
    #Delete bullets passing top of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet);
    check_bullet_alien_collisions(ai_config,screen,statistics,scoreboard,ship,aliens,bullets);


def check_bullet_alien_collisions(ai_config,screen,statistics,scoreboard,ship,aliens,bullets):
    #check if any bullet have reached any ufo
    collisions = pygame.sprite.groupcollide(bullets,aliens, True,True);

    if collisions:
        for aliens in collisions.values():
            statistics.score += ai_config.points_alien * len(aliens);
            scoreboard.set_score();
        check_high_score(statistics,scoreboard);

    if len(aliens) == 0:
        bullets.empty();
        ai_config.increase_speed();

        #increase level
        statistics.level +=1;
        scoreboard.set_level();

        create_ufos(ai_config,screen,ship,aliens);

def check_high_score(statistics, scoreboard):
    if statistics.score > statistics.high_score:
        statistics.high_score = statistics.score;
        scoreboard.set_highest_score();
    pass;

def get_number_aliens_x(ai_config, alien_width):
    """Calculate aviable number of aliens in a row"""
    available_space_x = ai_config.screen_width - 2 * alien_width;
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x;

def get_number_rows(ai_config, ship_height, alien_height):
    """Calculate how many ufos (rows) fits on screen"""
    available_space_y = (ai_config.screen_height - (3*alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows;

def shoot(ai_config, screen, ship, bullets):
    """Shoot a bullet if user haven't reach the limit"""
    #Create a new bullets and add into bullets group
    if len(bullets)<ai_config.bullet_allowed:
        _new_bullet = Bullet(ai_config,screen, ship);
        bullets.add(_new_bullet);

def create_alien(ai_config,screen,aliens, alien_number, row_number):
    """create an alien and iserts into row"""
    alien = Alien(ai_config,screen);
    alien_width = alien.rect.width;
    alien.x=alien_width + 2 * alien_width * alien_number;
    alien.rect.x = alien.x;
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number;
    aliens.add(alien);

def create_ufos(ai_config,screen,ship,aliens):
    """Create a fleet of ufos"""
    #Create new alien and find number of aliens straight
    #Space beetwen alien equals to alien width
    alien = Alien(ai_config,screen);
    number_aliens_x = get_number_aliens_x(ai_config,alien.rect.width);
    number_rows = get_number_rows(ai_config,ship.rect.height,alien.rect.height);

    #create 1st alien row
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_config,screen,aliens,alien_number,row_number);

def check_fleet_edges(ai_config, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_config,aliens);
            break;

def change_fleet_direction(ai_config,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_config.fleet_drop_speed;
    ai_config.fleet_direction *= -1;
    
def ship_reached(ai_config,statistics,screen,scoreboard,ship,aliens,bullets):
    if statistics.remain_ships > 0:
        statistics.remain_ships -= 1;

        scoreboard.set_ships();

        aliens.empty();
        bullets.empty();
        
        #creates a new fleet and creates another ship
        create_ufos(ai_config,screen,ship,aliens);
        ship.center_ship();

        #pause
        sleep(0.5);
    else:
        statistics.game_active = False;
        pygame.mouse.set_visible(True);

def check_aliens_bottom(ai_config,statistics,screen,scoreboard,ship,aliens,bullets):
    screen_rect = screen.get_rect();

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_reached(ai_config,statistics,screen,scoreboard,ship,aliens,bullets);
            break


def update_aliens(ai_config,statistics,screen,scoreboard,ship, aliens,bullets):
    """Update all ufo fleet"""
    check_fleet_edges(ai_config,aliens);
    aliens.update();

    #check any collision ufo-ship
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_reached(ai_config,statistics,screen,scoreboard,ship,aliens,bullets);

    check_aliens_bottom(ai_config,statistics,screen,scoreboard,ship,aliens,bullets);