'''
坦克大战游戏的需求
1.项目有哪些类
2.每个类有哪些方法

1.坦克类（我方坦克，敌方坦克）
  1.1.射击
  1.2.移动
  1.3.显示坦克类
2.子弹类
   2.1.移动
   2.2.显示子弹的方法
3.墙壁类
  3.1.属性：是否可以通过
4.爆炸效果类
  展示爆炸效果
5音效类
  播放音乐
6主类
  6.1.开始游戏
  6.2.结束游戏
'''


class MainGame():
    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        pass

    # 结束游戏
    def endGame(self):
        pass


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
