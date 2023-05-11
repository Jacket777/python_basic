# code02 使用datetime
""""
方便的格式化显示日期
日期进行算术运算
"""

from datetime import date, datetime, timedelta
import time


def use_datetime():
    datetime_now = datetime.now()  # 返回datetime.datetime类对象
    print(type(datetime_now))
    print(datetime_now.year, datetime_now.month, datetime_now.day,
          datetime_now.hour, datetime_now.minute, datetime_now.second)
    # 设置时间
    dt = datetime(2015, 10, 21, 15, 29, 0)
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute,dt.second)


# 时间转换
def transfer_time():
    # 时间戳转换
    dt = datetime.fromtimestamp(1000000)
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    dt = datetime.fromtimestamp(time.time())
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)


# 时间比较
def compare_time():
    dt01 = datetime(2015, 10, 31, 0, 0, 0)
    dt02 = datetime(2016, 1, 1, 0, 0, 0)
    dt03 = datetime(2015, 10, 31, 0, 0, 0)
    if dt01 == dt03:
        print("same time")
    if dt01 < dt02:
        print("dt02 bigger")
    if dt02 != dt03:
        print("not same time")


# 一段时间表时
def use_duration():
    delta = timedelta(days=11, hours=10, minutes=9, seconds=8)
    print("delta.days", "delta.seconds", "delta.microseconds")
    print(delta.days, delta.seconds, delta.microseconds)
    print("total second", delta.total_seconds())
    print(str(delta))


# 时间运算
def time_calc():
    dt = datetime.now()
    thousandDays = timedelta(days=1000)
    dt = dt + thousandDays
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    # 时间运算
    dt01 = datetime(2015, 10, 21, 16, 29, 0)
    thirty_years = timedelta(days=365*30)
    # 30年后
    dt01 = dt01 - thirty_years
    print(dt01.year, dt01.month, dt01.day, dt01.hour)
    # 60年后
    dt01 = dt01 - (2*thirty_years)
    print(dt01.year, dt01.month, dt01.day, dt01.hour)


# 暂停直至特定日期
def pause():
    dt = datetime(2022, 1, 1, 0, 0, 0)
    while datetime.now() < dt:
        time.sleep(1)


# 格式化datetime
def format_datetime():
    dt01 = datetime(2015, 10, 21, 16, 29, 0)
    result01 = dt01.strftime('%Y/%m/%d %H:%M:%S')
    print(result01)
    result02 = dt01.strftime('%I:%M %p')
    print(result02)
    result03 = dt01.strftime("%B of %y")
    print(result03)
    print('-------------------------------------')
    dt = datetime.strptime('October 21, 2015', '%B %d, %Y')
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    dt = datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    dt = datetime.strptime("October of '15", "%B of '%y")
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    dt = datetime.strptime("October of '63", "%B of '%y")
    print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)


def use_date():
    now = date.today()
    print(type(now), now)
    # 格式化
    result = now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')
    print(result)
    birthday = date(1964, 7, 31)
    age = now - birthday
    print(age.days)


if __name__ == '__main__':
    # test_datetime()
    # use_datetime()
    # transfer_time()
    # compare_time()
    # use_duration()
    # time_calc()
    format_datetime()
