#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *
from concretepart import ConcreteParts

class blockWall:
    ''' Represent a cmu wall'''
    def __init__(self, length, height, walltype=6):
        self.length=length
        self.height=height
        self.walltype = walltype # type is initialised as a dictionary key shall be an int
        
        
    def cmu(self):
        self.cmu_types={4:{'type':"4inch", 'width':0.333,
                           'length':1.333, 'depth':0.667, 
                           'core_volume':0.1157, 'area': 0.88711,
                           'bag_cement':0.02, 'sand_ton': 0.004
                           
                           },
                           
                        6:{'type':"6inch", 'width':0.5,
                           'length':1.333, 'depth':0.667, 
                           'core_volume':0.178, 'area': 0.88711,
                           'bag_cement':0.02,'sand_ton': 0.004 
                           },
                           
                        8:{'type':"8inch", 'width':0.667,
                           'length':1.333, 'depth':0.667, 
                           'core_volume':0.25, 'area': 0.88711,
                           'bag_cement':0.025, 'sand_ton': 0.005
                           },

                        10:{'type':"10inch", 'width':0.833,
                            'length':1.333, 'depth':0.667, 
                           'core_volume':0.33, 'area': 0.88711,
                           'bag_cement':0.025, 'sand_ton': 0.005
                           }
                        }
        return self.cmu_types
        
    def wall(self,sproperty):
        cmu_lib=self.cmu() # assign the cmu library 
        surface_area=self.length*self.height
        cmu=cmu_lib[self.walltype]
        cmu_amount=(surface_area/cmu['area'])*1.0095 # extra over 0.95%
        core_fill=cmu_amount*cmu['core_volume']
        rendering=surface_area*2
        
        cement = cmu_amount*cmu['bag_cement']
        sand = cmu_amount*cmu['sand_ton']
        if sproperty!='loadbearing':
        	core_fill=core_fill/2
        print(type(sproperty))
        	      
       
        	
        self.data={ 'wallArea':surface_area,
                'blockData':cmu,
                'blockAmount':round(cmu_amount),
                'coreFill_ft':round(core_fill,2),
                 'coreFill_yd':round(core_fill/27,3),
                'dressing_ft':rendering,
                 'dressing_yd':round(rendering/9,2)
                 
                
                }
        
        return self.data
        
         
        
        
    def rebars(self,vbar,hbar,vbar_spacing,hbar_spacing):
        self.bend=0.5
        self.extension=0.5
        vbars=(((self.length/vbar_spacing))*(self.height+self.bend+self.extension))/29.5
        hbars=((self.height/hbar_spacing)*(self.length+(self.extension*2)))/29.5 # add 2 extra link
                
        rebar_data = dict(
            vbar_type=vbar,
            hbar_type=hbar,
            vbars=int(round(vbars+1)),
            hbars=int(round(hbars+1))
            
           )
        return rebar_data
        


wl=blockWall(10.5,12.75)
bw=wl.wall('loadbearing')
print(bw)
