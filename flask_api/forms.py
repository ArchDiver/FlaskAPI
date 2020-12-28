from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email

# class UserForm(FlaskForm):
#     name = StringField('Name', validators = [DataRequired()])
#     email = StringField('Email', validators = [DataRequired(), Email()])
#     password = StringField('Password', validators = [DataRequired()])
#     confirm_password = StringField('Confirm Password', validators = [DataRequired(), EqualTo('Password')])
#     submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()