"""
类专有方法
可调用的方法__call__()
"""

class SalaryAccount:
    '''工资计算类'''
    def __call__(self, salary):
        print("算工资啦....")
        yearSalary = salary*12
        daySalary = salary//22.5
        hourSalary = daySalary//8
        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)


if __name__ == '__main__':
    s = SalaryAccount()
    result = s(3000)
    print(result)

