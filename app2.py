from tkinter import *
import Pmw

class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()
        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=RIGHT)



    def say_hi(self):
        print("hi there, everyone!,yes")

root = Tk()
app = App(root)
root.mainloop()