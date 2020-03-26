from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

HUNTERTYPES = [('noob','-Choose Hunter-'),('chosen','Chosen'), ('crooked','Crooked'), ('divine','Divine'), ('expert','Expert')]
GENDERS = ['Male', 'Female', 'Other']

class ccform(FlaskForm):
    character_name = StringField('Character Name', validators=[DataRequired()])
    cunter_type = SelectField('Hunter Type', choices = HUNTERTYPES)
    submit = SubmitField('Play God and Create')
