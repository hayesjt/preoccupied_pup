#Packages that are imported 

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

#Creating an instance of the flask server
app = Flask("__Name__")

#Main route for handling home log in/create page
@app.route("/")
def login():

    return render_template("login.html")

#Running the flask app when name = main
if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")