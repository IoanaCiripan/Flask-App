from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateTimeField
from wtforms import BooleanField
from wtforms import SelectField
from wtforms import StringField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms import SubmitField
from .collection import *
from .validators import *

class LoginForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[DataRequired()],
		render_kw = {"class": "form-control"}
	)
	password = PasswordField(
		'Password',
		validators=[DataRequired()],
		render_kw = {"class": "form-control"}
	)
	remember_me = BooleanField(
		'Remember Me'
	)
	submit = SubmitField(
		'Login',
		render_kw = {"class": "btn btn-primary"}
	)

	def validate_username(self, username):
		query = {'username': username.data}
		doc = mycol.find(query)
		if doc.count() == 0:
			raise ValidationError('Invalid username or password')

	def validate_password(self, password):
		query = {'password': password.data}
		doc = mycol.find(query)
		if doc.count() == 0:
			raise ValidationError('Invalid username or password')

class RegistrationForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[DataRequired()],
		render_kw = {"class": "form-control"})
	email = StringField(
		'Email',
		validators=[DataRequired(),
		Email()],
		render_kw = {"class": "form-control"})
	password = PasswordField(
		'Password',
		validators=[DataRequired()],
		render_kw = {"class": "form-control"})
	password2 = PasswordField(
		'Repeat Password',
		validators=[DataRequired(),
		EqualTo('password')],
		render_kw = {"class": "form-control"}
	)
	submit = SubmitField(
		'Register',
		render_kw = {"class": "btn btn-primary"}
	)

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

class PersonForm(FlaskForm):
	name = StringField(
		"Name",
		validators = [
			DataRequired(),
			Length(min = name_min_len, max = name_max_len)
		],
		render_kw = {"class": "form-control"}
	)

	first_name = StringField(
		"First name",
		validators = [
			DataRequired(),
			Length(min = name_min_len, max = name_max_len)
		],
		render_kw = {"class": "form-control"}
	)

	cnp = StringField(
		"CNP",
		validators = [
			DataRequired(),
			validate_cnp
		],
		render_kw = {"class": "form-control"}
	)

	ci_number = StringField(
		"Number",
		validators = [
			DataRequired(),
			validate_ci_number
		],
		render_kw = {"class": "form-control"}
	)

	ci_seria = StringField(
		"Seria",
		validators = [
			DataRequired(),
			validate_ci_seria
		],
		render_kw = {"class": "form-control"}
	)

	birthdate = StringField(
		"Birthdate",
		validators = [
			DataRequired()
		],
		render_kw = {"class": "form-control"}
	)

	gender = SelectField(
		"Gender",
		choices = genders,
		validators = [
			DataRequired()
		],
		render_kw = {"class": "form-control"}
	)

	service_supplier = StringField(
		"Service supplier",
		validators = [
			DataRequired(),
			Length(min = name_min_len, max = name_max_len)
		],
		render_kw = {"class": "form-control"}
	)

	medical_subscription = StringField(
		"Medical subscription",
		validators = [
			Length(max = name_max_len)
		],
		render_kw = {"class": "form-control"}
	)

	medical_history = TextAreaField(
		"Medical history",
		[
			Length(
				min = description_min_len,
				max = description_max_len
			)
		],
		render_kw = {"class": "form-control"}
	)

	observation = StringField(
		"Observation",
		validators = [
			Length(min = description_min_len, max = name_max_len)
		],
		render_kw = {"class": "form-control"}
	)

class AddForm(PersonForm):
	submit = SubmitField(
		"Add person",
		render_kw = {"class": "btn btn-primary"}
	)

class UpdateForm(PersonForm):
	submit = SubmitField(
		"Edit",
		render_kw = {"class": "btn btn-primary"}
	)