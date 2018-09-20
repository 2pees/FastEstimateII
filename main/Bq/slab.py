#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *
def runtime():
    from time import ctime
    time=ctime()
    del(ctime)
    return "Runtime: |------> {} <-------|".format(time)


class FLOORSLAB:
    def __init__(self,width,length,depth,sp):
        self.cover=0.166 # cover of reinforcement in feet
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
        self.property=sp      
        
        self.concrete=self.width*self.depth*self.length
        self.perimeter=(self.width+self.length)*2
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            perimeter=self.perimeter,
            
            
            formwork=round(((self.width*self.length)),3),        
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            }       	
        
            
            )

       

    
                    
                  
    def rebars(self,mainbar_spacing,distbar_spacing,omain_spacing,odist_spacing):

        def span(sspan):
            '''returns the quarter span of
                a slab distance'''
            return sspan/4.0
        def slabsteel(width,length,mainspacing,distspacing):
            ''' Returns a dictionary with
            '''
    
            mainlength=width
            distlength=length
            mainamt=length/mainspacing
            distamt=width/distspacing
            mainbars=(mainamt*mainlength)/29.5
            distbars=(distamt*distlength)/29.5

            return dict(
                mainlength=mainlength,
                mainamt= round(mainamt),
                mainbars=round(mainbars),
                distlength=distlength,
                distamt=round(distamt),
                distbars=round(distbars)
                ) 
        
        if self.width>self.length:
            width=self.length
            length=self.width
        else:
            width=self.width
            length=self.length

        bottombars=slabsteel(width,length,mainbar_spacing, distbar_spacing)
        if self.property=='loadbearing':
        	top1_bars=slabsteel(span(width),length,omain_spacing, odist_spacing)#x2
        	top2_bars=slabsteel(span(length),span(width)*2,omain_spacing, odist_spacing)#x2
         
         
        	rebar={'bottom_mainbar_length':bottombars['mainlength'],
               'bottom_mainbar_amount':bottombars['mainamt'],
               'bottom_mainbar':bottombars['mainbars'],

               'bottom_distributionbar_length':bottombars['distlength'],
               'bottom_distributionbar_amount':bottombars['distamt'],
               'bottom_distributionbar':bottombars['distbars'],

               
               'toplon_mainbar_length':top1_bars['mainlength']+self.bend,
               'toplon_mainbar_amount':top1_bars['mainamt']*2,
               'toplon_mainbar':((top1_bars['mainlength']+self.bend)*(top1_bars['mainamt']*2))/self.rebarLength,

               'toplon_distributionbar_length':top1_bars['distlength'],
               'toplon_distributionbar_amount':top1_bars['distamt']*2,
               'toplon_distributionbar':(top1_bars['distlength']*(top1_bars['distamt']*2))/self.rebarLength,

               'toplat_mainbar_length':top2_bars['mainlength']+self.bend,
               'toplat_mainbar_amount':top2_bars['mainamt']*2,
               'toplat_mainbar':((top2_bars['mainlength']+self.bend)*(top2_bars['mainamt']*2))/self.rebarLength,

               'toplat_distributionbar_length':top2_bars['distlength'],
               'toplat_distributionbar_amount':top2_bars['distamt']*2,
               'toplat_distributionbar':(top2_bars['distlength']*(top2_bars['distamt']*2))/self.rebarLength}


                                         
        					
        else:
            rebar={'bottom_mainbar_length':bottombars['mainlength']+self.bend,
               'bottom_mainbar_amount':bottombars['mainamt'],
               'bottom_mainbar':bottombars['mainbars'],

               'bottom_distributionbar_length':bottombars['distlength']+self.bend,
               'bottom_distributionbar_amount':bottombars['distamt'],
               'bottom_distributionbar':bottombars['distbars']}
       	
        
        return rebar


        
def test():
    print runtime()
    s1=FLOORSLAB(26,31,.5,'loadbearing')
    data=s1.data
    for key in data:
        print key, data[key]
    data=s1.rebars(.667,.667,.667,.75)
    for key in data:
        print key, data[key]

    
   

test()
        
