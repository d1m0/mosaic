from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, regexp

class UploadForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    country = StringField('country', validators=[DataRequired()])
    city = StringField('city', validators=[DataRequired()])
    video = StringField('Video File Link', validators=[DataRequired()])
    tags = StringField('tags', default="")
    relationship = SelectField('relationship', choices=[('mom', 'erased mom')])
    release = BooleanField('release', default=False, validators=[DataRequired()])
