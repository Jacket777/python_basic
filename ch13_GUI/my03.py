"""测试Label组件的基本用法，使用面向对象的方式"""
# coding=utf-8
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """经典的GUI程序的类的写法"""

    def __init__(self, master=None):
        super().__init__(master)  # super()代表父类的定义，不是父类的对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建新的组件"""
        self.label01 = Label(self, text="程序员",width=10, height=2,
                            bg="black", fg="white")
        self.label01["text"] = "CCC"
        self.label01.config(bg="black", fg="white")
        self.label01.pack()
        self.label02 = Label(self, text="程序员", width=10, height=2,
                             bg="blue", fg="white", font=("黑体", 30))
        self.label02.pack()

        # 显示图像
        global photo  # 把photo声明成全局变量，如果是局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出图像

        photo = PhotoImage(file="imgs/logo.gif")
        self.label03 = Label(self,image=photo)
        self.label03.pack()

        self.label04 = Label(self, text="北京\n程序员\n东西",
                             borderwidth=5, relief="groove",justify="right")
        self.label04.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250+200+300")
    app = Application(master=root)
    root.mainloop()

