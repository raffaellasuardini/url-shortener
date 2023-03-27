from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import URL, DataRequired

class InsertUrl(FlaskForm):
    url = URLField( validators=[DataRequired(message='The URL is required'), URL()], render_kw={"placeholder": "Insert url to short it!"})
