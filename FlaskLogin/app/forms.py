from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app import mycol

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        query = {'username': username.data}
        doc = mycol.find(query)
        if doc.count() != 0:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        query = {'username': email.data}
        doc = mycol.find(query)
        if doc.count() != 0:
            raise ValidationError('Please use a different email address.')