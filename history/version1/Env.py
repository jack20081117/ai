#Env.py
#Env是青蛙生存的模拟环境.使用tkinter作画
#-----------------------------------------------------------------------------------------------------------------------
from history.version1.utils.EggTool import EggTool
from history.version1.egg.Egg import Egg
from history.version1.Frog import Frog

from configs import *

import logging
from tkinter import *

class Env(object):

    foods:list[list[bool]]=[]#foods

    frogs:list[Frog]=[]#Frog
    eggs:list[Egg]=[]#Egg

    def __init__(self,tk:Tk,canvas:Canvas):
        self.tk=tk#Tk()
        self.canvas=canvas#Canvas()

        logging.info('Abrabrabra!')
        if DELETE_EGGS:
            EggTool.deleteEggs()

        for i in range(ENV_XSIZE):
            self.foods.append([])
            for j in range(ENV_YSIZE):
                self.foods[i].append(False)

    def rebuildFrogAndFood(self):
        #先把背景画成白色
        self.canvas.create_rectangle(0,0,self.canvas.winfo_width(),self.canvas.winfo_height(),fill='white')
        self.frogs.clear()#清空Frogs
        for i in range(ENV_XSIZE):
            for j in range(ENV_YSIZE):
                self.foods[i][j]=False#清空食物
        for i in range(len(self.eggs)):
            for j in range(FROG_PER_EGG):
                self.frogs.append(Frog(ENV_XSIZE/2+nextInt(90),ENV_YSIZE/2+nextInt(90),self.eggs[i],self.tk,self.canvas))
        logging.info("Created %d frogs"%(FROG_PER_EGG*len(self.eggs)))
        for i in range(FOOD_QTY):
            self.foods[nextInt(ENV_XSIZE-3)][nextInt(ENV_YSIZE-3)]=True

    def drawFood(self):#画食物
        for x in range(ENV_XSIZE):
            for y in range(ENV_YSIZE):
                if self.foods[x][y]:
                    self.canvas.create_oval(x,y,x+2,y+2,outline='black',fill='black')

    def run(self):#运行
        EggTool.loadEggs(self)#导入或新建一批Egg
        _round=1#运行次数
        while True:
            self.rebuildFrogAndFood()
            allDead=False#青蛙是否全部死亡
            for i in range(STEPS_PER_ROUND):
                if allDead:#全部死亡就可以提前结束
                    break
                allDead=True
                for frog in self.frogs:
                    if frog.active(self):
                        allDead=False
                    if frog.alive and frog.moveCount==0 and i>STEPS_PER_ROUND/10:#不移动的”懒惰青蛙“死亡
                        frog.alive=False
                if i%SHOW_SPEED:#画青蛙会拖慢速度
                    continue
                self.canvas.create_rectangle(0,0,self.canvas.winfo_width(),self.canvas.winfo_height(),fill='white')
                self.drawFood()#画食物
                for frog in self.frogs:#画青蛙
                    frog.show(self.canvas)#青蛙移动
                self.tk.update_idletasks()
                self.tk.update()
            EggTool.layEggs(self)#保存蛋
            self.tk.title('Frog test round %d'%_round)
            _round+=1