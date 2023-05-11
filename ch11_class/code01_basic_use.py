# code01 basic use

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        print(self.name.title()+" rolled over!")


def use_dog():
    my_dog = Dog('willie', 6)
    print("My dog's name is " + my_dog.name.title()+".")
    print("My dog is " + str(my_dog.age) + " years old.")
    my_dog.sit()
    my_dog.roll_over()
    your_dog = Dog('lucy', 3)
    print("Your dog's name is " + your_dog.name.title() + ".")
    print("Your dog is " + str(your_dog.age) + " years old.")


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " opening")


def use_restaurant():
    restaurant_01 = Restaurant('China', 'chinese')
    restaurant_01.describe_restaurant()
    restaurant_02 = Restaurant('Japan', 'japanese')
    restaurant_02.describe_restaurant()
    restaurant_03 = Restaurant('UK', 'pig')
    restaurant_03.describe_restaurant()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('first name : ' + self.first_name + ' last_name: ' + self.last_name)

    def greet_user(self):
        print('hello: ' + " " + self.last_name + " " + self.first_name)


def user_all():
    user01 = User('Jack', 'Li')
    user02 = User('Jason', 'Zhang')
    user03 = User('Marry', 'Ma')
    user01.describe_user()
    user01.greet_user()
    user02.describe_user()
    user02.greet_user()
    user03.describe_user()
    user03.greet_user()


if __name__ == '__main__':
    # use_dog()
    use_restaurant()
    user_all()
