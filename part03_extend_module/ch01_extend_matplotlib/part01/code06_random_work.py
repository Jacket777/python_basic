# coed05 随机练习 改进随机漫步，
from random import choice

import matplotlib.pyplot as plt


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机慢都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """计算随机漫步包含所有点"""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            x_step = x_direction * x_distance

            y_direction = choice([-1, 1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            y_step = y_direction * y_distance

            # 不能不走
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x 和 y的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


def draw_random_trace():
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()


def draw_more_random():
    while True:
        draw_random_trace()
        keep_running = input("Make another walk?(y/n): ")
        if keep_running == 'n':
            break


# 给点着色
def draw_random_color_trace():
    rw = RandomWalk(5000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=5)
    # 突出起点和终点
    plt.plot(0, 0, c='green', linewidth=5)
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red',  linewidth=5)

    # 隐藏坐标轴
    plt.axis('off')
    plt.show()




if __name__ == '__main__':
    # draw_random_trace()
    # draw_more_random()
    draw_random_color_trace()

