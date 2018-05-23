from flask_wtf import FlaskForm #import FlaskForm class from the module
from wtforms import StringField, TextAreaField, SubmitField #import these to help in creation of a text area field and submit button.
from wtforms.validators import Required #import required that will prevent submission if an input field is empty


class PitchForm(FlaskForm): #create a class that inherits from FlaskForm class
    name = StringField('Authors Name', validators = [Required()])
    category = StringField('Pitch Category', validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField('Submit')