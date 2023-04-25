# coding=utf-8

'''
新增功能
 1.加载主窗口
 2.添加事件
   2.1.
 3.左上角文字的绘制
 4.加载我方坦克
 5.我方坦克切换方向
 6.我方坦克移动
 7.优化坦克移动
 8.优化坦克移动--按键方向移动



'''

import pygame,time

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)

class MainGame():
    window = None
    my_tank = None

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口大小
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        MainGame.my_tank = Tank(350, 250)
        # 设置窗口标题
        pygame.display.set_caption("坦克大战1.03")
        while True:
            # 使用坦克移动的速度慢
            time.sleep(0.02)
            # 设置窗口填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            # 绘制文字
            MainGame.window.blit(self.getTextSurface('敌方坦克剩余数量:%d' % 10), (10, 10))
            # 调用坦克显示方法
            MainGame.my_tank.displayTank()
            # 调用移动方法
            # 如果坦克的开关是开启的，才可以移动
            if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
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
                MainGame.my_tank.stop = False
                if event.key == pygame.K_LEFT:
                    # 切换方向
                    MainGame.my_tank.direction = 'L'
                    #MainGame.my_tank.stop = False
                    # MainGame.my_tank.move()
                    print("按下左键，坦克向左移动")
                elif event.key == pygame.K_RIGHT:
                    # 切换方向
                    MainGame.my_tank.direction = 'R'
                    # MainGame.my_tank.move()
                    print("按下左键，坦克向右移动")
                elif event.key == pygame.K_UP:
                    # 切换方向
                    MainGame.my_tank.direction = 'U'
                    # MainGame.my_tank.move()
                    print("按下上键，坦克向上移动")
                elif event.key == pygame.K_DOWN:
                    # 切换方向
                    MainGame.my_tank.direction = 'D'
                    # MainGame.my_tank.move()
                    print("按下上键，坦克向下移动")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")

            # 修改坦克的移动的开关状态
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    MainGame.my_tank.stop = True









class Tank():
    # 坦克距离左边和上边的
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U':pygame.image.load('img/p1tankU.gif'),
            'D': pygame.image.load('img/p1tankD.gif'),
            'L': pygame.image.load('img/p1tankL.gif'),
            'R': pygame.image.load('img/p1tankR.gif'),
        }
        # 方向
        self.direction = 'L'
        # 根据当前图片的方向获取图片 surface
        self.image = self.images[self.direction]
        # 获取区域
        self.rect = self.image.get_rect()
        # 设置区域的left 和 top
        self.rect.left = left
        self.rect.top = top
        # 速度，决定移动的快慢
        self.speed = 5
        # 坦克是否停止
        self.stop = True


    # 移动
    def move(self):
        # 判断坦克的方向进行移动
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
        elif self.direction == 'R':
            if self.rect.left+self.rect.height < SCREEN_WIDTH:
                self.rect.left += self.speed


    # 射击
    def shot(self):
        pass

    # 展示坦克的方法
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用blit方法展示
        MainGame.window.blit(self.image, self.rect)


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

