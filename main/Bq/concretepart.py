#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *

class ConcreteParts:
    def __init__(self):
        self.note='concrete'
    def partmortar(self,mortar, ratio=(1,3)):
        
        part_cement=ratio[0]
        part_sand=ratio[1]
        const=float(sum(ratio))

        cement=(part_cement/const)*mortar
        sand = (part_sand/const)*mortar
        
        return dict(
                    cement=(round(cement,2)),
                    sand=round(sand,2)
                )

    def partconcrete(self,concrete, ratio=(1,3,5)):
        
        part_cement=ratio[0]
        part_sand=ratio[1]
        part_stone=ratio[2]
        const=float(sum(ratio))

        cement=(part_cement/const)*concrete
        sand = (part_sand/const)*concrete
        stone = (part_stone/const)*concrete
        
        return dict(
                    cement=(round(cement,2)),
                    sand=round(sand,2),
                    stone =round(stone,2)
                    
                )
                   
        

        
        
mat=ConcreteParts()

mparts=mat.partmortar(1)
cparts=mat.partconcrete(1)
                   
print mparts,cparts                   

