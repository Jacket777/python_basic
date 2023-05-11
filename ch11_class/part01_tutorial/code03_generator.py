# code03 生成器定义与使用

# 1. 生成器的定义
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# 2. 使用生成器
def use_generator():
    for char in reverse('golf'):
        print(char)


# 3.生成器表达式
def use_generator_expression():
    result = sum(i*i for i in range(10))
    print(result)
    x_vec = [10, 20, 30]
    y_vec = [7, 5, 3]
    result01 = sum(x*y for x, y in zip(x_vec, y_vec))
    print(result01)
    data = 'golf'
    list01 = list(data[i] for i in range(len(data)-1, -1, -1))
    print(list01)


if __name__ == '__main__':
    # use_generator()
    use_generator_expression()

