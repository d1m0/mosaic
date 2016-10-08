from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, regexp

class UploadForm(FlaskForm):
    video = FileField(u'Video File', validators=[regexp(u'^[^\/\\\\]*\.(mov|mp4|avi|mpg|mpeg)$'), DataRequired()])
    tags = StringField('tags', default="")
    location = StringField('location', default="")
    release = BooleanField('release', default=False)
