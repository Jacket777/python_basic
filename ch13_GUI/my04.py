# coding=utf-8
"""测试按钮的使用"""
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
        self.btn01 = Button(root, text="登录",
                            width=6, height=3,anchor=NE,command=self.login)
        self.btn01.pack()
        global photo
        photo = PhotoImage(file="imgs/start.gif")
        self.btn02 = Button(root, image=photo, command=self.login)
        self.btn02.pack()
        # self.btn02.config(state="disabled")  # 设置按钮不可点击


    def login(self):
        messagebox.showinfo("测试", "welcome to BJ")


if __name__ == "__main__":
    root = Tk()
    root.geometry("400x250+200+300")
    app = Application(master=root)
    root.mainloop()
