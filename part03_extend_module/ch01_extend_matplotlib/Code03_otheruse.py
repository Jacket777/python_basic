import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 绘制饼状图
def draw01():
    man = 71351
    woman = 68187
    man_perc = man / (woman + man)
    woman_perc = woman / (woman + man)
    # 添加名称
    labels = ['男', '女']
    # 添加颜色
    colors = ['blue', 'red']
    # 绘制饼状图  pie
    plt.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
    # labels 名称 colors：颜色，explode=分裂  autopct显示百分比
    paches, texts, autotexts = plt.pie([man_perc, woman_perc], labels=labels, colors=colors,
                                       explode=(0, 0.05), autopct='%0.1f%%')
    # 设置饼状图中的字体颜色
    for text in autotexts:
        text.set_color('white')

    # 设置字体大小
    for text in texts+autotexts:
        text.set_fontsize(20)
    plt.show()


# 使用randn函数生成1000个正太分布的随机数，使用hist函数绘制这1000个随机数的分布状态
def draw02():
    # 频次直方图，均匀分布
    # 正太分布
    x = np.random.randn(1000)
    # 画正太分布图
    #plt.hist(x)
    plt.hist(x, bins=100)  # 装箱的操作，将10个柱装到一起及修改柱的宽度
    plt.show()



# 使用normal函数生成1000个正太分布的随机数，使用hist函数绘制这100个随机数的分布状态
def draw03():
    # 几个直方图画到一个画布中,第一个参数期望  第二个均值
    x1 = np.random.normal(0, 0.8, 1000)
    x2 = np.random.normal(-2, 1, 1000)
    x3 = np.random.normal(3, 2, 1000)
    # 参数分别是bins：装箱，alpha：透明度
    kwargs = dict(bins=100, alpha=0.4)
    plt.hist(x1, **kwargs)
    plt.hist(x2, **kwargs)
    plt.hist(x3, **kwargs)
    plt.show()


# 使用pyplot绘制等高线图
def draw04():
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    # 计算x和y的相交点a
    X, Y = np.meshgrid(x, y)
    # 计算Z的坐标
    Z = np.sqrt(X**2 + Y**2)
    plt.contourf(X, Y, Z)
    plt.contour(X, Y, Z)
    # 颜色越深表示值越小，中间的黑色表示z=0.
    plt.show()


# 使用pyplot包和Matplotlib绘制三维图
def draw05():
    X = [1, 1, 2, 2]
    Y = [3, 4, 4, 3]
    Z = [1, 100, 1, 1]
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_trisurf(X, Y, Z)
    plt.show()





if __name__ == '__main__':
    draw05()
    #draw04()