# 继承练习
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + " opening")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['A', 'B', 'C']

    def display_flavors(self):
        print(self.flavors)


def use_ice_cream_stand():
    iceCreamRes = IceCreamStand('CHINA', 'chinese')
    iceCreamRes.display_flavors()



class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print('first name : ' + self.first_name + ' last_name: ' + self.last_name)

    def greet_user(self):
        print('hello: ' + " " + self.last_name + " " + self.first_name)


class Admin(User):
    def __init__(self, first_name, last_name):
        super(Admin, self).__init__(first_name, last_name)
        # self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()

    # def show_privilege(self):
    #     print(self.privileges)


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privilege(self):
        print(self.privileges)



def use_admin():
    admin_user = Admin('Tom', 'He')
    # admin_user.show_privilege()
    admin_user.privileges.show_privilege()


if __name__ == '__main__':
    # use_ice_cream_stand()
    use_admin()


