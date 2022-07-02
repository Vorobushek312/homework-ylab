from statistics import pstdev
import sys
import pygame
from backgraund import Background
from step import Step
from alien import Alien
import random


def check_event(ai_settings, screen, stats, play_button,  player_x, aliens, steps):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            check_play_button(aliens, steps, stats, play_button, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN and stats.game_active:
            if event.key == pygame.K_RIGHT:
                if player_x.rect.right < player_x.screen_rect.right:
                    player_x.rect.centerx += 120
            elif event.key == pygame.K_LEFT:
                if player_x.rect.left > 0:
                    player_x.rect.centerx -= 120
            elif event.key == pygame.K_UP:
                if player_x.rect.top > 0:
                    player_x.rect.bottom -= 80
            elif event.key == pygame.K_DOWN:
                if player_x.rect.bottom < player_x.screen_rect.bottom:
                    player_x.rect.bottom += 80
            elif event.key == pygame.K_SPACE:
                new_step = Step(ai_settings, screen, player_x)
                if pygame.sprite.spritecollideany(new_step, steps, collided = None) == None:
                    if pygame.sprite.spritecollideany(new_step, aliens, collided = None) == None:
                        steps.add(new_step)
                        while True:
                            new_alien = Alien(ai_settings, screen)
                            if pygame.sprite.spritecollideany(new_alien, steps, collided=None) == None:
                                if pygame.sprite.spritecollideany(new_alien, aliens, collided=None) == None:
                                    aliens.add(new_alien)
                                    break
                            elif pygame.sprite.spritecollideany(new_alien, aliens, collided=None) == None:
                                if pygame.sprite.spritecollideany(new_alien, steps, collided=None) == None:
                                    aliens.add(new_alien)
                                    break
            elif event.key == pygame.K_q:
                sys.exit()
                


def update_screen(ai_settings, screen, stats, player_x, aliens, steps, play_button):
    BackGround = Background('images/fon_pole.bmp', [0,0])
    screen.fill(ai_settings.bg_color)
    screen.blit(BackGround.image, BackGround.rect)
    for step in steps.sprites():
        step.blitme()
    player_x.blitme()
    for alien in aliens.sprites():
        alien.blitme()
    if not stats.game_active:
        play_button.draw_button()  
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()


def random_place():
    x = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080]
    y = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720]

    return [random.choice(x), random.choice(y)]
def check_play_button(aliens, steps, stats, play_button, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: 
        # if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        aliens.empty()
        steps.empty()
        
def chek_win(aliens, steps, loss_combo, stats):
    all_steps = []
    check_loss = False
    for step in steps.sprites():
        one_step = []
        one_step.append(step.rect.x)
        one_step.append(step.rect.y)
        all_steps.append(one_step)
    for combo in loss_combo:
        if check_loss == True:
            break
        for combo_one in combo:
            if combo_one in all_steps:
                check_loss = True
                continue
            else:
                check_loss = False
                break
            
    if check_loss == True:
        stats.game_active = False
