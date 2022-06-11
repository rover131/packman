import pygame
from pygame.sprite import Sprite
from random import randint


class Enemy(Sprite):  # враги
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        """загрузка изображения"""
        self.image = pygame.image.load('images/ghost.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self, direc):
        if direc == 0 and self.rect.x < 950:
            self.rect.x += 1
        elif direc == 1 and self.rect.x > 50:
            self.rect.x -= 1
        if direc == 2 and self.rect.y < 550:
            self.rect.y += 1
        if direc == 3 and self.rect.y > 50:
            self.rect.y -= 1


