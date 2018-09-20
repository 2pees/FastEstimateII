

from main.index.models import Beam

class SteelWeights:
    def __init__(self):
        self.steel_weights = {
                'round': {
                        '2': { 'size': '1/4', 'Diameter': 0.25, 'wpf': 0.167 },
                        '3': { 'size': '3/8', 'Diameter': 0.375, 'wpf': 0.376 },
                        '4': { 'size': '1/2', 'Diameter': 0.5, 'wpf': 0.668 },
                        '5': { 'size': '5/8', 'Diameter': 0.625, 'wpf': 1.043 },
                        '6': { 'size': '3/4', 'Diameter': 0.75, 'wpf': 1.502 },
                        '7': { 'size': '7/8', 'Diameter': 0.875, 'wpf': 2.044 },
                        '8': { 'size': '1', 'Diameter': 1, 'wpf': 2.67 },
                        '9': { 'size': '1-1/8', 'Diameter': 1.128, 'wpf': 3.4 },
                        '10': { 'size': '1-1/4', 'Diameter': 1.27, 'wpf': 4.303 },
                        },
                'square': {},
                'flat': {},
                'plate': {},
                'hollow': {}
                }

weight = SteelWeights()
stw = weight.steel_weights
'''
print(stw['round']['3'])
print(stw['round']['4'])
print(stw['round']['5'])
'''

def partmortar(mortar, ratio=(1,3)):
    ''' Returns the amount of materials parts in a given mortar batch by
        mix ratio. 
    '''
    part_cement=ratio[0]
    part_sand=ratio[1]
    const=float(sum(ratio))

    cement=(part_cement/const)*mortar
    sand = (part_sand/const)*mortar
        
    return dict(
            cement=(round(cement,2)),
            sand=round(sand,2))

def partconcrete(concrete, ratio=(1,3,5)):
    ''' Returns the amount of materials parts in a given concrete batch by
        mix ratio. 
    '''
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
            stone =round(stone,2) )
                   
        

# Blocks 
def cblocks(area):
    ''' Returns the amount of blocks, concrete and mortar required 
        to build a given wall area of blockwall. 
    '''
    length = 15.75/12.0
    width = 5.75/12
    height = 7.75/12
    block_area = length * height
    core_fill = 0.148
    data = {
            'block': {
            'type': '6 x 8 x 16 inch CMU Block',
            'length': length,
            'width': width,
            'depth': height,
            'area': block_area,
            'corefill': core_fill },
            'wall':{
            'blocks': round(area / block_area),
            'concrete': round(area / block_area)*core_fill,
            'mortar': 0.03 * round(area / block_area) # cuft
            }
            
            }
    return data
def wallBars(length, height, vbar_spacing, hbar_spacing):
    ''' Returns the amount of vertical and horizontal bars of the given
        wall area.
        Requires the wall length, height, vertical and horizontal bar spacing.
        
        To be implemented: 
            1. return bar weights given the bar types.
    '''
    rebars = {
     'vbars': round(((length/vbar_spacing)*height)/29.5,2),
     'hbars': round(((height/hbar_spacing)*length)/29.5,2) 
     }
    return rebars

#print(wallBars(4,4,1.33,2),' Each' ) 
 
def opening(width, height, otype, oamt=1): 
        ''' Returns the total area, total jamb dressing, total lintols,
            the vertical and horizontal bars used in the wall and the
            given opening specifications.
        '''
        headOverhang = 1.33
        oarea = width*height
    
        rebars = wallBars(width, height, 1.33, 2)
    
       
                 
        data={ 'oHead':(( width + headOverhang)*oamt),
                'oJamb':round((( (width*2)+(height*2))*oamt),2),
                'total_oArea':round((oarea*oamt),2),
                'oarea':oarea,
                 'width':width,
                'height':height,
                'oamt':oamt,
                'vbars':rebars['vbars']*oamt,
                'hbars':rebars['hbars']*oamt,
                'otype':otype
                                
                
                }         
        
        return data
#print(opening(4,4,'w1',1))


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
        self.data['rebar'] = rebar

        return rebar
    

class Column:
    def __init__(self, width, depth, height, amt):
        self.width = width; self.depth = depth; self.height = height
        self.amt = amt
        
        self.rebars
        
        self.cover = 0.166 # cover of reinforcement in feet
        self.rebarLength = 29.5
        self.bend = 0.5
        
        self.formwork = (((self.width + self.depth) * 2) * self.height) * self.amt
        self.concrete = ((self.width * self.depth) * self.height) * self.amt
        
    def rebars(self, bar_type='5/8 inch', amt_longbars=4, link_type='3/8 inch', link_spacing=0.667):
        long_bars = ( amt_longbars * (self.height + self.bend)) / self.rebarLength
        
        links = int( round(self.height / link_spacing)) + 2 # add 2 extra link
        link_length = ((self.width +self.depth) * 2 ) - (self.cover * 4 ) + .433
        linkBars = round( (( link_length * links ) / self.rebarLength ), 2 )

        rebar = {
                'reinfment': {
                        'mainbars': {
                        'amt': int( round( long_bars )),#add 1 extra bar
                        'bartype': bar_type,
                        'bars': amt_longbars,
                        'pounds': 0,
                        'ton': 0
                        },
                'stirrups': {
                        'amt': links,
                        'doz': round(links / 12.0, 2),
                        'bartype': link_type,
                        'length': link_length,
                        'bars': int( round( linkBars )),
                        'pounds': 0,
                        'ton': 0
                        }
            
                }
        					
        	}

        return rebar
        
    
    def report(self):
        return {
                'report': 'Structural Column',
                'formwork': {
                        'sqft': self.formwork,
                        'sqyd': round( self.formwork / 9.0 )
                        },
                'concrete': {
                        'cuft': self.concrete, 
                        'cuyd': round(self.concrete / 27.0, 2)
                        },
                'reinfment': self.rebars(),
                'log':{
                        'mainbars': {
                        'amt': 0,
                        'bartype': '5/8 inch',
                        'bars':0,
                        'pounds': 0,
                        'ton': 0
                        },
                'stirrups': {
                        'amt': 0,
                        'doz': 0,
                        'bartype': '3/8 inch',
                        'length': 0,
                        'bars':0,
                        'pounds': 0,
                        'ton': 0
                        }
            
                }
            
        }

def test():        
    cnum = Column(.6, 1, 10, 5) 
    print(cnum.report())
#test()

class Stiffener:
    def __init__(self, width=0.5, depth=1, height=10, amt=1):
        self.width = width; self.depth = depth; self.height = height
        self.amt = amt
        self.total_length = self.height * self.amt
        
        self.rebars
        
        self.cover = 0.166 # cover of reinforcement in feet
        self.rebarLength = 29.5
        self.bend = 0.5
        
        formwork = (( self.depth * 2) * self.height) * self.amt
        self.formwork = {
                'sides': {
                        'sqft': formwork,
                        'sqyd': round( formwork / 9.0, 2 )
                        }
                }
        self.concrete = ((self.width * self.depth) * self.height) * self.amt
        
    def rebars(self, bar_type='5/8 inch', amt_longbars=4, link_type='3/8 inch', link_spacing=0.667):
        self.long_bars = (( amt_longbars * (self.height + self.bend)) / self.rebarLength ) * self.amt
        
        self.links = (int( round(self.height / link_spacing)) + 2) * self.amt # add 2 extra link
        self.link_length = ((self.width +self.depth) * 2 ) - (self.cover * 4 ) + .433
        self.linkBars = round( (( self.link_length * self.links ) / self.rebarLength ), 2 )

        rebar = {
                'mainbars': {
                        'amt': int( round( self.long_bars )) + 1,#add 1 extra bar
                        'bartype': bar_type,
                        'bars': amt_longbars,
                        'pounds': 0,
                        'ton': 0
                        },
                'stirrups': {
                        'amt': self.links,
                        'doz': round( self.links / 12.0, 2),
                        'bartype': link_type,
                        'length': self.link_length,
                        'bars': int( round( self.linkBars )),
                        'pounds': 0,
                        'ton': 0
                        }
            
                }
        					
        	
        return rebar
        
    
    def report(self):
        return {
                'report': 'Structural Stiffener',
                'data': {
                        'width': self.width,
                        'depth': self.depth,
                        'length': self.height
                        },
                'formwork': self.formwork,
                'concrete': {
                        'cuft': self.concrete, 
                        'cuyd': round(self.concrete / 27.0, 2)
                        },
                'reinfment': self.rebars()
            
               
            
        }
    
def test_2():        
    stiffener = Stiffener() 
    print(stiffener.report())
#test_2()

class Lstiffener:
    def __init__(self, width=0.5, depth=1, height=10, amt=1, bulkhead=False,
                 bulk_height=0,num_bulkhead=0):
        self.width = width; self.depth = depth; self.height = height
        self.amt = amt
        self.total_length = self.height * self.amt
        self.rebars
        
        self.cover = 0.166 # cover of reinforcement in feet
        self.rebarLength = 29.5
        self.bend = 0.5
        formwork = (( self.depth * 3) * self.height) * self.amt
        self.concrete = ((self.width * (self.depth * 1.5)) * self.height) * self.amt
        if bulkhead:
            bulk_area = (( bulk_height * self.width ) * num_bulkhead )* self.amt
            bulk_length = (bulk_height * num_bulkhead)* self.amt
            
            self.formwork = {
                    'sides': {
                            'sqft': formwork,
                            'sqyd': round(formwork / 9.0, 2)
                            },
                    'bulkhead': {
                            'sqft': bulk_area,
                            'sqyd': round(bulk_area/9.0, 2),
                            'bulk_length': bulk_length
                            }
                                           
                    }
            #self.concrete = concrete
        else:
            self.formwork = {
                    'sides': {
                            'sqft': formwork,
                            'sqyd': round(formwork / 9.0, 2)
                            }
                    }
            #self.concrete = concrete
                
               
    def rebars(self, bar_type='5/8 inch', amt_longbars=6, link_type='3/8 inch', link_spacing=0.667):
        long_bars = (( amt_longbars * (self.height + self.bend)) / self.rebarLength )* self.amt
        
        links = ( int( round(self.height / link_spacing) * 2) + 4 )* self.amt # add 2 extra link
        link_length = ((self.width +self.depth) * 2 ) - (self.cover * 4 ) + .433
        linkBars = round( (( link_length * links ) / self.rebarLength ), 2 )

        rebar = {
                'mainbars': {
                        'amt': int( round( long_bars )) + 1,#add 1 extra bar
                        'bartype': bar_type,
                        'bars': amt_longbars,
                        'pounds': 0,
                        'ton': 0
                        },
                'stirrups': {
                        'amt': links,
                        'doz': round( links / 12.0, 2),
                        'bartype': link_type,
                        'length': link_length,
                        'bars': int( round( linkBars )),
                        'pounds': 0,
                        'ton': 0
                        }
            
                }
        					
        	

        return rebar
        
    
    def report(self):
        return {
                'report': 'Structural L Stiffener',
                'data': {
                        'width': self.width,
                        'depth': self.depth,
                        'length': self.height
                        },
                'formwork': self.formwork,
                'concrete': {
                        'cuft': self.concrete, 
                        'cuyd': round(self.concrete / 27.0, 2)
                        },
                'reinfment': self.rebars()
            
               
            
        }
                

    
def test_3():        
    stiffener = Lstiffener(bulkhead=True,
                 bulk_height=8,num_bulkhead=3) 
    print(stiffener.report())
#test_3()
def test_4():        
    stiffener = Lstiffener() 
    print(stiffener.report())
#test_4()

class Tstiffener:
    def __init__(self, width=0.5, depth=1, height=10, amt=1, bulkhead=False,
                 bulk_height=0,num_bulkhead=0):
        self.width = width; self.depth = depth; self.height = height
        self.amt = amt
        self.total_length = self.height * self.amt
        self.rebars
        
        self.cover = 0.166 # cover of reinforcement in feet
        self.rebarLength = 29.5
        self.bend = 0.5
        formwork = (((( self.depth * 3) + 0.5) * self.height) * self.amt)
        self.concrete = ((self.width * (self.depth * 2)) * self.height) * self.amt
        if bulkhead:
            bulk_area = (( bulk_height * self.width ) * num_bulkhead )* self.amt
            bulk_length = (bulk_height * num_bulkhead)* self.amt
            
            self.formwork = {
                    'sides': {
                            'sqft': formwork,
                            'sqyd': round(formwork / 9.0, 2)
                            },
                    'bulkhead': {
                            'sqft': bulk_area,
                            'sqyd': round(bulk_area/9.0, 2),
                            'bulk_length': bulk_length
                            }
                                           
                    }
            #self.concrete = concrete
        else:
            self.formwork = {
                    'sides': {
                            'sqft': formwork,
                            'sqyd': round(formwork / 9.0, 2)
                            }
                    }
            #self.concrete = concrete
                
               
    def rebars(self, bar_type='5/8 inch', amt_longbars=8, link_type='3/8 inch', link_spacing=0.667):
        long_bars = (( amt_longbars * (self.height + self.bend)) / self.rebarLength )* self.amt
        
        links = (int( (round(self.height / link_spacing))*3) + 2 )* self.amt # add 2 extra link
        link_length = ((self.width +self.depth) * 2 ) - (self.cover * 4 ) + .433
        linkBars = round( (( link_length * links ) / self.rebarLength ), 2 )

        rebar = {
                'mainbars': {
                        'amt': int( round( long_bars )) + 1,#add 1 extra bar
                        'bartype': bar_type,
                        'bars': amt_longbars,
                        'pounds': 0,
                        'ton': 0
                        },
                'stirrups': {
                        'amt': links,
                        'doz': round( links / 12.0, 2),
                        'bartype': link_type,
                        'length': link_length,
                        'bars': int( round( linkBars )),
                        'pounds': 0,
                        'ton': 0
                        }
            
                }
        					
        	

        return rebar
        
    
    def report(self):
        return {
                'report': 'Structural T Stiffener',
                'data': {
                        'width': self.width,
                        'depth': self.depth,
                        'length': self.height
                        },
                'formwork': self.formwork,
                'concrete': {
                        'cuft': self.concrete, 
                        'cuyd': round(self.concrete / 27.0, 2)
                        },
                'reinfment': self.rebars()
            
               
            
        }
                

    
def test_5():        
    stiffener = Tstiffener(bulkhead=True,
                 bulk_height=8,num_bulkhead=3) 
    print(stiffener.report())
#test_5()
def test_6():        
    stiffener = Tstiffener() 
    print(stiffener.report())
#test_6()
          


class Walls:
                    
    def __init__(self, length, height, op = {}):
        self.height = float(height)
        self.length = float(length)
        self.area = self.height * self.length
        openings = []
        jambs = []
        lintols = []
        vbars = []
        hbars = []
        for i in op:
            copening = opening(op[i]['w'],op[i]['h'],'opening',op[i]['amt'])
            openings.append(copening['total_oArea'])
            jambs.append(copening['oJamb'])
            lintols.append(copening['oHead'])
            vbars.append(copening['vbars'])
            hbars.append(copening['hbars'])
            
        self.openings = {
        'area': sum(openings),
        'jambs': sum(jambs),
        'lintols': sum(lintols),
        'vbars':sum(vbars),
        'hbars':sum(hbars)        
        }
        wall_area = self.area - self.openings['area']
        rebars = wallBars(self.length,self.height,1.33,2)
        wall_vbars = rebars['vbars']  
        wall_hbars = rebars['hbars'] 
        beams = Beam.query.all() 
        
        
        self.wall = {
                'area': wall_area,  
                'blocks': cblocks(wall_area), 
                'flats': self.openings['jambs'],
                'horizontalBars': wall_hbars - self.openings['hbars'],
                'length': self.length,
                'lintols': self.openings['lintols'],
                'roughCast': wall_area * 2,
                'render': wall_area * 2,
                'verticalBars': wall_vbars - self.openings['vbars']
               
               
                
                }


if __name__=='__main__':

    #print('#############################################################################################')             
    def ridgewood_ffl_walls():
        height = 10
        height2 = 13 
        thick = 0.5
        #data = []       
        allwall = [ { 'tag':'w1', 'length':28.5, 'height': height2, 'openings': {'t1':{'w':3,'h':4,'amt':2},'t2':{'w':3,'h':7,'amt':1}} }
           ,{ 'tag':'w2', 'length':31.5, 'height': height2, 'openings':{'t1':{'w':4,'h':4,'amt':3}}}
           ,{ 'tag':'w3', 'length':26.667, 'height': height2, 'openings':{'t1':{'w':3,'h':2,'amt':2}}}
           ]
        #walls_data = []
        wareas,blocks,concrete,mortar,flats,hbars,vbars,lintols,render,rough, belt = [],[],[],[],[],[],[],[],[],[],[] 
        for item in allwall:
            #print(item)
            ff = Walls(item['length'], item['height'], item['openings'])
            wall = ff.wall
            blocks.append(wall['blocks']['wall']['blocks'])
            concrete.append(wall['blocks']['wall']['concrete'])
            mortar.append(wall['blocks']['wall']['mortar'])
            belt.append(wall['length'])
            render.append(wall['render'])
            rough.append(wall['roughCast'])
            flats.append(wall['flats'])
            hbars.append(wall['horizontalBars'])
            vbars.append(wall['verticalBars'])  
            lintols.append(wall['lintols'])
            wareas.append(wall['area'])

        # Structurals
        # Lintols 
        lintol_ = BEAM(thick,sum(lintols),1)
        lintol_data = lintol_.data
        # BeltCourse
        belt = BELTCOURSE(thick,sum(belt),1.5)
        belt_data = belt.data

        qs_report = {
                'walls':{
                        'units':['sqft','rnft','length'],
                        'wallAreas': sum(wareas),
                        'blocks': sum(blocks),
                        'concrete': sum(concrete),
                        'granite': (sum(render)+(sum(flats)*.667))*(.5/12),
                        'mortar': sum(mortar) + ((sum(rough) + (sum(flats)*.667))*(.5/12)),
                        'render': sum(render),
                        'roughcast': sum(rough),
                        'flatJambs': sum(flats),
                        'vbars': sum(vbars),
                        'hbars': sum(hbars)
                        }, 
                'structurals':{
                        'lintols': {
                                'lintol': lintol_data,
                                'reinfment': lintol_.rebars(4,'m10', 0.667)
                                },
                        'beltCourse': {
                                'belt': belt_data,
                                'reinfment': belt.rebars(6,'m12', 0.75)
                                }
                        }
                    }
        
        return qs_report


    #print( 'Executing Quantity report.' )
    #print( ridgewood_ffl_walls() )
    
    def ridgewood_ffl_stiffeners():
        height = 10
        height2 = 13 
        data = []      
        
        stiffeners = [
                    {
                    'type':'stiffener',
                    'width': 0.5,
                    'depth': 1,
                    'height': height2,
                    'amt': 5
                    }
                    
                    ]
                            
        l_stiffeners = [
                    {
                    'type':'l_stiffener',
                    'width': 0.5,
                    'depth': 1,
                    'height': height2,
                    'amt': 2
                    }
                   
                    ]
        t_stiffeners = [
                    {
                    'type':'t_stiffener',
                    'width': 0.5,
                    'depth': 1,
                    'height': height2,
                    'amt': 1
                    }
                    ]
        
        formwork,concrete,mainbars,stirrups,stirrup_bars = [],[],[],[],[]
        i_stiff,l_stiff,t_stiff = [],[],[]
        for item in stiffeners:
            stiffener = Stiffener(item['width'],item['depth'],item['height'],item['amt'])
            i_stiff.append(stiffener.total_length)
            formwork.append(stiffener.formwork['sides']['sqft'])
            concrete.append(stiffener.concrete)
            rebars = stiffener.report()
            mainbars.append(rebars['reinfment']['mainbars']['amt'])
            stirrup_bars.append(rebars['reinfment']['stirrups']['bars'])
            stirrups.append(rebars['reinfment']['stirrups']['doz'])
            data.append( stiffener.report() )
            #print(i_stiffener.report())
        #print(data)
        
        for ls_ in l_stiffeners:
            l_stiffener = Lstiffener(ls_['width'],ls_['depth'],ls_['height'],ls_['amt'])
            l_stiff.append(l_stiffener.total_length)
            formwork.append(l_stiffener.formwork['sides']['sqft'])
            concrete.append(l_stiffener.concrete)
            rebars = l_stiffener.report()
            mainbars.append(rebars['reinfment']['mainbars']['amt'])
            stirrup_bars.append(rebars['reinfment']['stirrups']['bars'])
            stirrups.append(rebars['reinfment']['stirrups']['doz'])
            data.append( l_stiffener.report() )
            #print(i_stiffener.report())
        #print(data)
        
        for ts_ in t_stiffeners:
            t_stiffener = Tstiffener(ts_['width'],ts_['depth'],ts_['height'],ts_['amt'])
           
            t_stiff.append(t_stiffener.total_length)
            formwork.append(t_stiffener.formwork['sides']['sqft'])
            concrete.append(t_stiffener.concrete)
            rebars = t_stiffener.report()
            mainbars.append(rebars['reinfment']['mainbars']['amt'])
            stirrup_bars.append(rebars['reinfment']['stirrups']['bars'])
            stirrups.append(rebars['reinfment']['stirrups']['doz'])
            data.append( t_stiffener.report() )
            #print(i_stiffener.report())
       
        print('""""""""""""""""""""""""""""""""""""')
        #print('''formwork sqft: {} \n concrete cuft : {} \n mainbars length : {} \n stirrupbars length: {} 
        #stirrups doz: {}'''.format(formwork,concrete,mainbars,stirrup_bars,stirrups),i_stiff,l_stiff,t_stiff)
        summary = {
                'summary': {
                'stiffeners': {
                        'I rnft': sum(i_stiff),
                        'L rnft': sum(l_stiff),
                        'T rnft': sum(t_stiff)
                        },
                'formwork sqft': sum(formwork),
                'concrete cuft': sum(concrete),
                'mainbars length': sum(mainbars),
                'stirrup bars': sum(stirrup_bars),
                'stirrup doz': sum(stirrups)
                
                }
                }
        data.append(summary)
        print(summary)
        
        return data
            
        #stiffener = Stiffener() 
        #print(stiffener.report())
    #ridgewood_ffl_stiffeners()
    
