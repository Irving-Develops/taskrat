from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired
from app.models import Review

class ReviewForm(FlaskForm):
  rating = SelectField('rating', choices=[ 1, 2, 3, 4, 5], validators=[DataRequired()])
  comment = StringField('comment', validators=[DataRequired()])
