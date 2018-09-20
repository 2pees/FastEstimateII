#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *


class WallMember:
    ''' Represent window class'''
    def __init__(self):
        self.headOverhang = (0.50 * 2)
        
    def WINDOW(self, width, height, wtype,vbar_spacing,hbar_spacing, wamt=1): 
        '''  width height and amount of a window type
        returns lintel, jamb and area'''

        windowarea = width*height
    
        vbars=((width/vbar_spacing)*height)/29.5
    
        hbars=((height/hbar_spacing)*width)/29.5 
                 
        self.data={ 'windowHead':(( width + self.headOverhang)*wamt),
                'windowJamb':round((( (width*2)+(height*2))*wamt),2),
                'total_windowArea':round((windowarea*wamt),2),
                'windowarea':windowarea,
                 'width':width,
                'height':height,
                'wamt':wamt,
                'vbars':vbars*wamt,
                'hbars':hbars*wamt,
                'wtype':wtype
                                
                
                }         
        
        return self.data
        
 
    def DOOR(self, width, height, dtype,vbar_spacing,hbar_spacing, damt=1): 
            '''  width height and amount of a door type
            returns lintel, jamb and area'''

            doorarea = width*height
    
            vbars=((width/vbar_spacing)*height)/29.5
    
            hbars=((height/hbar_spacing)*width)/29.5 
                 
            self.data={ 'doorHead':(( width + self.headOverhang)*damt),
                    'doorJamb':round((( (width*2)+(height*2))*damt),2),
                'total_doorArea':round((doorarea*damt),2),
                'doorarea':doorarea,
                 'width':width,
                'height':height,
                'damt':damt,
                'vbars':vbars*damt,
                'hbars':hbars*damt,
                'dtype':dtype
                                
                
                }         
        
            return self.data


    def OPENING(self, width, height, otype,vbar_spacing,hbar_spacing, oamt=1): 
        '''  width height and amount of a opening type
        returns lintel, jamb and area'''

        oarea = width*height
    
        vbars=((width/vbar_spacing)*height)/29.5
    
        hbars=((height/hbar_spacing)*width)/29.5 
                 
        self.data={ 'oHead':(( width + self.headOverhang)*oamt),
                'oJamb':round((( (width*2)+(height*2))*oamt),2),
                'total_oArea':round((oarea*oamt),2),
                'oarea':oarea,
                 'width':width,
                'height':height,
                'oamt':oamt,
                'vbars':vbars*oamt,
                'hbars':hbars*oamt,
                'otype':otype
                                
                
                }         
        
        return self.data

def test():
    w=WallMember()
    W1=(4,4,'SASH',1.33,2.6,10)
    D1=(3,7,'PLY',1.33,2.6,3)
    O1=(8,8,'ARCHWAY',1.33,2.6,2)
    MEM=[W1,D1,O1]
    for item in MEM:
        if 'SASH' in item:
            print('WINDOW :',w.WINDOW(4,4,'SASH',1.33,2.6,10))
        elif 'PLY' in item:
            print('DOOR :',item)
        else:
            print('OPENING :',item)
            
        
#test()
