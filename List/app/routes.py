from flask import flash
from flask import render_template
from flask import redirect
from app import app
from .forms import *
from .pages import *

from app import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user
from app.forms import LoginForm, RegistrationForm
from flask_login import login_required, logout_user
#from app.models import User
from app import login_manager
from werkzeug.urls import url_parse

class User:
	def __init__(self, username):
		self.username = username

	@staticmethod
	def is_authenticated():
		return True

	@staticmethod
	def is_active():
		return True

	@staticmethod
	def is_anonymous():
		return False

	def get_id(self):
		return self.username

	@staticmethod
	def check_password(password_hash, password):
		return check_password_hash(password_hash, password)

	@login_manager.user_loader
	def load_user(username):
		query = {'username': username}
		mydoc = mycol.find_one(query)
		if mydoc is not None:
			return User(username=mydoc['username'])
		return None

	@login_required
	@app.route('/logout')
	def logout():
		logout_user()
		return redirect("/home")

	@app.route('/login', methods=['GET', 'POST'])
	def login():
		if current_user.is_authenticated:
			return redirect("/home")
		form = LoginForm()
		if form.validate_on_submit():
			username = form.username.data
			password = form.password.data
			#UserObj = User()
			query = {'username': username, 'password': password}
			mydoc = mycol.find(query)
			if 0 == mydoc.count():
				flash('Invalid username or password')
				return redirect(url_for('login'))

			user_obj = User(username = username)
			login_user(user_obj, remember=form.remember_me.data)
			next_page = request.args.get('next')
			if not next_page or url_parse(next_page).netloc != '':
				next_page = "/home"

		return render_template(
			"/login.html", 
			project = project.copy(),
			page = page["login"],
			form = form
		)

@app.route("/")
@app.route("/home")
def home():
	return render_template(
		"home.html",
		project = project.copy(), 
		page = page["home"],
		list = people.get_list(),
		current_user = current_user
	)

@app.route("/person/update/<id>", methods = ["GET", "POST"])
def person_update(id):
	message = ""
	alert = ""
	person = people.get_by_id(id)
	form = UpdateForm()

	if form.validate_on_submit():
		if person:
			alert = "alert-success"
			message = "Element with id {} was edited!".format(id)
		people.update(id, **form.data)
	else:
		form = UpdateForm(**person)

	if people.new_element_added:
		people.new_element_added = False
		alert = "alert-success"
		message = "Element with id {} was added from database!".format(id)

	return render_template(
		"/person/update.html", 
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
	first_person = people.get_first()
	return redirect("/person/update/{}".format(first_person["_id"]))

@app.route("/person/list", methods = ["GET", "POST"])
def person_list():
	return render_template(
		"/person/list.html", 
		project = project.copy(),
		page = page["person_list"],
		list = people.get_list()
	)

@app.route("/person/add", methods = ["GET", "POST"])
def person_add():
	form = AddForm()
	if form.validate_on_submit():
		flash("Add request for element {}".format(
			form.name.data
		))
		id = people.add(**form.data)

		return redirect("/person/update/{}".format(id))

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

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		username = form.username.data
		email = form.email.data
		password = form.password.data
		new_user = {"username": username, "email": email, "password": password}
		#UserObj = User(new_user)
		mycol.insert_one(new_user)
		return redirect(url_for('login'))

	return render_template(
		"/register.html", 
		project = project.copy(),
		page = page["register"],
		form = form
	)