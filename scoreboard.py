import pygame.font;
from pygame.sprite import Group;
from ship import Ship;

class Scoreboard():
    def __init__(self, ai_config, screen, statistics):
        self.screen = screen;
        self.screen_rect = screen.get_rect();
        self.ai_config = ai_config;
        self.statistics = statistics;

        # Font adjustment 
        self.text_color = (30,30,30);
        self.font = pygame.font.SysFont(None,48);
        
        #Set initial score image
        self.set_score();
        self.set_highest_score();
        self.set_level();
        self.set_ships();
    
    def set_level(self):
        self.level_image = self.font.render(str(self.statistics.level),True,self.text_color,self.ai_config.bgColor);

        self.level_rect = self.level_image.get_rect();
        self.level_rect.right = self.screen_rect.right - 20;
        self.level_rect.top = self.score_rect.bottom + 10;
        

    def set_highest_score(self):
        high_score = int(round(self.statistics.high_score,-1));
        high_score_str = "{:,}".format(high_score);
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_config.bgColor);

        # Display score (Top-right on screen)
        self.high_score_rect =  self.high_score_image.get_rect();
        self.high_score_rect.centerx = self.screen_rect.centerx;
        self.high_score_rect.top = self.score_rect.top;

    def set_score(self):
        """Convert score to a render"""
        rounded_score = int(round(self.statistics.score,-1));
        score_str = "{:,}".format(rounded_score);
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_config.bgColor);

        # Display score (Top-right on screen)
        self.score_rect =  self.score_image.get_rect();
        self.score_rect.right = self.screen_rect.right - 20;
        self.score_rect.top = 20;
    
    def set_ships(self):
        self.ships = Group();
        for ns in range(self.statistics.remain_ships):
            ship = Ship(self.ai_config,self.screen);
            ship.rect.x = 10 + ns * ship.rect.width;
            ship.rect.y = 10;
            self.ships.add(ship);

    def display_score(self):
        """Draw score on screen"""
        self.screen.blit(self.score_image,self.score_rect);
        self.screen.blit(self.high_score_image,self.high_score_rect);
        self.screen.blit(self.level_image,self.level_rect);
        self.ships.draw(self.screen);
