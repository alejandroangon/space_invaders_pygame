import pygame;
from pygame.sprite import Sprite;

class Alien(Sprite):
    """Single alien"""
    def __init__(self, ai_config, screen):
        """Init alien set initial position"""
        super(Alien, self).__init__()
        self.screen = screen;
        self.ai_config = ai_config;

        #load image and set rect property
        self.image = pygame.image.load("assets/alien.bmp");
        self.rect = self.image.get_rect();

        self.rect.x = self.rect.width;
        self.rect.y = self.rect.height;

        #store alien position
        self.x = float(self.rect.x);

    def blitme(self):
        """draw alien current position"""
        self.screen.blit(self.image,self.rect);
    
    def check_edges(self):
        """True if alien is on any edge"""
        screen_rect = self.screen.get_rect();
        if self.rect.right >= screen_rect.right:
            return True;
        elif self.rect.left <= 0:
            return True;
    
    def update(self):
        """Move ufo (right)"""
        self.x += (self.ai_config.factor_alien_speed * self.ai_config.fleet_direction);
        self.rect.x = self.x;
