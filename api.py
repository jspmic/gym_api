from flask import Flask
from flask_migrate import Migrate
from init import api, DB
from models import db, Sets, Exercise

app = Flask(__name__)

# app configuration
app.config["SQLALCHEMY_DATABASE_URI"] = DB

api.init_app(app)
db.init_app(app)
Migrate(app=app, db=db)
