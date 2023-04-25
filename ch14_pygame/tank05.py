# coding=utf-8

'''
新增功能
 1.加载主窗口
 2.添加事件
   2.1.
 3.左上角文字的绘制

'''

import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)

class MainGame():
    window = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口大小
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.03")
        while True:
            # 设置窗口填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量:%d' % 10), (10, 10))
            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print("谢谢使用，欢迎再次使用")
        exit()

    # 左上角文字的绘制
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有字体
        # print(pygame.font.get_fonts())
        # 获取字体Font对象
        font = pygame.font.SysFont("kaiti", 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface


    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        for event in eventList:
            # 判断按下的键是否是关闭还是键按下
            # 如果是退出，关闭窗口
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("按下左键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:
                    print("按下左键，坦克向右移动")
                elif event.key == pygame.K_UP:
                    print("按下上键，坦克向上移动")
                elif event.key == pygame.K_DOWN:
                    print("按下上键，坦克向下移动")



                # 判断按键的上下左右









class Tank():
    def __init__(self):
        pass

    # 移动
    def move(self):
        pass

    # 射击
    def shot(self):
        pass

    # 展示坦克的方法
    def displayTank(self):
        pass

# 我方坦克
class MyTank(Tank):
    def __init__(self):
        pass

# 敌方坦克
class EnemyTank(Tank):
    def __init__(self):
        pass

# 子弹类
class Bullet():
    def __init__(self):
        pass

    # 移动方法
    def move(self):
        pass

    # 展示子弹的方法
    def displayBullet(self):
        pass

# 墙壁类
class Wall():
    def __init__(self):
        pass
    # 展示墙壁的方法
    def displayWall(self):
        pass

class Explode():
    def __init__(self):
        pass

    # 展示爆炸效果的方法
    def displayExplode(self):
        pass


class Music():
    def __init__(self):
        pass

    # 播放音乐
    def playMusic(self):
        pass

if __name__=='__main__':
    mygame = MainGame()
    mygame.startGame()

