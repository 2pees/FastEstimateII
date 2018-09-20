#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:52:10 2018

@author: ian
"""
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
          