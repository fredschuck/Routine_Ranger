import os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from src.models import db, Routine, Exercise, ExerciseAttributes
from src.routines import routines
from src.exercises import exercises
from src.exercise_attributes import exercise_attributes
from src.logged_exercises import logged_exercises
from src.routine_exercise import routine_exercise


app = Flask(__name__)

# Database Connection
load_dotenv()

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] \
    = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False # set to True to see SQL queries

# app.config['ENV'] = 'development'
# app.config['DEBUG'] = True
# app.config['TESTING'] = True 

db.init_app(app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/error')
def error():
    return render_template('error.html')

@app.get('/create_routine')
def create_routine():
    return render_template('create_routine.html')

@app.post('/add_routine')
def add_routine():
    routine = request.form.get('routine_name', 'error')
    routines.add_routine(routine)
    return redirect('/')

@app.get('/create_exercise')
def create_exercise():
    return render_template('create_exercise.html', routines=routines.get_all_routines())

@app.post('/add_exercise')
def add_exercise():
    exercise = request.form.get('exercise_name', 'error')
    new_exercise = exercises.add_exercise(exercise)
    attributes = request.form.getlist('exercise_attributes')
    sets, reps, weight, height, speed, distance, time = False, False, False, False, False, False, False
    for attribute in attributes: #create a nested for loop? 
        if attribute == 'sets':
            sets = True
        if attribute == 'reps':
            reps = True
        if attribute == 'weight':
            weight = True
        if attribute == 'height':
            height = True
        if attribute == 'speed':
            speed = True
        if attribute == 'distance':
            distance = True
        if attribute == 'time':
            time = True
    exercise_attributes.add_attributes(new_exercise.exercise_id, sets, reps, weight, height, speed, distance, time)
    routine = request.form.get('routine_droplist', 'error')
    if routine != 'error':
        routines.add_exercise_to_routine(routine, new_exercise.exercise_id)
    return redirect('/')

@app.get('/log')
def log():
    return render_template('routine_select.html', routines=routines.get_all_routines())

@app.post('/log_select')
def log_select():
    routine_id = request.form.get('routine_droplist', 'error')
    routine = routines.get_routine(routine_id)
    return redirect(f'/log_workout/{routine.routine_name}/{routine.routine_id}')

@app.get('/log_workout/<routine_name>/<routine_id>')
def log_workout(routine_name, routine_id):
    # get all exercises in routine
    routine_exercises = routines.get_exercises_by_routine_id(routine_id)
    # create a dictionary of exercise attributes
    attributes = {}
    # for each exercise in routine, get the exercise attributes and add them to the dictionary
    for exercise in routine_exercises:
        # get the exercise attributes
        attributes_list = exercises.get_exercise_attributes(exercise.exercise_id)
        print(attributes_list)
        # add the exercise attributes to the dictionary
        attributes[exercise.exercise_id] = attributes_list
    return render_template('log.html', routine=routine_exercises, attributes=attributes)

@app.post('/log')
def save_log():
    return render_template('routine_select.html', routines=routines.get_all_routines())

@app.get('/log_bodyweight')
def log_bodyweight():
    ''' Allow the user to log their bodyweight '''
    return render_template('log_bodyweight.html')

'''

ERROR HANDLING

'''

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/error')

# DON'T FORGET THAT CARDIO HAS INCLINE
# Create a name field for exercises that auto completes or auto generates exercise options
# Allow the user to be able to log in and immediately choose how simple or complex they want the app to be
# What do you do when you need to log an exercise session? that isn't a routine?