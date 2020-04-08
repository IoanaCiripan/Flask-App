from flask import flash
from flask import render_template
from flask import redirect
from app import app
from .forms import *
from .pages import *

@app.route("/")
@app.route("/home")
def home():
	return render_template(
		"home.html",
		project = project.copy(), 
		page = page["home"],
		list = people.get_list()
	)

@app.route("/person/update/<id>", methods = ["GET", "POST"])
def person_update(id):
	message = ""
	alert = ""
	form = ViewForm()

	if form.validate_on_submit():
		element = people.update(
			id,
			form.name.data,
			form.description.data
		)
		if element:
			alert = "alert-success"
			message = "Element with id {} was edited!".format(id)
	else:
		element = people.get_by_id(id)

		form.name.data = element["name"]
		form.description.data = element["description"]

	if people.new_element_added:
		people.new_element_added = False
		alert = "alert-success"
		message = "Element with id {} was added from database!".format(id)

	return render_template(
		"person_update.html", 
		project = project.copy(),
		page = page["person_update"],
		list = people.get_list(),
		form = form,
		message = message,
		alert = alert,
		id = id
	)

@app.route("/person/first", methods = ["GET", "POST"])
def person_first():
	return render_template(
		"/person/first.html", 
		project = project.copy(),
		page = page["person_first"],
		list = people.get_list(),
		form = form
	)

@app.route("/person/list", methods = ["GET", "POST"])
def person_list():
	return render_template(
		"/person/list.html", 
		project = project.copy(),
		page = page["person_list"],
		list = people.get_list(),
		form = form
	)

@app.route("/person/add", methods = ["GET", "POST"])
def person_add():
	form = AddForm()
	if form.validate_on_submit():
		flash("Add request for element {}".format(
			form.name.data
		))
		element = people.add(
			form.name.data,
			form.description.data
		)
		people.new_element_added = True

		return redirect("/view/{}".format(element))

	return render_template(
		"/person/add.html", 
		project = project.copy(),
		page = page["person_add"],
		list = people.get_list(),
		form = form
	)

@app.route("/person/delete/<id>", methods = ["GET"])
def person_delete(id):
	message = ""
	alert = ""

	if people.delete_by_id(id):
		alert = "alert-success"
		message = "Element with id {} was deleted from database!".format(id)
	else:
		alert = "alert-warning"
		message = "Element with id {} was not found!".format(id)

	return render_template(
		"/person/delete.html", 
		project = project.copy(),
		page = page["person_delete"],
		list = people.get_list(),
		message = message,
		alert = alert
	)