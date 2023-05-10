# coed07 随机练习 改进随机漫步，
from random import choice
import matplotlib.pyplot as plt


class RandomWalk:
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        # 所有随机都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含所有点"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # 不能不走
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x 和 y的值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice(list(range(1, 8)))
        step = direction * distance
        return step


def draw_random_trace():
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()


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
    draw_random_color_trace()

