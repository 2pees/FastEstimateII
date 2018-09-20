# System Resources
import os
import requests
from dateutil.parser import parse
from datetime import date
from json import dumps, loads
from strgen import StringGenerator
from random import sample

# Server Resources 
from flask import Flask, request, jsonify, Blueprint, flash, redirect,url_for, render_template, abort

from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
#from flask_wtf.file import FileField, FileAllowed
#from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, TextField, DecimalField, SelectField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired



def uu_id(doc_tag):
    """ 
    Doc Tags: String( doc, app, key, job, user, item)
    """
    tags = dict(
        doc='[h-z5-9]{8:16}',
        app='[a-z0-9]{16:32}',
        key='[a-z0-9]{32:32}',
        job='[a-j0-7]{8:8}',
        user='[0-9]{4:6}',
        item='[a-n1-9]{8:8}'
        )
    if doc_tag == 'user':
        u_id =  StringGenerator(str(tags[doc_tag])).render(unique=True)
        u_id = 'U{}'.format(u_id)
    else:
        u_id =  StringGenerator(str(tags[doc_tag])).render(unique=True)
    return u_id




ROOT_DIR = os.path.dirname(os.path.abspath(__file__))



# creates a Flask application, named app
app = Flask(__name__)

# Configure the app
app.config['SECRET_KEY'] = uu_id('app')
app.config['WTF_CSRF_SECRET_KEY'] =  uu_id('key')
app.config['MAX_CONTENT_LENGTH'] = 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/fastDB.db'

# Create the Database Handle
db = SQLAlchemy(app)

CSRFProtect(app)
# Create the Api
api = Api(app)



# Import Application Blueprint
# Main Index
from main.index.views import index
from main.index import qsrep
# FastEstimate

from main.Bq.routes import fastestimate
from main.Bq import estimator


# Register the Blueprints
app.register_blueprint(index)
app.register_blueprint(fastestimate)

# Manage the Database
# Clear the database --- run once 
#db.drop_all()
# Create all tables 
db.create_all()


