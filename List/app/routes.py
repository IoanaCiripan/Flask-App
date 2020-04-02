from flask import flash
from flask import render_template
from flask import redirect
from app import app
from .collection import *
from .forms import *
from .pages import *

@app.route("/")
@app.route("/home")
def home():
	return render_template(
		"home.html",
		project = project.copy(), 
		page = page["home"],
		list = collection.get_list()
	)

@app.route("/view/<id>", methods = ["GET", "POST"])
def view(id):
	message = ""
	alert = ""
	form = ViewForm()

	if form.validate_on_submit():
		element = collection.update(
			id,
			form.name.data,
			form.description.data
		)
		if element:
			alert = "alert-success"
			message = "Element with id {} was edited!".format(id)
	else:
		element = collection.get_by_id(id)

		form.name.data = element["name"]
		form.description.data = element["description"]

	if collection.new_element_added:
		collection.new_element_added = False
		alert = "alert-success"
		message = "Element with id {} was added from database!".format(id)

	return render_template(
		"view.html", 
		project = project.copy(),
		page = page["view"],
		list = collection.get_list(),
		form = form,
		message = message,
		alert = alert,
		id = id
	)

@app.route("/add", methods = ["GET", "POST"])
def add():
	form = AddForm()
	if form.validate_on_submit():
		flash("Add request for element {}".format(
			form.name.data
		))
		element = collection.add(
			form.name.data,
			form.description.data
		)
		collection.new_element_added = True

		return redirect("/view/{}".format(element))

	return render_template(
		"add.html", 
		project = project.copy(),
		page = page["add"],
		list = collection.get_list(),
		form = form
	)

@app.route("/delete/<id>", methods = ["GET"])
def delete(id):
	message = ""
	alert = ""

	if collection.delete_by_id(id):
		alert = "alert-success"
		message = "Element with id {} was deleted from database!".format(id)
	else:
		alert = "alert-warning"
		message = "Element with id {} was not found!".format(id)


	return render_template(
		"delete.html", 
		project = project.copy(),
		page = page["delete"],
		list = collection.get_list(),
		message = message,
		alert = alert
	)