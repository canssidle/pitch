from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Enter the pitch category', validators = [Required()])
    description = TextAreaField('Pitch description')
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    name = TextAreaField('Write your comment here',validators = [Required()])
    submit = SubmitField('Submit')


# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about yourself',validators = [Required()])
#     submit = SubmitField('Submit')
