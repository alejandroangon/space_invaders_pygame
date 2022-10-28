import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Handle shoot bullets by Ship"""
    def __init__(self, ai_config,screen,ship):
        super(Bullet, self).__init__();
        self.screen = screen;
        
        #create a bullet rect (0,0) then is placed in right position
        self.rect = pygame.Rect(0,0, ai_config.bullet_width,ai_config.bullet_height);
        self.rect.centerx = ship.rect.centerx;
        self.rect.top = ship.rect.top;
        
        #store bullet position as a decimal
        self.y=float(self.rect.y);

        self.color = ai_config.bullet_color;
        self.factor_bullet_speed = ai_config.factor_bullet_speed;
    
    def update(self):
        """ Moves bullet from bottom to top """
        # Refresh bullet position
        self.y -= self.factor_bullet_speed;

        # Refresh rect position
        self.rect.y = self.y;
    
    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen,self.color,self.rect);
