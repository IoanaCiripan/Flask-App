from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length

name_min_len = 1
name_max_len = 20

description_min_len = 5
description_max_len = 200

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
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

    ci_number = StringField(
        "Number",
        validators = [
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

    ci_seria = StringField(
        "Seria", 
        validators = [
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

    birthdate = StringField(
        "Birthdate", 
        validators = [
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

    gender = StringField(
        "Gender", 
        validators = [
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
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

    medicalSubscription = StringField(
        "Medical subscription", 
        validators = [
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

    medical_history = TextAreaField(
        "Medical history", 
        [
            DataRequired(), 
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
            DataRequired(), 
            Length(min = name_min_len, max = name_max_len)
        ],
        render_kw = {"class": "form-control"}
    )

class AddForm(PersonForm):
    submit = SubmitField(
        "Add person",
        render_kw = {"class": "btn btn-primary"}
    )

class ViewForm(PersonForm):
    submit = SubmitField(
    	"Edit",
    	render_kw = {"class": "btn btn-primary"}
    )