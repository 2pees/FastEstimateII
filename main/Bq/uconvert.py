hl =25
hw = 12+12+14
hp = (hl*2)+(hw*2)
hh = 10

hi_1=24.5
hi_2 = hi_1
hi_1a = hi_1 * hh
hi_2a = hi_2

hi_3 = 14
hi_4 = hi_3

hi5 = 12
hi_6 = 14
h7 = hi_6

def partmortar(mortar, ratio=(1,3)):
    part_cement=ratio[0]
    part_sand=ratio[1]
    const=float(sum(ratio))

    cement=(part_cement/const)*mortar
    sand = (part_sand/const)*mortar
        
    return dict(
            cement=(round(cement,2)),
            sand=round(sand,2))

def partconcrete(concrete, ratio=(1,3,5)):
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
        length = 15.75/12.0
        width = 5.75/12
        height = 7.75/12
        block_area = length * height
        core_fill = (block_area*width)*0.80
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
    rebars = {
     'vbars': round(((length/vbar_spacing)*height)/29.5,2),
     'hbars': round(((height/hbar_spacing)*length)/29.5,2) 
     }
    return rebars

print(wallBars(4,4,1.33,2),' Each' ) 
 
def opening(width, height, otype, oamt=1): 
        '''  width height and amount of a opening type
        returns lintel, jamb and area'''
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
print(opening(4,4,'w1',1))
# Walls

class Walls:
                    
    def __init__(self, length, height, op = {}):
        self.height = height
        self.length = length
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
    
print('#############################################################################################')             
#ff = Walls(hl,hh)
height = 10
height2 = 13 
data = []       
allwall = [ { 'tag':'w1', 'length':25.5, 'height': height, 'openings': {'t1':{'w':3,'h':2,'amt':1},'t2':{'w':2.5,'h':4,'amt':2}} }
           ,{ 'tag':'w2', 'length':24.5, 'height': height, 'openings':{'t1':{'w':4,'h':8,'amt':1}}}
           ,{ 'tag':'w3', 'length':24.5, 'height': height, 'openings':{'t1':{'w':3,'h':7,'amt':1}}}
           ,{ 'tag':'w4', 'length':25.5, 'height': height2, 'openings':{'t1':{'w':3,'h':2,'amt':1}, 't2':{'w':4,'h':4,'amt':1}}}
           ,{ 'tag':'w5', 'length':14.5, 'height': height2, 'openings':{'t1':{'w':4,'h':4,'amt':1}}}
           ,{ 'tag':'w6', 'length':25, 'height': height, 'openings':{'t1':{'w':4,'h':4,'amt':1}, 't2':{'w':10,'h':8,'amt':1}}}
           ,{ 'tag':'w7', 'length':14, 'height': height2, 'openings':{'t1':{'w':4,'h':4,'amt':1}, 't2':{'w':3,'h':7,'amt':1}}}
           ,{ 'tag':'w8', 'length':14, 'height': height2, 'openings':{'t1':{'w':3,'h':2,'amt':1}, 't2':{'w':3,'h':7,'amt':1}}}
           ,{ 'tag':'w9', 'length':25, 'height': height, 'openings':{'t1':{'w':4,'h':6,'amt':1}, 't2':{'w':3,'h':2,'amt':1}}}
           ,{ 'tag':'w10', 'length':12.5, 'height': height, 'openings':{'t1':{'w':3,'h':7,'amt':1}}}
           ,{ 'tag':'w11', 'length':13, 'height': height, 'openings':{'t1':{'w':4,'h':3,'amt':1}, 't2':{'w':3,'h':7,'amt':1}}}
           ]
walls_data = []
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

qs_report = {
        'units':['sqft','rnft','length'],'wallAreas': sum(wareas),
        'blocks': sum(blocks), 'concrete': sum(concrete),
        'mortar': sum(mortar), 'render': sum(render), 'roughcast': sum(rough),
        'flatJambs': sum(flats), 'lintols': sum(lintols), 'hbars': sum(hbars),
        'vbars': sum(vbars), 'beltCourse': sum(belt)}
print(qs_report)
qs2_report = {
        'units':['sqyd','rnft','length','each','cuyd'],'wallAreas': sum(wareas)/9,
        'blocks': sum(blocks), 'concrete': sum(concrete)/27,
        'mortar': sum(mortar)/27, 'render': sum(render)/9, 'roughcast': sum(rough)/9,
        'flatJambs': sum(flats), 'lintols': sum(lintols), 'hbars': sum(hbars),
        'vbars': sum(vbars), 'beltCourse': sum(belt)}
print(qs2_report)