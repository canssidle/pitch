from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Enter the pitch title', validators = [Required()])
    description = TextAreaField('Pitch description')
    category = SelectField('Pitch Category', choices=[('Sports','Sports'),('Innovative','Innovative'),('Adding a Contact','Adding a Contact'),('Job Opportunity','Job Opportunity'), ('Product Pitch','Product Pitch'),('Promotional Pitch','Promotional Pitch')])
    submit = SubmitField('Add pitch')

class CommentForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Add comment')

    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    title = StringField("Title",validators=[Required()])
    name = TextAreaField('Write your comment here')
    submit = SubmitField('Add comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself',validators = [Required()])
    submit = SubmitField('Submit')
