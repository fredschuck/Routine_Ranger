from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Routine Model
class Routine(db.Model):
    '''This class contains methods for interacting with the Routine model'''
    routine_id = db.Column(db.Integer, primary_key=True)
    routine_name = db.Column(db.String(80), nullable=False)

    def __init__(self, routine_name):
        self.routine_name = routine_name

    def __repr__(self):
        return f'Routing: {self.routine_name}. ID: {self.routine_id}'

# Exercise Model
class Exercise(db.Model):
    '''This class contains methods for interacting with the Exercise model'''
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_name = db.Column(db.String(80), nullable=False)

    def __init__(self, exercise_name):
        self.exercise_name = exercise_name

    def __repr__(self):
        return f'Exercise: {self.exercise_name}. ID: {self.exercise_id}'

# Exercise Model
class ExerciseAttributes(db.Model):
    '''This class contains methods for interacting with the ExerciseAttributes model'''
    exercise_attributes_id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), nullable=False)
    exercise = db.relationship('Exercise', backref='exercise_attributes', lazy=True)
    sets = db.Column(db.Boolean, nullable=False)
    reps = db.Column(db.Boolean, nullable=False)
    weight = db.Column(db.Boolean, nullable=False)
    height = db.Column(db.Boolean, nullable=False)
    speed = db.Column(db.Boolean, nullable=False)
    distance = db.Column(db.Boolean, nullable=False)
    time = db.Column(db.Boolean, nullable=False)

    def __init__(self, exercise_id, sets, reps, weight, height, speed, distance, time):
        self.exercise_id = exercise_id
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.height = height
        self.speed = speed
        self.distance = distance
        self.time = time
    
    def __repr__(self):
        return f'{self.exercise.exercise_name}. Sets: {self.sets}. Reps: {self.reps}. Weight: {self.weight}. Height: {self.height}. Speed: {self.speed}. Distance: {self.distance}. Time: {self.time}'

# LoggedExercise Model
class LoggedExercises(db.Model):
    '''This class contains methods for interacting with the LoggedExercises model'''
    log_id = db.Column()
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), nullable=False)
    exercise = db.relationship('Exercise', backref='log_exercise', lazy=True)
    # routine_id = db.Column(db.Integer, db.ForeignKey('routine.routine_id'), nullable=True)
    # routine = db.relationship('Routine', backref='log_routine', lazy=True)
    log_date = db.Column(db.DateTime, nullable=False)
    log_time = db.Column(db.DateTime, nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    speed = db.Column(db.Integer, nullable=True)
    distance = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)

    def __init__(self, exercise_id, log_date, log_time, sets, reps, weight, height, speed, distance, time):
        self.exercise_id = exercise_id
        self.log_date = log_date
        self.log_time = log_time
        self.sets = sets
        self.reps = reps
        self.weight = weight
        self.height = height
        self.speed = speed
        self.distance = distance
        self.time = time

    def __repr__(self):
        return f'Exercise ID: {self.exercise_id}. Sets: {self.sets}. Reps: {self.reps}. Weight: {self.weight}. Height: {self.height}. Speed: {self.speed}. Distance: {self.distance}. Time: {self.time}'



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

# # Bodyweight Model
# class Bodyweight(db.Model):
#     bodyweight_id = db.Column(db.Integer, primary_key=True)
#     weight = db.Column(db.Integer, nullable=False)
#     date = db.Column(db.DateTime, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
#     user = db.relationship('User', backref='bodyweight_users', lazy=True)

#     def __init__(self, weight, date):
#         self.weight = weight
#         self.date = date

# # User Model
# class User(db.Model):
#     user_id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(80), nullable=False)
#     user_email = db.Column(db.String(80), nullable=False)
#     user_password = db.Column(db.String(80), nullable=False)
#     bodyweight = db.relationship('Bodyweight', backref='user', lazy=True)

#     def __init__(self, user_name, user_email, user_password):
#         self.user_name = user_name
#         self.user_email = user_email
#         self.user_password = user_password