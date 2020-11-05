"""Create, read, update, and delete operations"""
from model import db, Owner, Dog, Meal, Mood, Activity, Training, Grooming, Note, connect_to_db

"""CREATE FUNCTIONS"""
# Create a new owner
def create_owner(first_name, last_name, email, password):
    owner = Owner(first_name=first_name, last_name=last_name, email=email, password=password)
    db.session.add(owner)
    db.session.commit()
    return owner


"""GET FUNCTIONS"""
# Get a user by email address at log in
def get_owner_by_email(email):
    return Owner.query.filter_by(email=email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)