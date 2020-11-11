from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, PasswordField, TextAreaField, DateField, SelectField, FileField)
from wtforms.validators import (InputRequired, Email, Length)

# -------------------------------------- #

"""FORMS"""

# Flask form used for owner log in
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=80)])

# Flask form used for owner sign up
class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired(), Length(min=1, max=30)])
    last_name = StringField('Last name', validators=[InputRequired(), Length(min=1, max=30)])
    email = StringField('Email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Desired Password', validators=[InputRequired(), Length(min=8, max=80)])

# Flask form used for dog sign up (no log in needed for dog)
class DogSignupForm(FlaskForm):
    dog_name = StringField('Dogs name', validators=[InputRequired(), Length(min=1, max=30)])
    dog_bio = TextAreaField('Dogs Bio', validators=[InputRequired()])
    dog_img = FileField('Dogs Picture')

# Flask form used to add a meal to a dog
class MealForm(FlaskForm):
    meal_type = SelectField('Meal Type', choices=['Breakfast', 'lunch', 'dinner', 'Snack', 'Treat', 'Bone'])

# Flask form used to add a mood to a dog
class MoodForm(FlaskForm):
    mood_type = SelectField('Meal Type', choices=['Happy', 'Sad', 'Anxious', 'Lonely', 'Energetic', 'Aggressive'])
    mood_note = TextAreaField('Notes on Mood')

# Flask form used to add an activity to a dog
class ActivityForm(FlaskForm):
    activity_type = SelectField('Activity Type', choices=['Dog Park', 'Long Walk', 'Short Walk', 'Puppy Play Date', 'Played Ball/Frisbe', 'Run'])
    activity_duration = IntegerField('Duration in Mins')
    activity_note = TextAreaField('Notes on Activity')

# Flask form used to add a training session to a dog
class TrainingForm(FlaskForm):
    training_type = SelectField('Training Type', choices=['Sit', 'Place', 'Lay Down', 'Touch', 'Heel', 'High Five'])
    training_duration = IntegerField('Duration in Mins')
    training_note = TextAreaField('Notes on Training Session')

# Flask form used to add a grooming session to a dog
class GroomingForm(FlaskForm):
    grooming_type = SelectField('Training Type', choices=['Brushed', 'Clipped Nails', 'Bath', 'Hair Cut', 'Teeth Brushed', 'Cleaned Ears'])

# Flask form used for random notes needed to a dog
class NoteForm(FlaskForm):
    note = TextAreaField('Daily Notes')