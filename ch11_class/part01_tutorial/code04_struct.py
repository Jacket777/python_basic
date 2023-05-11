# code04 实现C中结构体

class Employee:
    pass


def use_struct():
    john = Employee()
    john.name = 'John Doe'
    john.dept = 'Computer lab'
    john.salary = 1000
    print(john.salary)


if __name__ == '__main__':
    use_struct()
