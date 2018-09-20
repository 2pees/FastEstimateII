#from flask_wtf.file import FileField, FileAllowed
#from flask_login import current_user

#from music_app.fastestimate.models import Wall
from main import FlaskForm, StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField, DecimalField, SelectField, DataRequired, Length, Email, EqualTo, ValidationError , InputRequired

class NameForm(FlaskForm):
    name = TextField('Name', validators=[InputRequired()], render_kw={'autofocus':True})

class WallEntryForm(FlaskForm):
    tag = TextField('Wall Tag', validators=[InputRequired()], render_kw={'autofocus':True})
    length = DecimalField('Length')
    height = DecimalField('Height')
    v_bar_type = TextField('Vertical BarType')
    h_bar_type = DecimalField('Horizontal BarType')
    v_bar_spacing = DecimalField('Vertical BarSpacing')
    h_bar_spacing = DecimalField('Horizontal BarSpacing')
    #wtype = SelectField('Wall Type')
    category = SelectField('Category', coerce=int)

class OpeningForm(FlaskForm):
    tag = TextField('Opening Tag', validators=[InputRequired()], render_kw={'autofocus':True})
    wall_tag = TextField('Wall Tag', validators=[InputRequired()])
    category = SelectField('Category', coerce=int)
    width = DecimalField('Width')
    height = DecimalField('Height')
    amount = DecimalField('Amount')

class WallBarsForm(FlaskForm):
    v_bar_type = TextField('Vertical BarType')
    h_bar_type = DecimalField('Horizontal BarType')
    v_bar_spacing = DecimalField('Vertical BarSpacing')
    h_bar_spacing = DecimalField('Horizontal BarSpacing')

class BeamCategoryForm(NameForm):
    pass

class CategoryForm(NameForm):
    pass

class ColumnCategoryForm(NameForm):
    pass
class WallCategoryForm(NameForm):
    pass

class BarTypeForm(NameForm):
    pass

class BeamEntryForm(FlaskForm):
    tag = TextField('Beam Tag', validators=[InputRequired()], render_kw={'autofocus':True})
    wall_tag = TextField('Wall Tag')
    category = SelectField('Category', coerce=int)

    width = DecimalField('Width')
    depth = DecimalField('Depth')
    length = DecimalField('Length')
    amount = DecimalField('Amount')  
    top_bar_type = TextField('Top BarType')
    mid_bar_type = TextField('Mid BarType')
    bot_bar_type = TextField('Botton BarType')
    stir_bar_type = TextField('Stirrup BarType')

    top_bar_amt = TextField('Amount TopBar')
    mid_bar_amt = TextField('Amount MidBar')
    bot_bar_amt = TextField('Amount BottomBar')
    stir_spacing = DecimalField('Stirrup Spacing')
        
    