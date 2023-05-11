# code02 使用实例，与修改属性值

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage  # 通过方法更新属性值

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage


def car_use():
    my_car = Car('audi', 'a4', 2016)
    print(my_car.get_descriptive_name())
    my_car.read_odometer()
    my_car.update_odometer(1000)
    my_car.read_odometer()
    my_car.increment_odometer(200)
    my_car.read_odometer()


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " opening")

    def set_number_served(self, number):
        self.number_served = number
        print("the number in restaurant is " + str(self.number_served))

    def increment_number_served(self, number):
        self.number_served += number


def restaurant_use():
    restaurant01 = Restaurant('China', 'Chinese')
    restaurant01.set_number_served(100)
    restaurant01.increment_number_served(20)
    restaurant01.set_number_served(0)


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print('first name : ' + self.first_name + ' last_name: ' + self.last_name)

    def greet_user(self):
        print('hello: ' + " " + self.last_name + " " + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("try number: " + str(self.login_attempts))

    def reset_login_attempts(self):
        self.login_attempts = 0


def use_all():
    user01 = User('Jack', 'Li')
    user01.increment_login_attempts()
    user01.increment_login_attempts()
    user01.increment_login_attempts()
    user01.reset_login_attempts()
    user01.increment_login_attempts()


if __name__ == '__main__':
    use_all()
    # car_use()
    # restaurant_use()

