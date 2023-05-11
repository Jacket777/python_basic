import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen
        # 加载图片
        # self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.image.load("images/A.bmp")
        self.rect = self.image.get_rect()
        # 每个外星人都在最左上方
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """如果外星人位于屏幕边缘， 就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """向左或向右移动外星人"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x



