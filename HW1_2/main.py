import imp
import sys
import pygame
from settings import Settings
from game_stats import GameStats
from button import Button
from backgraund import Background
from player_x import Player_x
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from loss_combinations import loss_combo_2

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("x and 0")
    play_button = Button(ai_settings, screen, "Play")
    player_x = Player_x(screen)
    steps = Group()
    aliens = Group()
    stats = GameStats(ai_settings)
    # df.create_fleet(ai_settings, screen, aliens)
    # alien = Alien(ai_settings, screen)
    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_event(ai_settings, screen, stats, play_button, player_x, aliens, steps, loss_combo_2)
        
        # При каждом проходе цикла перерисовывается экран.
        gf.update_screen(ai_settings, screen, stats,  player_x, aliens, steps,  play_button)

        gf.chek_win(aliens, steps, loss_combo_2, stats)
        
run_game()