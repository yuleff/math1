import math
from tkinter import *

win = Tk()
frame = Frame(win)
frame.pack(padx=10,pady=10)
win.title("一元二次方程求解")
win.geometry("400x400+200+50")
label = Label(win,
                 font=("黑体", 20),
                 width=20,
                 height=10,
                 wraplength=100,
                 justify="left",
                 anchor="ne")



v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
def test(content):
    if content.isdigit():
        return True
    else:
        return  False
testCMD=win.register(test)

Entry(frame, textvariable=v1, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=0)
Label(frame, text="x^2 +").grid(row=0, column=1)
Entry(frame, textvariable=v2, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=2)
Label(frame, text="x +").grid(row=0, column=3)
Entry(frame, textvariable=v3, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=4)
Label(frame, text="=0").grid(row=0, column=5)
Entry(frame, textvariable=v4, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=3, column=2)
Entry(frame, textvariable=v5, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=3, column=3)
Entry(frame, textvariable=v6, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=4, column=2)
Entry(frame, textvariable=v7, width=10, validate="key", validatecommand=(testCMD, '%P')).grid(row=4, column=3)

#TODO 声明函数

def quadratic( ):
    a = float(v1.get())    #a是什么
    b = float(v2.get())
    c = float(v3.get())
    h1 = v4
    h2 = v5
    h3 = v6
    h4 = v7


    if a == 0 and b!=0:
        x1= -c/b
        print("x1=",x1)
        h1.set("x1=")
        h2.set(x1)




    if a !=0:
        key = b**2-4*a*c
        if key > 0:
            x1= (-b+math.sqrt(key))/2*a
            x2 = (-b-math.sqrt(key))/2*a
            print("x1=",x1,"x2=",x2)
            h1.set("x1=")
            h2.set(x1)
            h3.set("x2=")
            h4.set(x2)


        if key == 0:
            x1 = -b/2*a
            x2 = x1
            print("x1=x2=",x1)
            h1.set("x1=x2=")
            h2.set(x1)


        if key < 0:
            print('无实数解.b^2-4*a*c=',key)
            h1.set("无实数解")
            h3.set("b^2-4*a*c=")
            h4.set(key)




h=Button(frame, text="计算结果", command=quadratic).grid(row=2, column=2, pady=7)





win.mainloop()