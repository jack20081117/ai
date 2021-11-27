# Egg.py
# Egg 蛋存在的目的是为了以最小的字节数串行化存储Frog,它是Frog的生成算法描述，而不是Frog本身，这样一来Frog就不能"永生"了，因为每一个egg都不等同于
# 它的母体，而且每一次测试，大部分条件反射的建立都必须从头开始训练，类似于人类，无论人类社会有多聪明，婴儿始终是一张白纸，需要花大量的时间从头学习。
# -----------------------------------------------------------------------------------------------------------------------
from version.egg.CellGroup import CellGroup
from version.egg.OrganDesc import OrganDesc
from version.egg.Zone import Zone
from version.brain.Organ import Organ
from version.Frog import Frog
from configs import *

class Egg(object):
    cellGroups=[]
    organDescs=[]

    randomCellGroupQty=30 #随机生成多少个组
    randomCellQtyPerGroup=3 #每个组有多少个脑细胞
    randomInputQtyPerCell=3 #每个脑细胞有多少个输入触突(神经末梢)
    randomOutputQtyPerCell=2 #每个脑细胞有多少个输出触突(树突)

    def __init__(self,*args):
        if len(args)==0:
            pass
        if len(args)==1:
            frog=args[0]
            if not isinstance(frog,Frog):
                raise TypeError
            self.cellGroups=[]
            for i in range(len(frog.cellGroups)):
                if frog.cellGroups[i].fat<=0:
                    if not frog.cellGroups[i].inherit:
                        continue
                    if percent(5):
                        continue
                oldCellGroup=frog.cellGroups[i]
                newCellGroup=CellGroup()
                newCellGroup.groupInputZone=Zone(self.variation(oldCellGroup.groupInputZone.x),
                                                 self.variation(oldCellGroup.groupInputZone.y),
                                                 self.variation(oldCellGroup.groupInputZone.radius))
                newCellGroup.groupOutputZone=Zone(self.variation(oldCellGroup.groupOutputZone.x),
                                                  self.variation(oldCellGroup.groupOutputZone.y),
                                                  self.variation(oldCellGroup.groupOutputZone.radius))
                newCellGroup.cellQty=round(self.variation(oldCellGroup.cellQty))
                newCellGroup.cellInputRadius=self.variation(oldCellGroup.cellInputRadius)
                newCellGroup.cellOutputRadius=self.variation(oldCellGroup.cellOutputRadius)
                newCellGroup.inputQtyPerCell=round(self.variation(oldCellGroup.inputQtyPerCell))
                newCellGroup.outputQtyPerCell=round(self.variation(oldCellGroup.outputQtyPerCell))
                newCellGroup.inherit=True
                self.cellGroups.append(newCellGroup)
            self.addOrganDescs()
        if len(args)==2:
            xEgg,yEgg=args
            if not isinstance(xEgg,Egg) or not isinstance(yEgg,Egg):
                raise TypeError
            self.cellGroups=[]
            for i in range(len(xEgg.cellGroups)):
                oldCellGroup=xEgg.cellGroups[i]
                newCellGroup=CellGroup(oldCellGroup)
                newCellGroup.inherit=True
                self.cellGroups.append(newCellGroup)
            yGroup=yEgg.cellGroups[nextInt(len(yEgg.cellGroups))-1]
            self.cellGroups.append(yGroup)
            for i in range(self.randomCellGroupQty):
                self.cellGroups.append(CellGroup(FROG_BRAIN_LENGTH,xEgg.randomCellQtyPerGroup,
                                            xEgg.randomInputQtyPerCell,xEgg.randomOutputQtyPerCell))
            self.addOrganDescs()

    def variation(self,f):
        i=nextInt(100)
        if i<=95:
            return f
        if i<=99:
            rate=0.05
        else:
            rate=0.1
        return float(f*(nextFloat()*2*rate+1-rate))

    def createBrandNewEgg(self):#随即制造一个新的Egg
        egg=Egg()
        for i in range(egg.randomCellGroupQty):
            egg.cellGroups.append(CellGroup(FROG_BRAIN_LENGTH,egg.randomCellQtyPerGroup,
                                            egg.randomInputQtyPerCell,egg.randomOutputQtyPerCell))
        egg.addOrganDescs()
        return egg

    def addOrganDescs(self):
        self.organDescs=[]
        self.organDescs.append(OrganDesc(Organ.HUNGRY,300,100,100))
        self.organDescs.append(OrganDesc(Organ.UP,800,400,60))
        self.organDescs.append(OrganDesc(Organ.DOWN,800,100,60))
        self.organDescs.append(OrganDesc(Organ.LEFT,700,250,60))
        self.organDescs.append(OrganDesc(Organ.RIGHT,900,250,60))
        self.organDescs.append(OrganDesc(Organ.EAT,0,0,0))