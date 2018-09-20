#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:53:36 2018

@author: ian

Bar No. Bar Size in Inches Diameter in Inches Weight per Ft. in Lbs.
"""
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
                
   
                

