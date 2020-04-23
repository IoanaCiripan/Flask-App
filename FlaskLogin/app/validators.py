from wtforms.validators import ValidationError
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email, EqualTo, ValidationError

name_min_len = 1
name_max_len = 25

description_min_len = 0
description_max_len = 300

date_time_format = '%d/%m/%y'

genders = [
	("M", "Male"),
	("F", "Female")
]

cnp_len = 13
ci_number_len = 6
ci_seria_len = 2

def validate_cnp(form, field):
	if field.data.isdigit():
		if cnp_len != len(field.data):
			raise ValidationError("CNP-ul must has 13 caracters!")
		if field.data.startswith("0"):
			raise ValidationError("CNP-ul can't begin with 0.")
	else:
		raise ValidationError("The CNP must contains only digits!")

def validate_ci_seria(form, field):
	if ci_seria_len == len(field.data):
		if field.data.isalpha():
			if field.data.isupper():
				return True
			return ValidationError("The seria must contains only {} letters in uppercase!".format(ci_seria_len))
		else:
			raise ValidationError("The seria must contains only {} letters in uppercase!".format(ci_seria_len))
	else:
		raise ValidationError("The seria must contains only {} letters in uppercase!".format(ci_seria_len))

def validate_ci_number(form, field):
	if ci_number_len == len(field.data):
		if field.data.isdigit():
			return True
		else:
			raise ValidationError("The number must contains only {} digits!".format(ci_number_len))
	else:
		raise ValidationError("The number must contains only {} digits!".format(ci_number_len))