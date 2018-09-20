#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *

class Notes:
    ''' A library of construction notations where keys are mapped to a
        costruction statement.
        Use: to word construction documents.
    '''
    def __init__(self):
        self.notes='Use: to word construction documents.'

    def connote(self):
        ''' returns a dictionary mapping abreviated keywords to a string
            representing a costruction statement.
        '''
        cnote={'excavation':{'exc':'to excavate for ','topsoil':'topsoil ',
                             'soil':'solid earth ','marl':'solid marl ',
                             'stone':'solid stone ','loosestone':'loose stone ',
                             'softclay':'soft clay ','sand':'loose sand ',
                             'dispose':'cart away and dispose of excavated material ',
                             'backfill':'To backfill with suitable fill and compact '
                             },
               
                             
            'concrete':{'mix':'mix place and vibrate ', 'conc':'concrete to ',
                            'r121':'1:2:1 ', 'r122':'1:2:2 ', 'r123':'1:2:3 ',
                            'r124':'1:2:4 ','r131':'1:3:1 ', 'r132':'1:3:2 ',
                            'r133':'1:3:3 ','r134':'1:3:4 ','r135':'1:3:5 ','r136':'1:3:6 '                            
                            },
               
            'rebar':{'cut':'cut bend and install ','fab':'cut and fabticate ',
                        'lnk':'links to ', 'str':'stirrups ', 'brs':'bars to ','rbr':'re-bar ',
                        'm5':'6mm ', 'm10':'10mm ', 'm12':'12mm ','m16':'16mm ', 'm20':'20mm ',
                        'm25':'25mm ',
                        '1/4':'1/4 inch ','3/8':'1/2 inch ','5/8':'5/8 inch ',
                        '3/4':'3/4 inch ','1':'1 inch '
                        },

            'structural':{'fdn':'foundation ','stf':'stiffeners ', 'clm':'columns ',
                             'lnt':'lintels ','bms':'beams ','blt':'beltcourse ',
                            'slb':'slab ', 'wll':'block walls ', 'blk':'block cores '},
               
            'wall':{'erect':'to erect ', 'wll':'block wall ', 
                       'acore':'fill alternate cores ', 'core':'fill all cores ',
                       'drw':'dry wall ','cstone':'cut stone wall ',
                       'dstone':'dressed stone wall ','rstone':'rubble stone wall ',
                       'ply':'plyboard wall ','brd':'boarded wall '
                       
                       },

            'form':{'make':'make formwork ','erect':'erect and remove formwork to ',
                       'mprop':'install and remove metal shores to ',
                       'wprop':'install and remove wooden shores to '
                       },

            'roof':{'install':'install roofing ','erect':'erect roof ',
                       'decra':'decra metal ','metro':'metro romano ',
                       'fiber':'fiber glass shingle ','zinc':'zinc sheet ',
                       'alsheet':'aluminum sheeting ','stseam':'standing seam '
                       },

            'floor':{'install':'install flooring ','lay':'level and lay ',
                        'cer':'ceramic tiles ','porc':'porcelain tiles ',
                        'prk':'pakae tile ','wood':'wooden flooring ',
                        'thset':'thinset mortar ',
                        'grt':'grouted in matching grout ',
                        'plsh':'polish '
                        }
                 }
        return cnote


if __name__ == '__main__':
    pass
