import pygame
import time


class Hero:
    def __init__(self, ai_game):
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        # пакмен и начальная позиция
        self.walk_r = [pygame.image.load('images/pac_r1.bmp'), pygame.image.load('images/pac_r2.bmp'),
                       pygame.image.load('images/pac_r3.bmp')]
        self.walk_l = [pygame.image.load('images/pac_l1.bmp'), pygame.image.load('images/pac_l2.bmp'),
                       pygame.image.load('images/pac_r3.bmp')]
        self.walk_d = [pygame.image.load('images/pac_d1.bmp'), pygame.image.load('images/pac_d2.bmp'),
                       pygame.image.load('images/pac_r3.bmp')]
        self.walk_u = [pygame.image.load('images/pac_u1.bmp'), pygame.image.load('images/pac_u2.bmp'),
                       pygame.image.load('images/pac_r3.bmp')]
        self.rect = self.walk_r[0].get_rect()
        self.rect.center = self.screen_rect.center
        self.time_ = time.perf_counter()
        self.mov = 0

        """Флаги для непрерывного движения"""
        self.mov_right = False
        self.mov_left = False
        self.mov_up = False
        self.mov_down = False

    def update(self):
        if self.mov_right and self.rect.right < self.screen_rect.right - 5 and not self.mov_up and not self.mov_down:
            self.rect.x += 10
        if self.mov_left and self.rect.left > 5 and not self.mov_up and not self.mov_down:
            self.rect.x -= 10
        if self.mov_up and self.rect.y > 5:
            self.rect.y -= 10
        if self.mov_down and self.rect.bottom < self.screen_rect.bottom - 5:
            self.rect.y += 10

    def blitme(self):
        if time.perf_counter() - self.time_ > 1:
            self.time_ = time.perf_counter()
        if self.mov == 0:
            if 0.25 <= time.perf_counter() - self.time_ < 0.5:
                self.screen.blit(self.walk_r[2], self.rect)
            elif 0 <= time.perf_counter() - self.time_ < 0.25 or 0.5 <= time.perf_counter() - self.time_ < 0.75:
                self.screen.blit(self.walk_r[1], self.rect)
            elif 0.75 <= time.perf_counter() - self.time_ < 1:
                self.screen.blit(self.walk_r[0], self.rect)
        elif self.mov == 1:
            if 0.25 <= time.perf_counter() - self.time_ < 0.5:
                self.screen.blit(self.walk_l[2], self.rect)
            elif 0 <= time.perf_counter() - self.time_ < 0.25 or 0.5 <= time.perf_counter() - self.time_ < 0.75:
                self.screen.blit(self.walk_l[1], self.rect)
            elif 0.75 <= time.perf_counter() - self.time_ < 1:
                self.screen.blit(self.walk_l[0], self.rect)
        elif self.mov == 2:
            if 0.25 <= time.perf_counter() - self.time_ < 0.5:
                self.screen.blit(self.walk_u[2], self.rect)
            elif 0 <= time.perf_counter() - self.time_ < 0.25 or 0.5 <= time.perf_counter() - self.time_ < 0.75:
                self.screen.blit(self.walk_u[1], self.rect)
            elif 0.75 <= time.perf_counter() - self.time_ < 1:
                self.screen.blit(self.walk_u[0], self.rect)
        elif self.mov == 3:
            if 0.25 <= time.perf_counter() - self.time_ < 0.5:
                self.screen.blit(self.walk_d[2], self.rect)
            elif 0 <= time.perf_counter() - self.time_ < 0.25 or 0.5 <= time.perf_counter() - self.time_ < 0.75:
                self.screen.blit(self.walk_d[1], self.rect)
            elif 0.75 <= time.perf_counter() - self.time_ < 1:
                self.screen.blit(self.walk_d[0], self.rect)


