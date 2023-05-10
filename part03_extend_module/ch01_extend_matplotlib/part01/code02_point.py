# code02 绘制散点图

import matplotlib.pyplot as plt


def draw_point():
    x_values = [1, 2,  3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    plt.scatter(x_values, y_values, s=100)
    # 设置图表标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    plt.show()


def auto_point():
    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]
    # plt.scatter(x_values, y_values, s=40)
    # plt.scatter(x_values, y_values, edgecolors='none', s=40)
    # plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
    # plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
    # 设置图表标题并给坐标轴加上标签
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)
    # 设置刻度标记的大小
    plt.tick_params(axis='both', which='major', labelsize=14)
    # 设置每个坐标的取值范围
    plt.axis([0, 1100, 0,  1100000])
    # plt.show()  # 保存图片时，不能使用
    plt.savefig('squares_plot.png', bbox_inches='tight')  # 自动保存图表




if __name__ == '__main__':
    # draw_point()
    auto_point()
