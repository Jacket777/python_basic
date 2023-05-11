# code01 use time module
import sys
import time


def use_time():
    """简单应用"""
    value = time.time()  # UNIX纪元时间戳，浮点值，单位为秒数
    print(value)
    value = round(value, 4)  # 保留四位小数
    print(value)


def calc_prod():
    """"测试方法"""
    product = 1
    for i in range(1, 10000):
        product = product * 1
    return product


def calc_time():
    """计算调用时间"""
    startTime = time.time()
    prod = calc_prod()
    endTime = time.time()
    print('The result is %s digits long' % len(str(prod)))
    print('Took %s seconds to calculate ' % (endTime - startTime))


def use_sleep():
    """休眠时间"""
    for i in range(10):
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)


# 秒表
def stopwatch():
    print('Press ENTER to begin, Afterwards, press ENTER to "click" the stopwatch.Press Ctr-C to quit')
    input()  # press ENTER to begin
    print('Started.')
    startTime = time.time()  # get the first lap's start time
    lastTime = startTime
    lapNum = 1
    # Start tracking the lap times
    try:
        while True:
            command = input()
            if not command:
                lapTime = round(time.time() - lastTime, 2)
                totalTime = round(time.time() - startTime, 2)
                print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
                lapNum += 1
                lastTime = time.time()  # reset the last lap time
            else:
                sys.exit()
    except KeyboardInterrupt:
        print('\nDone.')


if __name__ == '__main__':
    # use_time()
    stopwatch()
