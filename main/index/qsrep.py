
class Stuctural:
    def __init__(self):
        
        self.steel_weights = {
            'round': {
                '2': {'size': '1/4', 'Diameter': 0.25, 'wpf': 0.167},
                '3': {'size': '3/8', 'Diameter': 0.375, 'wpf': 0.376},
                '4': {'size': '1/2', 'Diameter': 0.5, 'wpf': 0.668},
                '5': {'size': '5/8', 'Diameter': 0.625, 'wpf': 1.043},
                '6': {'size': '3/4', 'Diameter': 0.75, 'wpf': 1.502},
                '7': {'size': '7/8', 'Diameter': 0.875, 'wpf': 2.044},
                '8': {'size': '1', 'Diameter': 1, 'wpf': 2.67},
                '9': {'size': '1-1/8', 'Diameter': 1.128, 'wpf': 3.4},
                '10': {'size': '1-1/4', 'Diameter': 1.27, 'wpf': 4.303},
            },
            'square': {},
            'flat': {},
            'plate': {},
            'hollow': {}
        }

    def partmortar(self, mortar, ratio=(1, 3)):
        ''' Returns the amount of materials parts in a given mortar batch by
        mix ratio. 
        '''
        part_cement = ratio[0]
        part_sand = ratio[1]
        const = float(sum(ratio))

        cement = (part_cement/const)*mortar
        sand = (part_sand/const)*mortar

        return dict(
            cement=(round(cement, 2)),
            sand=round(sand, 2))

    def partconcrete(self, concrete, ratio=(1, 3, 5)):
        ''' Returns the amount of materials parts in a given concrete batch by
            mix ratio. 
        '''
        part_cement = ratio[0]
        part_sand = ratio[1]
        part_stone = ratio[2]
        const = float(sum(ratio))

        cement = (part_cement/const)*concrete
        sand = (part_sand/const)*concrete
        stone = (part_stone/const)*concrete

        return dict(
            cement=(round(cement, 2)),
            sand=round(sand, 2),
            stone=round(stone, 2))

    # Blocks

    def cblocks(self, area):
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
                'corefill': core_fill},
            'wall': {
                'blocks': round(area / block_area),
                'concrete': round(area / block_area)*core_fill,
                'mortar': 0.03 * round(area / block_area)  # cuft
            }

        }
        return data

    def wallBars(self, length, height, vbar_spacing, hbar_spacing):
        ''' Returns the amount of vertical and horizontal bars of the given
            wall area.
            Requires the wall length, height, vertical and horizontal bar spacing.

            To be implemented: 
                1. return bar weights given the bar types.
        '''
        rebars = {
            'vbars': round(((length/vbar_spacing)*height)/29.5, 2),
            'hbars': round(((height/hbar_spacing)*length)/29.5, 2)
        }
        return rebars


structurals = Stuctural()
    
# CMU Walls


class Walls(Stuctural):

    def __init__(self, length, height, op={}):
        self.height = float(height)
        self.length = float(length)
        self.area = self.height * self.length
        wall_parts = Stuctural()
        openings = []
        jambs = []
        lintols = []
        vbars = []
        hbars = []
        for i in op:
            copening = Opening(op[i]['w'], op[i]['h'], 'opening', op[i]['amt'])
            openings.append(copening.data['total_oArea'])
            jambs.append(copening.data['oJamb'])
            lintols.append(copening.data['oHead'])
            vbars.append(copening.data['vbars'])
            hbars.append(copening.data['hbars'])

        self.openings = {
            'area': sum(openings),
            'jambs': sum(jambs),
            'lintols': sum(lintols),
            'vbars': sum(vbars),
            'hbars': sum(hbars)
        }
        wall_area = self.area - self.openings['area']
        rebars = structurals.wallBars(self.length, self.height, 1.33, 2)
        wall_vbars = rebars['vbars']
        wall_hbars = rebars['hbars']

        self.wall = {
            'area': wall_area,
            'blocks': wall_parts.cblocks(wall_area),
            'flats': self.openings['jambs'],
            'horizontalBars': wall_hbars - self.openings['hbars'],
            'length': self.length,
            'lintols': self.openings['lintols'],
            'roughCast': wall_area * 2,
            'render': wall_area * 2,
            'verticalBars': wall_vbars - self.openings['vbars']
        }

    def __repr__(self):
        return '<Wall {}'.format(str(self.wall))


class Opening:
    def __init__(self, width, height, otype, oamt=1):
        ''' Returns the total area, total jamb dressing, total lintols,
            the vertical and horizontal bars used in the wall and the
            given opening specifications.
        '''

        headOverhang = 1.33
        oarea = width*height

        rebars = structurals.wallBars(width, height, 1.33, 2)

        self.data = {'oHead': ((width + headOverhang)*oamt),
                'oJamb': round((((width*2)+(height*2))*oamt), 2),
                'total_oArea': round((oarea*oamt), 2),
                'oarea': oarea,
                'width': width,
                'height': height,
                'oamt': oamt,
                'vbars': rebars['vbars']*oamt,
                'hbars': rebars['hbars']*oamt,
                'otype': otype


                }

        
