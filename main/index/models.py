import time 
from main import app, db
'''
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
    nullable=False)
'''
class Beam(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    tag = db.Column(db.String, unique=True)
    wg_tag = db.Column(db.String(10))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('beam', lazy=True))

    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    length = db.Column(db.Float)
    amount = db.Column(db.Integer)

    top_bar_type = db.Column(db.String(20))
    mid_bar_type = db.Column(db.String(20))
    bot_bar_type = db.Column(db.String(20))
    stir_bar_type = db.Column(db.String(20))

    top_bar_amt = db.Column(db.Integer)
    mid_bar_amt = db.Column(db.Integer)
    bot_bar_amt = db.Column(db.Integer)
    stir_spacing = db.Column(db.Float)
    
    timestamp = db.Column(db.String, default=time.ctime())


    def __init__(self,doc_id,tag,wg_tag,width,depth,length,amount,category,top_bar,mid_bar,bot_bar,stirup,stirup_spacing,amt_top,amt_mid,amt_bot):
        
        self.tag=tag
        self.wall_tag=wg_tag
        
        self.width=width
        self.length=length
        self.depth=depth
        self.amount=amount

        self.top_bar_type = top_bar
        self.mid_bar_type = mid_bar
        self.bot_bar_type = bot_bar
        self.stir_bar_type = stirup

        self.top_bar_amt = amt_top
        self.mid_bar_amt = amt_mid
        self.bot_bar_amt = amt_bot
        self.stir_spacing = stirup_spacing

        
       
             
    def __repr__(self):
        return '<Structural Member Beam {}'.format(self.tag)  

class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    tag = db.Column(db.String, unique=True)
    wg_tag = db.Column(db.String(10))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('column', lazy=True))

    width = db.Column(db.Float)
    depth = db.Column(db.Float)
    height = db.Column(db.Float)
    amount = db.Column(db.Integer)

    main_bar_type = db.Column(db.String(20))
    composite_bar_type = db.Column(db.String(20))
    stir_bar_type = db.Column(db.String(20))

    main_bar_amt = db.Column(db.Integer)
    composite_bar_amt = db.Column(db.Integer)
    stir_spacing = db.Column(db.Float)
    
    timestamp = db.Column(db.String, default=time.ctime())


    def __init__(self,doc_id,tag,wg_tag,category,width,depth,height,amount,main_bar,composite_bar,stirup,stirup_spacing,amt_main,amt_composite):
        
        self.tag=tag
        self.wg_tag=wg_tag
        
        self.width=width
        self.depth=depth
        self.height=height
        self.amount=amount

        self.main_bar_type = main_bar
        self.mid_bar_type = composite_bar
        self.stir_bar_type = stirup

        self.main_bar_amt = amt_main
        self.composite_bar_amt = amt_composite
        self.stir_spacing = stirup_spacing      
             
    def __repr__(self):
        return '<Structural Member Column {}'.format(self.tag)      




class Wall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eid = db.Column(db.String, unique=True)
    tag = db.Column(db.String, unique=True)
    length = db.Column(db.Float)
    height = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('wall', lazy=True))

    timestamp = db.Column(db.String, default=time.ctime())

    def __init__(self, tag, length, height, category, eid):
        self.tag = tag
        self.width = length
        self.height = height
      
    def __repr__(self):
        return '<Opening {}'.format(self.tag)

class Opening(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wall_tag = db.Column(db.String(10))
    wall_id = db.Column(db.Integer, db.ForeignKey('wall.id'))
    wall = db.relationship('Wall', backref=db.backref('walls', lazy='dynamic'))
    tag = db.Column(db.String(8))
    width = db.Column(db.Float)
    height = db.Column(db.Float)
    amount = db.Column(db.Float)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('estimates', lazy=True))
    timestamp = db.Column(db.String, default=time.ctime())
    
    
    def __init__(self, tag, wall_tag, width, height, amount, category, uid):
        self.tag = tag
        self.wall_tag = wall_tag
        self.width = width
        self.height = height
        self.amount = amount
        self.category = category

      
    def __repr__(self):
        return '<Opening {}'.format(self.tag)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<Category {}'.format(self.id)  
