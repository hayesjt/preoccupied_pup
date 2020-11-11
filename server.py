#Packages that are imported 
from flask import (Flask, render_template, request, flash, session, redirect)
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, PasswordField, TextAreaField, DateField, SelectField, FileField)
from wtforms.validators import (InputRequired, Email, Length)
from werkzeug.security import (generate_password_hash, check_password_hash)
from model import connect_to_db
import crud
from form import (LoginForm, SignupForm, DogSignupForm, MealForm, MoodForm, ActivityForm, TrainingForm, GroomingForm, NoteForm)

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
                session['owner_email'] = owner.email
                return redirect('/dashboard')

        return '<p>Invalid Email or Password</p>'

    return render_template("login.html", form=form)

# sign up page for owner
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form= SignupForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_owner = crud.create_owner(form.email.data, form.first_name.data, form.last_name.data, hashed_password)
        session['owner_email'] = new_owner.email
        return redirect('/pupsignup')
        
    return render_template("signup.html", form=form)

# Puppy sign up form
@app.route("/pupsignup", methods=['GET', 'POST'])
def pupsignup():

    form= DogSignupForm()

    if form.validate_on_submit():
        owner_email = session['owner_email']
        new_dog = crud.create_dog(owner_email, form.dog_name.data, form.dog_bio.data, form.dog_img.data)
        session['dog_id'] = new_dog.dog_id
        return redirect('/dashboard')

    return render_template("pupsignup.html", form=form)

# Puppy dashboard page
@app.route("/dashboard")
def dashboard():
    meal_form = MealForm()
    mood_form = MoodForm()
    activity_form = ActivityForm()
    training_form = TrainingForm()
    grooming_form = GroomingForm()
    note_form = NoteForm()

    return render_template("dashboard.html", meal_form=meal_form, mood_form=mood_form, activity_form=activity_form, training_form=training_form, grooming_form=grooming_form, note_form=note_form)

#Running the flask app when name = main
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")