from flask import request, make_response, json,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config
from flask_restful import Api
from flask import Flask

app= Flask(__name__)
app.config.from_object('config')

db=SQLAlchemy(app)
api=Api(app)
migrate=Migrate(db,app)

# if app.config['DEBUG']:
#     app.debug =True

# UPLOAD_FOLDER='static/files'
# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

import Student_app . routes.routes

@app.before_first_request
def create_table():
    db.create_all()