"""测试单行文本框--Entry"""
# coding=utf8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        """创建组件"""
        self.label01 = Label(self,text="用户名")
        self.label01.pack()
        # StringVar变量绑定到指定组件
        # StringVar变量的值发生变化，组件内容也变化
        # 组件内容发生变化，StringVar变量也发生变化
        v1 = StringVar()
        self.entry01 = Entry(self,textvariable=v1)
        self.entry01.pack()
        v1.set("admin")
        print(v1.get(), self.entry01.get())

        # 创建密码框
        self.label02 = Label(self,text="密码")
        self.label02.pack()

        # 创建密码输入框
        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2,show="*")
        self.entry02.pack()
        # 创建登录按钮
        self.btn01 = Button(self, text="登录", command=self.login)
        self.btn01.pack()

    def login(self):
        username = self.entry01.get()
        pwd = self.entry02.get()
        print("去数据库比对")
        print("用户名: "+username)
        print("密码:"+pwd)
        if username == "Jack" and pwd == "123456":
            messagebox.showinfo("测试", "登录成功")
        else:
            messagebox.showinfo("测试", "登录失败")






if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250+200+300")
    app = Application(master=root)
    root.mainloop()
