from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Routine Model
class Routine(db.Model):
    routine_id = db.Column(db.Integer, primary_key=True)
    routine_name = db.Column(db.String(80), nullable=False)

    def __init__(self, routine_name):
        self.routine_name = routine_name

    def __repr__(self):
        return f'{self.routine_name} routine created with ID {self.routine_id}'


# Exercise Model
class Exercise(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(80), nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    speed = db.Column(db.Integer, nullable=True)
    distance = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)
    # routine_id = db.Column(db.Integer, db.ForeignKey('routine.routine_id'), nullable=False)
    # routine = db.relationship('Routine', backref='exercises', lazy=True)

    def __init__(self, exercise_name):
        self.exercise_name = exercise_name

# Routine/Exercise Model
class RoutineExercise(db.Model):
    routine_exercise_id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.routine_id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), nullable=False)
    routine = db.relationship('Routine', backref='routine_exercises', lazy=True)
    exercise = db.relationship('Exercise', backref='routine_exercises', lazy=True)

    def __init__(self, routine_id, exercise_id):
        self.routine_id = routine_id
        self.exercise_id = exercise_id

# Bodyweight Model
class Bodyweight(db.Model):
    bodyweight_id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    user = db.relationship('User', backref='bodyweight_users', lazy=True)

    def __init__(self, weight, date):
        self.weight = weight
        self.date = date

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