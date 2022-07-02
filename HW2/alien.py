import pygame
from pygame.sprite import Sprite
import game_functions as gf
class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/player_o.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = gf.random_place()[0]
        self.rect.y = gf.random_place()[1]
        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)