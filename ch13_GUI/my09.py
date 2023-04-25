"""测试画布--canvas"""
# coding=utf8
from tkinter import *
import random


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()

    def creatWidget(self):
        self.canvas = Canvas(self, width=400, height=300, bg="green")
        self.canvas.pack()
        # 画一条直线
        line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        # 画一个矩形
        rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # 画一个椭圆，坐标两双， 为椭圆的边界矩形左上角和底部右下角
        oval = self.canvas.create_oval(100, 60, 300, 150)
        global photo
        photo = PhotoImage(file="imgs/logo.gif")
        self.canvas.create_image(150, 170, image=photo)
        Button(self, text="画出10个矩形", command=self.draw50Recg).pack(side="left")

    def draw50Recg(self):
        for i in range(0,10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)
            x2 = x1 + random.randrange(int(self.canvas["width"])/2)
            y2 = y1 + random.randrange(int(self.canvas["height"])/2)
            self.canvas.create_rectangle(x1,y1,x2,y2)




if __name__ == "__main__":
    root = Tk()
    root.geometry("500x350+200+300")
    app = Application(master=root)
    root.mainloop()
