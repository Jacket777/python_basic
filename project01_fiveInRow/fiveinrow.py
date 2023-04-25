"""
五子棋
"""
from enum import IntEnum

import pygame

# 基础参数
square_size = 40  # 单元格的宽度
chess_size = square_size // 2 - 2  # 棋子大小
web_broad = 15  # 棋盘的格数 + 1
# 棋盘长度与宽度
map_w = web_broad * square_size
map_h = web_broad * square_size
# 按钮界面宽度
info_w = 60
# 按钮长宽
button_w = 120
button_h = 45
# 总窗口 长宽
screen_w = map_w
screen_h = map_h + info_w

"""
使用数字表示当前格情况
"""


class MAP_ENUM(IntEnum):
    be_empty = 0  # 无人下
    player1 = 1  # 玩家一， 执白
    player2 = 2  # 玩家二， 执黑
    out_of_range = 3  # 出界


class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.map = [[0 for x in range(self.width)] for y in range(self.height)]
        self.steps = []

    def get_init(self):
        for y in range(self.height):
            for x in range(self.width):
                self.map[y][x] = 0
        self.steps = []

    def intoNextTurn(self, turn):
        if turn == MAP_ENUM.player1:
            return MAP_ENUM.player2
        else:
            return MAP_ENUM.player1

    """
    根据输入的下标返回棋子的具体位置
    """

    def getLoacte(self, x, y):
        map_x = x * square_size
        map_y = y * square_size
        return map_x, map_y, square_size, square_size  # 返回位置信息


    def getIndex(self, map_x, map_y):
        x = map_x // square_size
        y = map_y // square_size
        return x, y


    def isInside(self, map_x, map_y):
        if map_x <= 0 or map_x >= map_w or map_y<=0 or map_y >= map_h:
            return False
        return True

    def isEmpty(self, x, y):
        return self.map[y][x] == 0

    def printChessPiece(self, screen):
        player_one = (255,245.238)
        player_two = (41,36,33)
        player_color = [player_one, player_two]
        for i in range(len(self.steps)):
            x, y = self.steps[i]
            map_x, map_y, width,height = self.getLoacte(x, y)
            pos, radius = (map_x + width//2, map_y+height//2), chess_size
            turn = self.map[y][x]
            pygame.draw.circle(screen,player_color[turn-1],pos,radius)
        pass

    def drawBoard(self, screen):
        color = (0,0,0)
        for y in range(self.height):
            start_pos = (square_size //2, square_size // 2 +square_size*y)
            end_pos = (map_w - square_size //2, square_size // 2 +square_size*y)
            pygame.draw.line(screen,color,start_pos,end_pos,1)
        for x in range(self.width):
            start_pos = (square_size //2 + +square_size*x, square_size // 2 )
            end_pos = (square_size //2 + square_size * x, map_h - square_size // 2 )
            pygame.draw.line(screen,color,start_pos,end_pos,1)




class MyChessAI():
    def __init__(self, chess_len):
        self.len = chess_len
        self.record = [[[0,0,0,0]] for i in range(chess_len) for j in range(chess_len)]
        self.count = [[0 for in range(SIU)]]
        pass

    def get_init(self):
        pass

    def isWin(self, board, turn):
        pass

    def genmove(self, board, turn):
        pass

    def search(self, board, turn):
        pass

    def findBestChess(self, board, turn):
        pass

    def getScore(self, mychess, yourchess):
        pass

    def evaluate(self, board, turn, checkWin=False):
        pass

    def evaluatePoint(self, board, x, y, me, you):
        pass

    def getLine(self, board, x, y, direction, me, you):
        pass

    def getBasicSituation(self, board, x, y, dir_index, dir, me, you, count):
        pass


class Button:
    def __init__(self, screen, text, x, y, color, enable):
        self.msg_image_rect = None
        self.msg_image = None
        self.screen = screen
        self.width = button_w
        self.height = button_h
        self.button_color = color
        self.text_color = (255, 255, 255)  # 纯白
        self.enable = enable
        self.font = pygame.font.SysFont(None, button_h * 2 // 3)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.topleft = (x, y)
        self.text = text
        self.init_msg()

    '''
    重写pygame 内函数，初始化按钮
    '''

    def init_msg(self):
        if self.enable:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
        else:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

        pass

    """
    根据按钮的enable状态填色，具体颜色在后续子类控制
    """

    def draw(self):
        if self.enable:
            self.screen.fill(self.button_color[0], self.rect)
        else:
            self.screen.fill(self.button_color[1], self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


class WhiteStartButton(Button):
    def __init__(self, screen, text, x, y):
        super.__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

    """
    点击
    """

    def click(self, game):
        if self.enable:
            game.start()
            game.winner = None
            game.multiple = False
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
            self.enable = False
            return True
        return False

    """
    取消点击
    """

    def unclick(self):
        if not self.enable:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
            self.enable = True


class BlackStartButton(Button):
    def __init__(self, screen, text, x, y):
        super.__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

    """
    点击
    """

    def click(self, game):
        if self.enable:
            game.start()
            game.winner = None
            game.multiple = False
            game.useAI = True
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
            self.enable = False
            return True
        return False

    """
    取消点击
    """

    def unclick(self):
        if not self.enable:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
            self.enable = True


class GiveupButton(Button):
    def __init__(self, screen, text, x, y):
        super.__init__(screen, text, x, y, [(230, 67, 64), (236, 139, 137)], False)

    """
    点击
    """

    def click(self, game):
        if self.enable:
            game.is_play = False
            if game.winner is None:
                game.winner = game.map.intoNextTurn(game.player)
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
            self.enable = False
            return True
        return False

    """
    取消点击
    """

    def unclick(self):
        if not self.enable:
            self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
            self.enable = True


class Game:
    def __init__(self, caption):
        pygame.init()
        self.screen = pygame.display.set_mode([screen_w, screen_h])
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock
        self.buttons = []
        self.buttons.append(WhiteStartButton(self.screen, 'Pick White', 20, map_h))
        self.buttons.append(WhiteStartButton(self.screen, 'Pick White', 20, map_h))
        self.buttons.append(WhiteStartButton(self.screen, 'Pick White', 20, map_h))
        self.buttons.append(WhiteStartButton(self.screen, 'Pick White', 20, map_h))
        self.is_play = False
        self.map = Map(web_broad, web_broad)
        self.player = MAP_ENUM.player1
        self.action = None
        self.AI = MyChessAI(web_broad)
        self.useAI = False
        self.winner = None
        self.multiple = False

    def start(self):
        self.is_play = True
        self.player = MAP_ENUM.player1  # 白棋先手
        self.map.get_init()

    '''
    绘制棋盘和按钮
    '''

    def play(self):
        # 画底板
        self.Clock.tick(60)
        wood_color = (210, 180, 140)
        pygame.draw(self.screen, wood_color, pygame.Rect(0, 0, map_w, screen_h))
        pygame.draw(self.screen, (255, 255, 255), pygame.Rect(map_w, 0, info_w, screen_h))
        # 画按钮
        for button in self.buttons:
            button.draw()
        if self.is_play and not self.isOver():
            if self.useAI and not self.multiple:
                x, y = self.AI.findBestChess(self.map.map, self.player)
                self.checkClick(x, y, True)
                self.useAI = False
            if self.action is not None:
                self.checkClick(self.action[0], self.action[1])
                self.action = None
            if not self.isOver():
                self.changeMouseShow()
        if self.isOver():
            self.showWinner()
        self.map.drawBoard(self.screen)
        self.map.printChessPiece(self.screen)

    def changeMouseShow(self):
        map_x, map_y = pygame.mouse.get_pos()
        x, y = self.map.getIndex(map_x, map_y)
        if self.map.isInside(map_x, map_y) and self.map.isEmpty(x, y):
            pygame.mouse.set_visible(False)
            smoke_blue = (176, 224, 230)
            pos, radius = (map_x, map_y), chess_size
            pygame.draw.circle(self.screen, smoke_blue, pos, radius)
        else:
            pygame.mouse.set_visible(True)

    def checkClick(self, x, y, isAI=False):
        self.map.click(x, y, self.player)
        if self.AI.isWin(self.map.ma, self.player):
            self.winner = self.player
            self.click_button(self.buttons[2])
        else:
            self.player = self.map.intoNextTurn(self.player)
            if not isAI:
                self.useAI = True

    def mouseClick(self, map_x, map_y):
        if self.is_play and self.map.isInside(map_x, map_y) and not self.isOver():
            x, y = self.map.getIndex(map_x, map_y)
            if self.map.isEmpty(x, y):
                self.action = (x, y)

    def isOver(self):
        return self.winner is not None

    def showWinner(self):
        def showFont(screen, text, location_x, location_y, height):
            font = pygame.font.SysFont(None, height)
            font_image = font.render(text, True, (255, 215, 0), (255, 255, 255))
            # 金黄色
            font_image_rect = font_image.get_rect()
            font_image_rect.x = location_x
            font_image_rect.y = location_y
            screen.blit(font_image, font_image_rect)

        if self.winner == MAP_ENUM.player1:
            str = 'White Wins!'
        else:
            str = 'Black Win!'
        showFont(self.screen, str, map_w / 5, screen_h / 8, 100)
        pygame.mouse.set_visible(True)

    def click_button(self, param):
        pass
