 
# -*- coding: utf-8 -*-
#from gluon import *

class BELTCOURSE:
    def __init__(self,width,length,depth):
        self.cover=0.166 # cover of reinforcement in feet
        self.rebarLength=29.5
        self.bend=0.5
        
        self.width=width
        self.depth=depth
        self.length=length
              
        
        self.concrete=self.width*self.depth*self.length
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            formwork=round(((self.depth*self.length)*2),3),        
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            }       	
        
            
            )

       

    
                    
    def rebars(self,amt_longbars,link_type,link_spacing):
        long_bars=(amt_longbars*self.length)/self.rebarLength
        links=int(round(self.length/link_spacing))+2 # add 2 extra link
        link_length=((self.width +self.depth)*2)-(self.cover*4)+.433
        linkBars = round(((link_length*links)/self.rebarLength),3)

        rebar={'mainBar':int(round(long_bars))+1,#add 1 extra bar
        		    'links':links,
        		    'linkLength':link_length,
        		    'linkBars': int(round(linkBars))
        					
        					}

        return rebar
        
class BEAM:
    def __init__(self,width,length,depth):
        self.cover=0.166 # cover of reinforcement in feet
        self.rebarLength=29.5
        self.bend=0.5
        self.cover=0.166
        self.width=width
        self.depth=depth
        self.length=length
              
        
        self.concrete=self.width*self.depth*self.length
        

        self.data=dict(
            length=self.length,
            width=self.width,
            depth=self.depth,
            formwork=round((((self.depth*2)+self.width)*self.length),3),
            
            concrete= {'cuft':self.concrete,
                            'cuyd':self.concrete/27
                            }       	
        
            
            )

       

    
                    
    def rebars(self,amt_longbars,link_type,link_spacing):
        long_bars=(amt_longbars*self.length)/self.rebarLength
        links=int(round(self.length/link_spacing))+2 # add 2 extra link
        link_length=((self.width +self.depth)*2)-(self.cover*4)+.433
        linkBars = round(((link_length*links)/self.rebarLength),3)

        rebar={'mainBar':int(round(long_bars))+1,#add 1 extra bar
        		    'links':links,
        		    'linkLength':link_length,
        		    'linkBars': int(round(linkBars))
  		}

        return rebar
def main():
    print('hello you')
"""
    if __name__=='main':
   b1=BELTCOURSE(0.5,1.5,400)
           
    def test():
        b1=BELTCOURSE(0.5,1.5,400)
        data=b1.data
        return "BELTCOURSE:\n",(data),"\nrebars:\n",b1.rebars(3,'m10',1.33)
"""
   
    

