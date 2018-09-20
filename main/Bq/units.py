#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from gluon import *

class UnitsLog:
    ''' A measurement units catalog  of
        units abreviation.
        '''
    def __init__(self):
        self.unit='units'

    def unit_log(self):
        ''' returns a dictionary mapping abreviated keywords to a string represntation
        '''
        abrev={'sqyd':'sqyd',
               	'sqft':'sqft',
               	'cuft':'cuft',
                'cuyd':'cuyd',
                'ea':'each',
               'lgth':'length',
               'm':'meter',
               'sm':'sqr meter',
               'cum':'cu meter',
               'g':'gram',
               'kg':'kilogram',
               'lb':'pound',
               'tn':'ton',
               'yd':'yard',
               'ft':'feet'
               }
        return abrev


