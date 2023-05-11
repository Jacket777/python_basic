# 主窗口

import pygame
from part04_game.ch01_alien_invasion.button import Button
from part04_game.ch01_alien_invasion.scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()




    # 创建一个外星人
    # alien = Alien(ai_settings, screen)
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            # bullets.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings,  screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)





if __name__ == '__main__':
    run_game()
