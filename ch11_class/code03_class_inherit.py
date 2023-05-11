# code03 继承


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
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage  # 通过方法更新属性值
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        print("the care has gas tank")


# 电池抽象为类
class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")

    def get_range(self):
        if self.battery_size == 70:
            range_distance = 240
        elif self.battery_size == 85:
            range_distance = 270
        message = "This car can go approximately "+str(range_distance)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()

    # def describe_battery(self):
    #     print("This car has a "+str(self.battery_size)+"-kwh battery.")


    """重写父类方法"""
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")


if __name__ == '__main__':
    my_car = ElectricCar('tesla', 'model s', 2016)
    print(my_car.get_descriptive_name())
    # my_car.describe_battery()
    my_car.battery.describe_battery()
    my_car.fill_gas_tank()
    my_car.battery.get_range()
    my_car.battery.upgrade_battery()
    my_car.battery.get_range()

