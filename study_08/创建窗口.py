# coding = utf-8
import random

import pygame
import time
from pygame.locals import *


class HeroPlan():
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 500
        self.img = pygame.image.load("./img/hero1.png")
        self.screen = screen_temp
        self.bullet_lists = []

    def disPlay(self):
        self.screen.blit(self.img, (self.x, self.y))

        for bullet in self.bullet_lists:
            # print(len(self.bullet_lists))
            bullet.disPlay()
            bullet.move()
            if bullet.judge():
                self.bullet_lists.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def hero_fire(self):
        self.bullet_lists.append(Bullet(self.screen, self.x, self.y))


"""敌机"""


class EnemyPlan():
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.img = pygame.image.load("./img/enemy0.png")
        self.screen = screen_temp
        self.bullet_lists = []
        self.direction = "r"

    def disPlay(self):
        self.screen.blit(self.img, (self.x, self.y))

        for bullet in self.bullet_lists:
            # print(len(self.bullet_lists))
            bullet.disPlay()
            bullet.move()
            if bullet.judge():
                self.bullet_lists.remove(bullet)

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5

    def move_down(self):
        self.y += 5

    def fire(self):
        if random.randint(1, 100) == 30 or random.randint(1, 100) == 8:
            self.bullet_lists.append(EnemyBullet(self.screen, self.x, self.y))

    def move(self):
        if self.direction == "r":
            self.x += 5
        elif self.direction == "l":
            self.x -= 5

        if self.x > 440:
            self.direction = "l"
        elif self.x < 0:
            self.direction = "r"


# 飞机发射的子弹
class Bullet():
    def __init__(self, screen_temp, x, y):
        self.x = x + 40
        self.y = y - 20
        self.img = pygame.image.load("./img/bullet.png")
        self.screen = screen_temp

    def disPlay(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        elif self.y > 0:
            return False


# 敌机发射的子弹
class EnemyBullet():
    def __init__(self, screen_temp, x, y):
        self.x = x + 25
        self.y = y + 40
        self.img = pygame.image.load("./img/bullet1.png")
        self.screen = screen_temp

    def disPlay(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 600:
            return True
        else:
            return False


def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.hero_fire()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero_temp.move_down()
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero_temp.move_up()


def main():
    screen = pygame.display.set_mode((480, 600), 0, 32)
    background = pygame.image.load("./img/background.png")
    pygame.key.set_repeat(10)

    hero = HeroPlan(screen)
    enemy = EnemyPlan(screen)

    while True:
        screen.blit(background, (0, 0))
        # screen.blit( hero, (x, y) )
        hero.disPlay()
        enemy.disPlay()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main();
