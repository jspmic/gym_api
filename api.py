from flask import Flask
from init import api
from models import db, Sets, Exercise

app = Flask(__name__)
api.init_app(app)
db.init_app(app)
