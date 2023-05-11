# code02 飞船类
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        """初始化飞船并设置飞船的初始位置"""
        self.screen = screen
        self.settings = settings

        # 加载飞船图片并获取其外矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放到屏幕中央底部
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值， 而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += self.settings.ship_speed_factor
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.settings.ship_speed_factor

        # 根据self.centerx更新对象
        self.rect.centerx = self.center


    def blitme(self):
        """在指定位置放置飞船"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

