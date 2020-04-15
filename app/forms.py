from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

#class for adding a profile
class AddProfile(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[("Male", "Male"), ("Female", "Famale")])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    bio = StringField('Biography', validators=[DataRequired()])
    photo = FileField('Profile Picture',validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images Only')])