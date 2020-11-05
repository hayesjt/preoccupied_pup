#Packages that are imported 
from flask import (Flask, render_template, request, flash, session, redirect)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash
from model import connect_to_db
import crud

# -------------------------------------- #

"""FORMS"""
# Flask form used to log in
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

# Flask form used to sign up
class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(min=1, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Desired Password', validators=[InputRequired(), Length(min=8, max=80)])

# -------------------------------------- #

"""ROUTES & SERVER"""
#Creating an instance of the flask server along with other instances that are needed for the app
app = Flask("__Name__")
app.config['SECRET_KEY'] = 'ilovedogs'
bootstrap = Bootstrap(app)

# Index page with about information and a link to log in or sign up
@app.route('/')
def index():
    return render_template('index.html')

# Log in page 
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        owner = crud.get_owner_by_email(form.email.data)
        if owner:
            if check_password_hash(owner.password, form.password.data):
                return redirect('/dashboard')

        return '<p>Invalid Email or Password</p>'

    return render_template("login.html", form=form)

# sign up page for owner
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form= RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_owner = crud.create_owner(form.first_name.data, form.last_name.data, form.email.data, hashed_password)
        return ("success, new user added")
        
    return render_template("signup.html", form=form)

# Puppy dashboard page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

#Running the flask app when name = main
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")