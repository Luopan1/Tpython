#coing=utf-8
# 飞机发射的子弹
import pygame
class Bullet():
    def __init__(self,screen_temp):
        self.x = 200
        self.y = 500
        self.img = pygame.image.load( "./img/hero1.png" )
        self.screen = screen_temp