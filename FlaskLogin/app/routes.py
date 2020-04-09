from app import app
from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user
from app.forms import LoginForm, RegistrationForm
from app import mycol
from flask_login import login_required, logout_user, login_user
#from app.models import User
from app import login_manager
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required
def index():
    #user = {'username': 'aa'}
    return render_template('index.html', title='Home', current_user=current_user)

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        #UserObj = User()
        query = {'username': username, 'password': password}
        mydoc = mycol.find(query)
        print(mydoc)
        if mydoc.count() == 0:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(current_user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


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
    return  render_template('register.html', title='Sign Up', form=form)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@login_manager.user_loader
def load_user(id):
    query = {'id': id}
    mydoc = mycol.find_one(query)
    if mydoc is not None:
        return mydoc['_id']
    return None

