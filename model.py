"""Models for Preoccupied Pup App"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""Only one owner per account but owner can have multiple dogs"""
class Owner(db.Model):

    __tablename__ = 'owners'

    email = db.Column(db.String, nullable=False, unique=True, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # dogs = a list of dogs that owner owns

    def __repr__(self):
        return f'<OWNER email={self.email} first_name={self.first_name} last_name={self.last_name}>'


"""Each dog can have one owner and also multiple meals, moods, activities, trainings, groomings, and notes"""
class Dog(db.Model):

    __tablename__ = 'dogs'

    dog_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    owner_email = db.Column(db.String, db.ForeignKey('owners.email'))
    dog_name = db.Column(db.String, nullable=False)
    dog_bio = db.Column(db.String, nullable=False)
    dog_img = db.Column(db.String)
    #meals = list of all meals 
    #moods = list of all moods
    #activities = list of all activities
    #trainings = list of all trainings
    #groomings = list of all groomings
    #notes = list of all notes
    #medications = list of all medications

    owner = db.relationship('Owner', backref='dogs')

    def __repr__(self):
        return f'<DOG dog_id={self.dog_id} dog_name={self.dog_name} dog_img={self.dog_img}>'


"""Each dog can have multiple meals (breakfast, dinner, treat)"""
class Meal(db.Model):

    __tablename__ = "meals"

    meal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    meal_type = db.Column(db.String)
    meal_date = db.Column(db.String)
    meal_month = db.Column(db.String)
    meal_time = db.Column(db.String)

    dog = db.relationship('Dog', backref='meals')

    def __repr__(self):
        return f'<MEAL meal_id={self.meal_id} meal_type={self.meal_type} meal_date={self.meal_date}>'


"""Each Dog can have multiple moods throughout the day that the owner may want to document (sad, happy, sick)"""
class Mood(db.Model):

    __tablename__ = "moods"

    mood_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    mood_type = db.Column(db.String)
    mood_date = db.Column(db.String)
    mood_month = db.Column(db.String)
    mood_note = db.Column(db.Text)

    dog = db.relationship('Dog', backref='moods')

    def __repr__(self):
        return f'<MOOD mood_id={self.mood_id} mood_type={self.mood_type} mood_date={self.mood_date}>'


"""Each Dog can have multiple activities throughout the day that the owner may want to document (park, play date, vet)"""
class Activity(db.Model):

    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    activity_type = db.Column(db.String)
    activity_date = db.Column(db.String)
    activity_month = db.Column(db.String)
    activity_time = db.Column(db.String)
    activity_duration = db.Column(db.Integer)
    activity_note = db.Column(db.Text)

    dog = db.relationship('Dog', backref='activities')

    def __repr__(self):
        return f'<ACTIVITY activity_id={self.activity_id} activity_type={self.activity_type} activity_date={self.activity_date}>'


"""Each Dog can have multiple trainging sessions throughout the day that the owner may want to document (sit, heel, stay)"""
class Training(db.Model):

    __tablename__ = "trainings"

    training_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    training_type = db.Column(db.String)
    training_date = db.Column(db.String)
    training_month = db.Column(db.String)
    training_time = db.Column(db.String)
    training_duration = db.Column(db.Integer)
    training_note = db.Column(db.Text)

    dog = db.relationship('Dog', backref='trainings')

    def __repr__(self):
        return f'<TRAINING training_id={self.training_id} training_type={self.training_type} training_date={self.training_date}>'


"""Each Dog can have multiple grooming sessions throughout the day that the owner may want to document (bath, nails clipped, brushed)"""
class Grooming(db.Model):

    __tablename__ = "groomings"

    grooming_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    grooming_type = db.Column(db.String)
    grooming_date = db.Column(db.String)
    grooming_month = db.Column(db.String)

    dog = db.relationship('Dog', backref='groomings')

    def __repr__(self):
        return f'<GROOMING grooming_id={self.grooming_id} grooming_type={self.grooming_type} grooming_date={self.grooming_date}>'


"""Each Dog can have other things that may to pretain to it in so notes just gives the owner flexability"""
class Note(db.Model):

    __tablename__ = "notes"

    note_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    note_date = db.Column(db.String)
    note = db.Column(db.Text)

    dog = db.relationship('Dog', backref='notes')

    def __repr__(self):
        return f'<NOTE note_id={self.note_id} note_date={self.note_date} note={self.note}>'

"""Each Dog can take medications so owner must track those"""
class Medication(db.Model):

    __tablename__ = "medications"

    med_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.dog_id'))
    med_type = db.Column(db.String)
    med_date = db.Column(db.String)
    med_note = db.Column(db.Text)

    dog = db.relationship('Dog', backref='medications')

    def __repr__(self):
        return f'<MED med_id={self.med_id} med_date={self.med_date} med_note={self.med_note}>'


"""Connecting to db"""
def connect_to_db(flask_app, db_uri='postgresql:///accounts', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Database has been connected')


if __name__ == '__main__':
    from server import app
    connect_to_db(app)