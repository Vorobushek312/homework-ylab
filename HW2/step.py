import pygame
from pygame.sprite import Sprite

class Step(Sprite):
    def __init__(self, ai_setting, screen, player_x):
        super(Step, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/player_x.bmp')
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x.rect.centerx
        self.rect.bottom = player_x.rect.bottom
    def draw_step(self):
        pygame.draw.rect(self.screen, self.rect, self.rect)
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    