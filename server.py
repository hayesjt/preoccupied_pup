#Packages that are imported 
from flask import (Flask, render_template, session, redirect, jsonify)
from flask_bootstrap import Bootstrap
from datetime import (date, datetime)
from form import (LoginForm, SignupForm, DogSignupForm, MealForm, MoodForm, ActivityForm, TrainingForm, GroomingForm, NoteForm, MedForm)
from flask_uploads import (configure_uploads, IMAGES, UploadSet)
from werkzeug.security import (generate_password_hash, check_password_hash)
from model import connect_to_db
import pytz
import crud

# -------------------------------------- #

"""ROUTES & SERVER"""

# Creating an instance of the flask server along with other instances that are needed for the app
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ilovedogs'

# Configuring a folder for images
app.config['UPLOADS_DEFAULT_DEST'] = 'static/imgs/user_uploads'
images = UploadSet('images', IMAGES)
configure_uploads(app, (images,))

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
                owners_dog = crud.get_dog_by_owner(session['owner_email'])
                session['owner_email'] = owner.email
                session['dog_id'] = owners_dog.dog_id
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
        new_dog = crud.create_dog(owner_email, form.dog_name.data, form.dog_bio.data, form.dog_img.data.filename)
        image_save = images.save(form.dog_img.data)
        session['dog_id'] = new_dog.dog_id
        return redirect('/dashboard')

    return render_template("pupsignup.html", form=form)

# Puppy dashboard page
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    # Create variables for all forms
    meal_form = MealForm()
    mood_form = MoodForm()
    activity_form = ActivityForm()
    training_form = TrainingForm()
    grooming_form = GroomingForm()
    note_form = NoteForm()
    med_form = MedForm()

    # Variables for dog_id, current date, and current time
    dog_id = session['dog_id']

    # Current date and Month to use for filtering Database
    current_date = date.today().strftime("%m/%d/%y")
    current_month = date.today().strftime("%m")

    # Not Ideal but datetime does not offer taking time directly from device being used
    central_time = pytz.timezone('America/Chicago')
    current_time = datetime.now(central_time).strftime("%I:%M")

    # Getting all data to render on dashboard
    dog_info = crud.get_dog_by_dog_id(dog_id)
    all_meals = crud.get_all_meals(dog_id, current_date)
    all_moods = crud.get_all_moods(dog_id, current_date)
    all_activities = crud.get_all_activities(dog_id, current_date)
    all_trainings = crud.get_all_training_sessions(dog_id, current_date)
    all_groomings = crud.get_all_grooming_sessions(dog_id, current_date)
    all_notes = crud.get_all_notes(dog_id, current_date)
    all_meds = crud.get_all_meds(dog_id, current_month)

    # Creating a new meal from form
    if meal_form.validate_on_submit():
        new_meal = crud.create_meal(dog_id, meal_form.meal_type.data, current_date, current_month, current_time)
        return redirect('/dashboard')

    # Creating a new mood from form
    if mood_form.validate_on_submit():
        new_mood = crud.create_mood(dog_id, mood_form.mood_type.data, current_date, current_month, mood_form.mood_note.data)
        return redirect('/dashboard')

    # Creating a new activity from form
    if activity_form.validate_on_submit():
        new_activity = crud.create_activity(dog_id, activity_form.activity_type.data, current_date, current_month, current_time, activity_form.activity_duration.data, activity_form.activity_note.data)
        return redirect('/dashboard')

    # Creating a new training session from form
    if training_form.validate_on_submit():
        new_training = crud.create_training(dog_id, training_form.training_type.data, current_date, current_month, current_time, training_form.training_duration.data, training_form.training_note.data)
        return redirect('/dashboard')

    # Creating a new grooming session from form
    if grooming_form.validate_on_submit():
        new_grooming = crud.create_grooming(dog_id, grooming_form.grooming_type.data, current_date, current_month)
        return redirect('/dashboard')

    # Creating a new note from form
    if note_form.validate_on_submit():
        new_note = crud.create_note(dog_id, current_date, note_form.note.data)
        return redirect('/dashboard')
    
    # Create a new medication from form
    if med_form.validate_on_submit():
        new_med = crud.create_med(dog_id, med_form.med_type.data , current_month, med_form.med_note.data )
        return redirect('/dashboard')


    return render_template("dashboard.html", meal_form=meal_form, mood_form=mood_form, activity_form=activity_form, training_form=training_form, grooming_form=grooming_form, note_form=note_form, med_form=med_form, all_meals=all_meals, all_moods=all_moods, all_activities=all_activities, all_trainings=all_trainings, all_groomings=all_groomings, all_notes=all_notes, all_meds=all_meds, dog_info=dog_info)

# Data for Meal Chart
@app.route("/mealdata")
def mealdata():

    dog_id = session['dog_id']
    current_month = date.today().strftime("%m")
    meal_amounts = crud.get_month_meals(dog_id, current_month)

    return jsonify(meal_amounts) 

# Data for Mood Chart
@app.route("/mooddata")
def mooddata():

    dog_id = session['dog_id']
    current_month = date.today().strftime("%m")
    mood_amounts = crud.get_month_moods(dog_id, current_month)

    return jsonify(mood_amounts)

# Data for Grooming Chart
@app.route("/groomdata")
def groomdata():

    dog_id = session['dog_id']
    current_month = date.today().strftime("%m")
    groom_amounts = crud.get_month_grooms(dog_id, current_month)

    return jsonify(groom_amounts)  

# Data for Training Chart
@app.route("/trainingdata")
def trainingdata():

    dog_id = session['dog_id']
    current_month = date.today().strftime("%m")
    training_amounts = crud.get_month_training(dog_id, current_month)

    return jsonify(training_amounts) 

# Data for Activity Chart
@app.route("/activitydata")
def activitydata():

    dog_id = session['dog_id']
    current_month = date.today().strftime("%m")
    activity_amounts = crud.get_month_activity(dog_id, current_month)

    return jsonify(activity_amounts) 
    

#Running the flask app when name = main
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")