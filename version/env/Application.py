# Application.py
# Application负责项目的启动，关闭等基础服务

from version.env.Env import Env

from tkinter import *

class Application(object):
    def __init__(self):
        self.tk=Tk()
        self.tk.title('Frog test round: 0, time used: 0s')
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.canvas=Canvas(self.tk,width=520,height=550,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.tk.update()

    def main(self):
        env=Env(self.tk,self.canvas)
        try:
            env.run()
        except TclError as e:
            pass