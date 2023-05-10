import matplotlib.pyplot as plt
import numpy as np


# 绘制散点图
def drawpoint():
    x = np.linspace(0, 10, 100)
    plt.scatter(x, np.sin(x))
    plt.show()


# 使用bar绘制柱状图，并设置柱的宽度
def drawclone():
    x = [1980, 1985, 1990, 1995]
    x_labels = ['1980年', '1985年', '1990年', '1995年']
    y = [1000, 3000, 4000, 5000]
    plt.bar(x, y, width=3)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xticks(x, x_labels)
    plt.xlabel('年份')
    plt.ylabel('销量')
    plt.title('根据年份销量对比图')
    plt.show()


# 使用bar和barh绘制柱状图
def drawclone2():
    np.random.seed(0)
    x = np.arange(5)
    y = np.random.randint(-5, 5, 5)
    print(x, y)
    # 将画布分隔成一行两列
    plt.subplot(1, 2, 1)
    # 在第一列中画图
    v_bar = plt.bar(x, y)
    # 在第一列的画布中 0位置画一条蓝线
    plt.axhline(0, color='blue', linewidth=2)
    plt.subplot(1, 2, 2)
    # barh将y和x轴对换 竖着方向为x轴
    h_bar = plt.barh(x, y, color='red')
    # 在第二列的画布中0位置处画蓝色的线
    plt.axvline(0, color='red', linewidth=2)
    plt.show()

# 对部分柱状图，使用颜色区分
def drawclone3():
    np.random.seed(0)
    x = np.arange(5)
    y = np.random.randint(-5, 5, 5)
    v_bar = plt.bar(x, y, color='lightblue')
    for bar, height in zip(v_bar, y):
        if height < 0:
            bar.set(edgecolor='darkred', color='lightgreen', linewidth='3')
    plt.show()



#  柱状图使用实例
def drawclone4():
    # 三天中三部电影的票房变化
    real_names = ['千与千寻', '玩具总动员4', '黑衣人']
    real_num01 = [5453, 7548, 6543]
    real_num02 = [1840, 4013, 3412]
    real_num03 = [1080, 1673, 2342]
    # 生成x  第1天   第2天   第3天
    x = np.arange(len(real_names))
    x_label = ['第{}天'.format(i+1) for i in range(len(real_names))]
    # 绘制柱状图
    # 设置柱的宽度
    width = 0.3
    plt.bar(x, real_num01, color='g', width=width, label=real_names[0])
    plt.bar([i + width for i in x], real_num02, color='b', width=width, label=real_names[1])
    plt.bar([i + 2*width for i in x], real_num03, color='r', width=width, label=real_names[2])
    plt.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签
    # 修改x坐标
    plt.xticks([i+width for i in x], x_label)
    # 添加图例
    plt.legend()
    # 添加标题
    plt.title('3天的票房数')
    plt.show()











if __name__ == '__main__':
    #drawpoint()
    #drawclone()
    #drawclone2()
    drawclone3()
