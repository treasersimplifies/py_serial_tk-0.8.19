__author__ ="* * treaer 2017 * *"
from serial import *
from tkinter import *
import time
import Pmw
'''
演示关于python中tk的用法：详见：http://www.cnblogs.com/kaituorensheng/p/3287652.html
包括控件：label、frame、entry（单行文本）、text（文本区域）、

'''
'''
#注意是/dev/XXX
i = 0
g[0] = 0
while(i):
    g[i] = ser.read()
    print(ser.port+':')
    print(g[i])
    i = i+1

print(g)
'''


class MySerial():

    def __init__(self, port_name):
        self.ser = Serial(port_name, 9600, timeout=0.5)
        self.data = ""
        self.count = 0

    def show_data(self, text):
        self.count += 1
        self.data = str(self.ser.readline())
        text.insert(END, str(self.count) + ". " + self.data+"\n")


class conver():
    #   传入广义的xy，转化为构造坐标所需要传入的xy
    def __init__(self, x, y):
        self.x = x + 20
        self.y = 440 - y - 20


class SerialApp(Frame):

    def __init__(self,root):
        root.title("上位机串口通信")
        root.geometry("1100x580")
        root.resizable(width=True, height=True)
        Pmw.initialise()
        self.port_name = ""
        self.open_enr = False
        self.start_enr = False
        self.stop_enr = False

        def main():
            frame_vice.pack_forget()
            frame_main.pack()   #

        def vice():
            frame_main.pack_forget()
            frame_vice.pack()   #

        def open_port():
            self.open_enr = True
            if self.open_enr:
                # 这一句直接去掉了空余的列表成员
                self.port_name = text_one.get(2.0, 3.0)[11:50].replace("\n", "")
                print(str(self.port_name))
                try:
                    self.myserial = MySerial(self.port_name)
                except SerialException:
                    text_two.insert(END, "Port open:Failed----Port " + self.port_name + " not found.\n")
                else:
                    text_two.insert(END, "Port open:           Successfully.\n")

        def start():
            self.start_enr = True
            if self.start_enr:
                try:
                    self.myserial = MySerial(self.port_name)
                except SerialException:
                    text_two.insert(END, "Calculation starts:Failed----Port " + self.port_name + " not available.\n")
                else:
                    text_two.insert(END, "Calculation starts:  Successfully.\n")
                    self.myserial.show_data(text_two)

        def stop():
            self.open_enr = False
            self.start_enr = False
            self.stop_enr = True
            MySerial(self.port_name).ser.close()
            text_two.insert(END, "Port close:           Successfully.\n")

        def test():
            text_two.insert(END, "That's for button test.\n")
            for i in range(4):
                text_one.delete(14.18)

        def resume():
            text_one.delete(1.0,END)
            text_one.insert(1.0, "1.Serial Port to Choose.\n")
            text_one.insert(2.0, "  tag     :Copy dev name here.\n")
            text_one.insert(3.0, "  anchor 1:Copy dev name here(no space in the beginning).\n")
            text_one.insert(4.0, "  anchor 2:Copy dev name here(no space in the beginning).\n")
            text_one.insert(5.0, "  anchor 3:Copy dev name here(no space in the beginning).\n")
            text_one.insert(6.0, "  anchor 4:Copy dev name here(no space in the beginning).\n")
            text_one.insert(2.11, "/dev/tty.usbmodem14541")
            # text_one.insert(2.11, "/dev/tty")表示向第2行第11列添加文本
            text_one.insert(7.0, "2.(X,Y) of tag(calculated) and anchors(m).\n")
            text_one.insert(8.0,  "  tag     :\n")
            text_one.insert(9.0,  "  anchor 1:\n")
            text_one.insert(10.0, "  anchor 2:\n")
            text_one.insert(11.0, "  anchor 3:\n")
            text_one.insert(12.0, "  anchor 4:\n")
            text_one.insert(8.11,"1.55,3.70,-4.7")
            text_one.insert(13.0, "3.Distance between tag and anchors(m).\n")
            text_one.insert(14.0, "  tag to anchor 1:\n")
            text_one.insert(15.0, "  tag to anchor 2:\n")
            text_one.insert(16.0, "  tag to anchor 3:\n")
            text_one.insert(17.0, "  tag to anchor 4:\n")
            text_one.insert(14.18, "3.36")
            text_one.insert(18.0, "4.Distance between anchors(m).\n")
            text_one.insert(19.0, "  1 to 2:\n")
            text_one.insert(20.0, "  1 to 3:\n")
            text_one.insert(21.0, "  1 to 4:\n")
            text_one.insert(22.0, "  2 to 3:\n")
            text_one.insert(23.0, "  2 to 4:\n")
            text_one.insert(24.0, "  3 to 4:\n")
            text_one.insert(24.9, "2.54")

            text_two.insert(END, "Resume the text area:Successfully.\n")

        frame_main = Frame(root)

        frame_top = Frame(root)   # usage :   用作容器，其中relief属性用于上升或者下沉
        label_one = Label(root, text="“The Loser Now Will Be Later to Win.”\n""Reality Is Just God's Imagination.\n"
                          "Real Artists Simplify."
                          , bg="yellow", font=("Arial", 18))
        # usage :   Label(根对象, [属性列表])

        button_main = Button(frame_top, text="MAIN", command=main, width=10, height=3, disabledforeground="red",
                             highlightcolor="red", highlightbackground="grey", activebackground="green",
                             activeforeground="green")
        button_main.pack(side=LEFT)
        button_vice = Button(frame_top, text="VICE", command=vice, width=10, height=3)
        button_vice.pack(side=LEFT)

        label_one.pack(side=TOP)   # 这里的side可以赋值为LEFT RTGHT TOP BOTTOM
        Label(frame_top, text="Two years passed.",
              relief=RAISED).pack(side=LEFT, padx=5)
        Label(frame_top, text="Still Needs To Drill.", relief=SUNKEN).pack(side=LEFT,padx=15)

        var = StringVar()
        entry_one = Entry(frame_top, textvariable=var, width=10)
        # usage :   先绑定StringVar类型的变量，再用set方法改变即可
        var.set("hello")
        entry_one.pack(side=LEFT)
        frame_top.pack()    # #

        frame_vice = Frame(root)
        label_vice = Label(frame_vice, text="What a pleasure to use the software!\n" +
                        "Version: 7.8.17\n" + "Author: Treaser Lou"
                          , font=("Symbol", 20, "bold"))
        label_vice.pack(side=LEFT)

        text_two = Text(frame_vice, height=29, width=69)
        login_time = time.ctime()
        text_two.insert(1.0, "This is the command window.\n")
        text_two.insert(2.0, "Last login: " + login_time + "\n")
        text_two.insert(3.0, "TreaserdeMacBook-Pro:~ treasersmac$ \n")
        text_two.insert(4.0, "HISTORY COMMANDS:\n")
        text_two.pack(side=LEFT)

        frame_left = Frame(frame_main)
        text_one = Text(frame_left, height=29, width=69, bg="grey")
        # usage :   文本区域，这里的height指的是行数，width指的是一行的字符数，而不是像素！
        # 关于text的帖子：http://lib.csdn.net/article/python/43389
        resume()   # 全部的代码都封装到这个函数里
        text_one.pack(side=TOP)
        frame_left.pack(side=LEFT)    # #

        frame_mid = Frame(frame_main)
        button_one = Button(frame_mid, text="press test", command=test, width=10, height=3).pack(side=TOP)
        button_resume = Button(frame_mid, text="resume", command=resume, width=10, height=3).pack(side=TOP)
        button_open = Button(frame_mid, text="open port", command=open_port, width=10, height=3).pack(side=TOP)
        button_start = Button(frame_mid, text="start", command=start, width=10, height=3).pack(side=TOP)
        button_stop = Button(frame_mid, text="stop", command=stop, width=10, height=3).pack(side=TOP)
        frame_mid.pack(side=LEFT)    # #

        canvas = Canvas(frame_main, height=440, width=440, bg="grey")
        # 有关canvas的帖子：http://blog.csdn.net/aa1049372051/article/details/51886507
        for i in range(20, 470, 40):
            canvas.create_line(i, 20, i, 420, dash=2)    # dash是虚线属性
            canvas.create_line(20, i, 420, i, dash=2)
        canvas.create_text(conver(-5, -10).x, conver(-5, -10).y, text="0")
        for i in range(40, 440, 40):
            canvas.create_text(conver(i, 0).x, conver(i, -10).y, text=str(i))
            canvas.create_text(conver(-5, i).x, conver(0, i).y, text=str(i))
        point_tag = canvas.create_oval(conver(40,80).x-5, conver(40,80).y-5, conver(40,80).x+5, conver(40,80).y+5, fill="black")
        canvas.pack(side=LEFT)

        print(self.open_enr)
        print(self.start_enr)
        frame_main.pack()  #

root = Tk()
app = SerialApp(root)
root.mainloop()


'''
canvas.create_rectangle(0, 0, 100, 100)
Last login: Thu Aug 17 11:21:38 on ttys000
TreaserdeMacBook-Pro:~ treasersmac$


'''
