import os
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from dotenv import load_dotenv

load_dotenv()

# Constants section
HOST: str | None = os.getenv("HOST")
DB: str | None = os.getenv("DB")


db = SQLAlchemy()
api = Api()
