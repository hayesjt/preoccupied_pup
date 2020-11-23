"""Create, read, update, and delete operations"""

# importing tables for database 
from model import (db, Owner, Dog, Meal, Mood, Activity, Training, Grooming, Note, Medication, connect_to_db)

# -------------------------------------- #

"""CREATE FUNCTIONS"""

# Create a new owner
def create_owner(email,first_name, last_name, password):
    owner = Owner(email=email, first_name=first_name, last_name=last_name, password=password)
    db.session.add(owner)
    db.session.commit()
    return owner

# Create a new dog
def create_dog(owner_email, dog_name, dog_bio, dog_img):
    dog = Dog(owner_email=owner_email, dog_name=dog_name, dog_bio=dog_bio, dog_img=dog_img)
    db.session.add(dog)
    db.session.commit()
    return dog

# Create a new meal
def create_meal(dog_id, meal_type, meal_date, meal_month, meal_time):
    meal = Meal(dog_id=dog_id, meal_type=meal_type, meal_date=meal_date, meal_month=meal_month, meal_time=meal_time)
    db.session.add(meal)
    db.session.commit()
    return meal

# Create a new mood
def create_mood(dog_id, mood_type, mood_date, mood_month, mood_note):
    mood = Mood(dog_id=dog_id, mood_type=mood_type, mood_date=mood_date, mood_month=mood_month, mood_note=mood_note)
    db.session.add(mood)
    db.session.commit()
    return mood

# Create new activity
def create_activity(dog_id, activity_type, activity_date, activity_month, activity_time, activity_duration, activity_note):
    activity = Activity(dog_id=dog_id,activity_type=activity_type, activity_date=activity_date, activity_month=activity_month, activity_time=activity_time, activity_duration=activity_duration, activity_note=activity_note)
    db.session.add(activity)
    db.session.commit()
    return activity

# Create new training
def create_training(dog_id, training_type, training_date, training_month, training_time, training_duration, training_note):
    training = Training(dog_id=dog_id, training_type=training_type, training_date=training_date, training_month=training_month, training_time=training_time, training_duration=training_duration, training_note=training_note)
    db.session.add(training)
    db.session.commit()
    return training

# Create new grooming
def create_grooming(dog_id, grooming_type, grooming_date, grooming_month):
    grooming = Grooming(dog_id=dog_id, grooming_type=grooming_type, grooming_date=grooming_date, grooming_month=grooming_month)
    db.session.add(grooming)
    db.session.commit()
    return grooming

# Create new note
def create_note(dog_id, note_date, note):
    note = Note(dog_id=dog_id, note_date=note_date, note=note)
    db.session.add(note)
    db.session.commit()
    return note

def create_med(dog_id, med_type, med_date, med_note):
    med = Medication(dog_id=dog_id, med_type=med_type, med_date=med_date, med_note=med_note)
    db.session.add(med)
    db.session.commit()
    return med

# -------------------------------------- #

"""READ/GET FUNCTIONS"""

# Get an owner by email address at log in
def get_owner_by_email(email):
    return Owner.query.filter_by(email=email).first()

# Get a dog by owner id
def get_dog_by_owner(owner_email):
    return Dog.query.filter_by(owner_email=owner_email).first()

# Get a dog by dog_id
def get_dog_by_dog_id(dog_id):
    return Dog.query.filter_by(dog_id=dog_id).first()

# Get all meals by date and dog_id
def get_all_meals(dog_id, date):
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_date == date))

# Get all moods by date and dog_id
def get_all_moods(dog_id, date):
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_date == date))

# Get all activities date and dog_id
def get_all_activities(dog_id, date):
    return Activity.query.filter((Activity.dog_id == dog_id) & (Activity.activity_date == date))

# Get all training sessions by date and dog_id
def get_all_training_sessions(dog_id, date):
    return Training.query.filter((Training.dog_id == dog_id) & (Training.training_date == date))

# Get all grooming sessions by date and dog_id
def get_all_grooming_sessions(dog_id, date):
    return Grooming.query.filter((Grooming.dog_id == dog_id) & (Grooming.grooming_date == date))

# Get all notes by date and dog_id
def get_all_notes(dog_id, date):
    return Note.query.filter((Note.dog_id == dog_id) & (Note.note_date == date))

# Get all meds by month and dog_id
def get_all_meds(dog_id, month):
    return Medication.query.filter((Medication.dog_id == dog_id) & (Medication.med_date == month))

# GET METHODS FOR CHART DATA 

# MEAL DATA
def get_month_breakfasts(dog_id, month):
    # meals where type=breakfast
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Breakfast") & (Meal.meal_month == month)).count()

def get_month_lunchs(dog_id, month):
    # meals where type=lunch
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Lunch") & (Meal.meal_month == month)).count()

def get_month_dinners(dog_id, month):
    # meals where type=dinner
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Dinner") & (Meal.meal_month == month)).count()

def get_month_snacks(dog_id, month):
    # meals where type=snack
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Snack") & (Meal.meal_month == month)).count()

def get_month_treats(dog_id, month):
    # meals where type=treat
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Treat") & (Meal.meal_month == month)).count()

def get_month_bones(dog_id, month):
    # meals where type=bone
    return Meal.query.filter((Meal.dog_id == dog_id) & (Meal.meal_type == "Bone") & (Meal.meal_month == month)).count()

# MOOD DATA
def get_month_happy(dog_id, month):
    # moods where type=happy
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Happy") & (Mood.mood_month == month)).count()

def get_month_sad(dog_id, month):
    # moods where type=sad
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Sad") & (Mood.mood_month == month)).count()

def get_month_anxious(dog_id, month):
    # moods where type=anxious
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Anxious") & (Mood.mood_month == month)).count()

def get_month_lonely(dog_id, month):
    # moods where type=lonely
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Lonely") & (Mood.mood_month == month)).count()

def get_month_energetic(dog_id, month):
    # moods where type=energetic
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Energetic") & (Mood.mood_month == month)).count()

def get_month_aggressive(dog_id, month):
    # moods where type=aggressive
    return Mood.query.filter((Mood.dog_id == dog_id) & (Mood.mood_type == "Aggressive") & (Mood.mood_month == month)).count()


# -------------------------------------- #

"""CONNECTING TO SERVER AND CREATING TABLES"""

if __name__ == '__main__':
    from server import app
    connect_to_db(app)