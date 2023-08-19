from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Routine Model
class Routine(db.Model):
    routine_id = db.Column(db.Integer, primary_key=True)
    routine_name = db.Column(db.String(80), nullable=False)

    def __init__(self, routine_name):
        self.routine_name = routine_name


# Exercise Model
class Exercise(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(80), nullable=False)
    # routine_id = db.Column(db.Integer, db.ForeignKey('routine.routine_id'), nullable=False)
    # routine = db.relationship('Routine', backref='exercises', lazy=True)

    def __init__(self, exercise_name):
        self.exercise_name = exercise_name

# Bodyweight Model
class Bodyweight(db.Model):
    bodyweight_id = db.Column(db.Integer, primary_key=True)
    bodyweight = db.Column(db.Integer, nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    # user = db.relationship('User', backref='bodyweight_users', lazy=True)
    post_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, bodyweight, post_date):
        self.bodyweight = bodyweight
        self.post_date = post_date

# User Model
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    user_email = db.Column(db.String(80), nullable=False)
    user_password = db.Column(db.String(80), nullable=False)
    bodyweight = db.relationship('Bodyweight', backref='user', lazy=True)

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password