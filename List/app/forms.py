from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length

name_min_len = 3
name_max_len = 25

description_min_len = 5
description_max_len = 200

class AddForm(FlaskForm):
    name = StringField(
    	"Name", 
    	validators = [
    		DataRequired(), 
    		Length(min = name_min_len, max = name_max_len)
    	],
    	render_kw = {"class": "form-control"}
    )
    description = TextAreaField(
    	"Description", 
    	[
    		DataRequired(), 
	    	Length(
	    		min = description_min_len, 
	    		max = description_max_len
	    	)
	    ],
    	render_kw = {"class": "form-control"}
    )
    submit = SubmitField(
    	"Add",
    	render_kw = {"class": "btn btn-primary"}
    )

class ViewForm(FlaskForm):
    name = StringField(
    	"Name", 
    	validators = [
    		DataRequired(), 
    		Length(min = name_min_len, max = name_max_len)
    	],
    	render_kw = {"class": "form-control"}
    )
    description = TextAreaField(
    	"Description", 
    	validators = [
    		DataRequired(), 
	    	Length(
	    		min = description_min_len, 
	    		max = description_max_len
	    	)
	    ],
    	render_kw = {"class": "form-control"}
    )
    submit = SubmitField(
    	"Edit",
    	render_kw = {"class": "btn btn-primary"}
    )