import turtle

t = turtle.Pen()
my_colors=("red","green","yellow","black")
t.width(4)
t.speed(10)
for i in range(10):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(10*i+10)

turtle.done()#程序执行完后，界面存在