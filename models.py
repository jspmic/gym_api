from init import db


class Sets(db.Model):
    __tablename__ = "Exercise"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sets = db.Column(db.VARCHAR(5), nullable=False, unique=False)


class Exercise(db.Model):
    __tablename__ = "Exercise"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False, unique=False)
    name = db.Column(db.String, nullable=False, unique=False)
