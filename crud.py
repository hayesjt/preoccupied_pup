"""Create, read, update, and delete operations"""
from model import db, Owner, Dog, Meal, Mood, Activity, Training, Grooming, Note, connect_to_db

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


"""READ/GET FUNCTIONS"""
# Get a user by email address at log in
def get_owner_by_email(email):
    return Owner.query.filter_by(email=email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)