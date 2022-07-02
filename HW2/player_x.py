from turtle import Screen
import pygame

class Player_x():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/player_x.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        # Флаг перемещения
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)



