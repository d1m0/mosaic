from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, FileField, SelectField
from wtforms.validators import DataRequired, Length, regexp

class UploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    video = StringField('Video File Link', validators=[DataRequired()])
    tags = StringField('Tags', default="")
    relationship = SelectField('Relationship', choices=[('mom', 'erased mom')])
    release = BooleanField('Release', default=False, validators=[DataRequired()])
