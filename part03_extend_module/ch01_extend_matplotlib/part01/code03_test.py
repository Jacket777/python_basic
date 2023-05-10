# code03 小练习

import matplotlib.pyplot as plt
import math

def simple_use():
    x_value = [1, 2, 3, 4, 5]
    y_value = [math.pow(x, 3) for x in x_value]
    plt.scatter(x_value, y_value, s=40)
    # 设置图表标题并给坐标轴加标签
    # 设置图表标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def complex_use():
    x_value = [x for x in range(5001)]
    y_value = [math.pow(x, 3) for x in x_value]
    plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
    # 设置图表标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标的取值范围
    plt.axis([0, 5000, 0, 125000000000])
    plt.show()





if __name__ == '__main__':
    # simple_use()
    complex_use()