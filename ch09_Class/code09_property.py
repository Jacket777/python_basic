"""
测试@property的最简化的用法
"""


class Employee:
    @property
    def salary(self):
        print("salary return ....")
        return 10000


if __name__ == '__main__':
    emp1 = Employee()
    # emp1.salary()
    print(emp1.salary)
