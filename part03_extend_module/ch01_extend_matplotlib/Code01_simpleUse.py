import matplotlib.pyplot as plt
import numpy as np


# 绘制直线
def drawine():
    plt.plot([0, 2], [1, 4])
    plt.show()

#  绘制折线图
def drwanoline():
    x = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(x, squares)
    plt.show()


# 绘制折线图并设置样式
def drawnolineWithtitle():
    datas = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(datas, squares, linewidth=5)  # 设置线条宽度
    # 设置图标标题， 并在坐标轴上添加标签
    plt.title('Numbers', fontsize=24)
    plt.xlabel('datas', fontsize=14)
    plt.ylabel('squares', fontsize=14)
    plt.show()


# 绘制图片包含中文
def drawwithchina():
    datas = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(datas, squares, linewidth=5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('标题设置', fontsize=24)
    plt.xlabel('x轴', fontsize=14)
    plt.ylabel('y轴', fontsize=14)
    plt.show()


# 绘制一元二次方程的曲线
def drawtopng():
    x = range(-100,100)
    y = [i**2 for i in x]
    plt.plot(x, y)
    plt.savefig('result.jpg')
    plt.show()


# 绘制正弦曲线和余弦曲线
def drawsin():
    # 生成x的坐标（0-10的100个等差数列）
    x = np.linspace(0, 10, 100)
    sin_y = np.sin(x)
    # 绘制正弦曲线
    plt.plot(x, sin_y)
    cos_y = np.cos(x)
    plt.plot(x, cos_y)
    plt.show()


# 将画布分为区域，将图画到画布的指定区域
def drawdiffcanvas():
    x = np.linspace(1, 10, 100)
    # 将画布分为2行2列，将图画到画布的1区域
    plt.subplot(2, 2, 1)
    plt.plot(x, np.sin(x))
    plt.subplot(2, 2, 3)
    plt.plot(x, np.cos(x))
    plt.show()






if __name__ == '__main__':
    #drawine()
    #drwanoline()
    #drawnolineWithtitle()
    #drawwithchina()
    #drawtopng()
    #drawsin()
    drawdiffcanvas()