#Application.py
#Application负责项目的启动,关闭等基础服务
#-----------------------------------------------------------------------------------------------------------------------
from history.version1.Env import Env

from tkinter import *
import logging;logging.basicConfig(level=logging.INFO)

class Application(object):
    def __init__(self):
        self.tk:Tk=Tk()
        self.tk.title('Frog test round 0')
        self.tk.geometry("500x500")
        self.canvas:Canvas=Canvas(self.tk,width=300,height=300,bd=0,highlightthickness=0)
        self.canvas.pack()
        self.canvas.place(x=100,y=100)
        self.tk.update()

    def main(self):
        env:Env=Env(self.tk,self.canvas)
        try:
            env.run()
        except TclError:
            pass