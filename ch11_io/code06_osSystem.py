import os
"""
启动各类命令
"""

# 启动记事本
def test01():
    os.system("notepad.exe")


# 在控制台中启动ping命令
def test02():
    os.system("ping www.baidu.com")


# 启动注册表
def test03():
    os.system("regedit")


# 启动控制台
def test04():
    os.system("cmd")


# 直接调用可执行的文件
def test05():
    os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")


if __name__ == '__main__':
    test01()
