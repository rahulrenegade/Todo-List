from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired

class TaskForm(FlaskForm):
    label = TextAreaField('label', validators=[InputRequired()])


