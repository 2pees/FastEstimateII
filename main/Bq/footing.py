 #!/usr/bin/env python
# -*- coding: utf-8 -*-

from units import UnitsLog
from cnotes import Notes

getunits=UnitsLog()
units=getunits.unit_log()
getnotes=Notes()
note=getnotes.connote()

class TOPSOIL:
    def __init__(self,width,length,depth):       
        self.width=float(width)
        self.length=float(length)
        self.depth=float(depth)           
        self.excavation=self.depth*self.length*self.width
        self.area=self.length*self.width
        self.snote=(note['excavation']['exc']+note['excavation']['topsoil']+note['excavation']['dispose'])
        self.data=dict(
            note=self.snote,
            length=self.length,
            width=self.width,
            depth=self.depth,
            area=self.area,
            excavation={'cuft':self.excavation,
        		    'cuyd':round(self.excavation/27,2)
                             }
            )
   
##-----------------------------------------------------------------------------------##    


class STRIP:
    def __init__(self,width,depth,length,thickness):
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
        self.thickness=thickness
           
        self.excavation=round(self.width*self.depth*self.length,2)
        self.concrete=round(self.width*self.thickness*self.length,2)
        fww=self.width/3 #approximate width of footing wall
        fwh=self.depth-self.thickness #approximate height of footing wall 
        self.backfill=round(self.excavation-((fww*fwh*self.length)+self.concrete),2)##approximate footing wall volumr + footing volume
        self.notexc=(note['excavation']['exc']+note['structural']['fdn']+note['excavation']['dispose'])
        self.notebackfill=(note['excavation']['backfill'])
        self.notecon=(note['concrete']['mix']+note['concrete']['r124']+note['concrete']['conc']+note['structural']['fdn'])
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            thickness=self.thickness, 
            note= {'excavation':self.notexc,
                    'backfill':self.notebackfill,
                    'concrete':self.notecon
                    },                   	
        
            excavation={'cuft':self.excavation,
        		    'cuyd':round(self.excavation/27,2)
                             },
            concrete= {'cuft':self.concrete,
                            'cuyd':round(self.concrete/27,2)
                            },
            backfill= {'cuft':self.backfill,
                            'cuyd':round(self.backfill/27,2)
                            }
            )
        			
        
                    
    def rebars(self,amt_longbars,link_type,link_spacing):
        long_bars=(amt_longbars*self.length)/29.5
        links=int(round(self.length/link_spacing))+2 # add 2 extra link
        link_length=(self.width-0.25)+0.5
        barnote={'mainbar':note['rebar']['cut']+note['rebar']['brs']+note['structural']['fdn'],
              'links':note['rebar']['fab']+note['rebar']['lnk']
              }
        
        return dict(rebar={'mainBar':int(round(long_bars))+1,#add 1 extra bar
        		    'links':links,
        		    'linkLength':link_length,
        		    'linkBars': int(round((link_length*links)/29.5)),
                            'note':barnote
        					
        					}
        					
                    )
##-----------------------------------------------------------------------------------##          
class PAD:
    def __init__(self,width,length,depth,thickness):
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
        self.thickness=thickness
           
        self.excavation=self.width*self.depth*self.length
        self.concrete=self.width*self.thickness*self.length
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            thickness=self.thickness,        
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            },       	
        
            excavation={'cuft':self.excavation,
        		    'cuyd':self.excavation/27
                             }
            )
        			
        
                    
    def rebars(self,mainbar_spacing,distbar_spacing):
        if self.width>self.length:
            width=self.length
            length=self.width
        else:
            width=self.width
            length=self.length
        print("TEST ::::",width,length)
        main_bars=(((width/mainbar_spacing)*length)+(self.bend*2))/self.rebarLength
        dist_bars=(((length/distbar_spacing)*width)+(self.bend*2))/self.rebarLength
        
        
        return dict(rebar={'mainBar':int(round(main_bars)),#add 1 extra bar
                            'distributionBars':int(round(dist_bars)),#add 1 extra bar,
                           'amt_mainBar':int(round(width/mainbar_spacing)),
                           'amt_distBar':int(round(length/distbar_spacing)),
        		    'mainbarLength':(width+(self.bend*2)),
        		    'distributionBarLength': int(round((length+(self.bend*2))))
        					
        					}
        					
                    )
##-----------------------------------------------------------------------------------## 
class PILE:
    def __init__(self,width,depth,length,thickness):
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
        self.thickness=thickness
           
        self.excavation=self.width*self.depth*self.length
        self.concrete=self.width*self.thickness*self.length
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            thickness=self.thickness,        
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            },       	
        
            excavation={'cuft':self.excavation,
        		    'cuyd':self.excavation/27
                             }
            )
        			
        
                    
    def rebars(self,amt_longbars,link_type,link_spacing):
        long_bars=(amt_longbars*self.length)/29.5
        links=int(round(self.length/link_spacing))+2 # add 2 extra link
        link_length=(self.width-0.25)+0.5
        
        return dict(rebar={'mainBar':int(round(long_bars))+1,#add 1 extra bar
        					'links':links,
        					'linkLength':link_length,
        					'linkBars': int(round((link_length*links)/29.5))
        					
        					}
        					
                    )

##-----------------------------------------------------------------------------------## 
class RAFT:
    def __init__(self,width,length,depth,thickness):
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
        self.thickness=thickness
           
        self.excavation=self.width*self.depth*self.length
        self.concrete=self.width*self.thickness*self.length
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            thickness=self.thickness,        
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            },       	
        
            excavation={'cuft':self.excavation,
        		    'cuyd':self.excavation/27
                             }
            )
        			
        
                    
    def rebars(self,amt_longbars,link_type,link_spacing):
        long_bars=(amt_longbars*self.length)/29.5
        links=int(round(self.length/link_spacing))+2 # add 2 extra link
        link_length=(self.width-0.25)+0.5
        
        return dict(rebar={'mainBar':int(round(long_bars))+1,#add 1 extra bar
        					'links':links,
        					'linkLength':link_length,
        					'linkBars': int(round((link_length*links)/29.5))
        					
        					}
        					
                    )

##----------------------------------- END ------------------------------------------------## 
def test():
    foot=STRIP(1.5,3,86.67,.75)
    data=foot.data

    pad=PAD(4,3,10,2)

    print("STRIP FOUNDATION:\n",(data),"\nrebars:\n",foot.rebars(3,'m10',.667))
     #"PAD FOUNDATION:\n",pad.data,pad.rebars(0.5,0.667)


    
