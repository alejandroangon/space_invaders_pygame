import pygame;
from pygame.sprite import Sprite;

class Ship(Sprite):
    def __init__(self, ai_config, pantalla):
        super(Ship,self).__init__();
        self.pantalla = pantalla;
        self.ai_config = ai_config;

        #Load ship image and get rect
        self.image = pygame.image.load("assets/ship.bmp");
        self.rect = self.image.get_rect();
        self.pantalla_rect = pantalla.get_rect();

        #Load each new ship in the middle of the screen
        self.rect.centerx = self.pantalla_rect.centerx;
        self.rect.bottom = self.pantalla_rect.bottom;

        #store decimal value for ship center
        self.center = float(self.rect.centerx);

        # mov flagS
        self.moving_right = False;
        self.moving_left = False;
    
    def update(self):
        """ refresh ship position by checking flag"""
        if self.moving_right and self.rect.right < self.pantalla_rect.right:
            self.center += self.ai_config.factor_ship_speed;

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_config.factor_ship_speed;

        # refresh rect object by self.center
        self.rect.centerx = self.center;
        
    def blitme(self):
        """ Draw ship in actual position """
        self.pantalla.blit(self.image, self.rect)
    
    def center_ship(self):
        self.center = self.pantalla_rect.centerx