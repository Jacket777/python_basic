from die import Die
import pygal

# 1. 投一个
def test_die():
    die = Die()
    # 结果存在列表中
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)  # 统计每个数出现的次数
        frequencies.append(frequency)
    # 对结果进行可视化
    hist = pygal.Bar()
    hist.title = "Result of rolling one D6 1000 times."
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add("D6", frequencies)
    hist.render_to_file('die_visual.svg')


def test_die2():
    die_1 = Die()
    die_2 = Die()

    # 存储结果列表
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)


    # 对结果进行可视化
    hist = pygal.Bar()
    hist.title = "Result of rolling one D6 1000 times."
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add("D6 + D6", frequencies)
    hist.render_to_file('die_visual.svg')


# 面值不同
def test_die3():
    die_1 = Die()
    die_2 = Die(10)

    # 存储结果列表
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    # 分析结果
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

    # 对结果进行可视化
    hist = pygal.Bar()
    hist.title = "Result of rolling one D6 1000 times."
    hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'
                     '13', '14', '15', '16']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add("D6 + D10", frequencies)
    hist.render_to_file('die_visual.svg')



if __name__ == '__main__':
    test_die3()


