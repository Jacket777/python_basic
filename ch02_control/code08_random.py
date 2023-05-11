#  random使用
import random


def random_use():
    for i in range(10):
        print(random.randint(1, 10))


def random_basic():
    random_choice = random.choice(['apple', 'pear', 'banana'])
    print(random_choice)
    random_list = random.sample(range(100), 10)
    print(random_list)
    random_number = random.random()
    print(random_number)
    random_integer = random.randrange(6)
    print(random_integer)


def test_random():
    counter = 0
    for i in range(100):
        value = random.random()
        if value >= 0.5:
            counter += 1
    print(counter/100)


if __name__ == '__main__':
    # random_use()
    test_random()
