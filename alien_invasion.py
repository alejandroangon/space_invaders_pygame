import pygame;
from pygame.sprite import Group;
from settings import Settings;
from ship import Ship;
from statistics import Statistics;
from scoreboard import Scoreboard;
from button import Button;
import game_functions as gf;


def run_game():
    #init game, settings, and create an object screen
    pygame.init();
    _ai_config = Settings();
    _screen = pygame.display.set_mode((_ai_config.screen_width,_ai_config.screen_height));
    pygame.display.set_caption("👽 Invasion alien 👽");

    #Create play button 
    _play_button = Button(_ai_config, _screen, "Play")

    #Create an instance to store game statistics and create a scoreboard
    _statistics = Statistics(_ai_config);
    _scoreboard = Scoreboard(_ai_config,_screen,_statistics)
    
    #Create ship,bullets,aliens
    _ship = Ship(_ai_config,_screen);
    _bullets = Group();
    _aliens = Group();

    #Create ufo fleet
    gf.create_ufos(_ai_config,_screen,_ship,_aliens);

    #main loop in game
    while True:

        #listen keyboard or mouse events
        gf.check_events(_ai_config,_screen,_statistics,_scoreboard,_play_button,_ship,_aliens,_bullets);

        if _statistics.game_active:    
            _ship.update();
            gf.update_bullets(_ai_config,_screen,_statistics,_scoreboard,_ship,_aliens,_bullets);
            gf.update_aliens(_ai_config,_statistics,_screen,_scoreboard,_ship,_aliens,_bullets);
        gf.refresh_screen(_ai_config ,_screen,_statistics,_scoreboard ,_ship,_aliens,_bullets,_play_button);


        
run_game();