import os
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from dotenv import load_dotenv

load_dotenv()

# Constants section
HOST = os.getenv("HOST")
DB = os.getenv("DB")


db = SQLAlchemy()
api = Api()
