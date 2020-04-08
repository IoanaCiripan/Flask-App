from app import app
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user
from app.forms import LoginForm, RegistrationForm
from app import mycol
from flask_login import login_required
#from app.models import User





@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'aa'}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET','POST'])
def login():
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
        return render_template('index.html', current_user=username)
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
        return render_template('index.html', current_user=username)
    return  render_template('register.html', title='Sign Up', form=form)



