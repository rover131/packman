import pygame
import sys
from hero import Hero
from enemy import Enemy
from random import randint
import time


class Pack:
    def __init__(self):  # инициализация
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Pacman")
        self.bg_color = (207, 227, 239)
        self.hero = Hero(self.screen)
        self.enemies = pygame.sprite.Group()
        self._create_fleet()  # создание врагов

    def _create_fleet(self):  # создание врагов
        for i in range(4):
            enemy = Enemy(self)
            enemy.rect.x = randint(50, 950)
            enemy.rect.y = randint(50, 550)
            self.enemies.add(enemy)

    def run_game(self):  # запуск
        time1 = time.perf_counter()
        direc = randint(0, 3)
        while True:
            self._check_events()  # события клавиатуры
            self.update_screen()  # обновление экрана
            self.hero.update()  # движение пакмена
            self.enemies.update(direc)  # движение приведений
            direc, time1 = self.col_enem(direc, time1)  # возрождение и смена направлений приведений
            time.sleep(0.05)

    def col_enem(self, direc, time1):
        if time.perf_counter() - time1 > 5:
            direc1 = randint(0, 3)
            while direc1 == direc:
                direc1 = randint(0, 3)
            direc = direc1
            time1 = time.perf_counter()
        collisions = pygame.sprite.spritecollide(self.hero, self.enemies, True)
        if len(self.enemies) == 0:
            self._create_fleet()
        return direc, time1

    def _check_events(self):  # события клавиатуры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_down_events(self, event):
        """Реакция на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:  # перемещаем направо вкл
            self.hero.mov_right = True
            self.hero.mov = 0
        elif event.key == pygame.K_LEFT:  # перемещаем налево вкл
            self.hero.mov_left = True
            self.hero.mov = 1
        elif event.key == pygame.K_UP:  # перемещаем вверх вкл
            self.hero.mov_up = True
            self.hero.mov = 2
        elif event.key == pygame.K_DOWN:  # перемещаем вниз вкл
            self.hero.mov_down = True
            self.hero.mov = 3
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_up_events(self, event):
        """Реакция на отпускаие клавиш"""
        if event.key == pygame.K_RIGHT:  # перемещаем направо выкл
            self.hero.mov_right = False
        elif event.key == pygame.K_LEFT:  # перемещаем налево выкл
            self.hero.mov_left = False
        elif event.key == pygame.K_UP:  # перемещаем вверх выкл
            self.hero.mov_up = False
        elif event.key == pygame.K_DOWN:  # перемещаем вниз выкл
            self.hero.mov_down = False

    def update_screen(self):  # обновление экрана
        self.screen.fill(self.bg_color)
        self.hero.blitme()
        self.enemies.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    pa = Pack()
    pa.run_game()
