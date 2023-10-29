import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from src.models import db
from src.routines import routines
from src.exercises import exercises
from src.exercise_attributes import exercise_attributes
from src.bodyweight import bodyweights
# from src.logged_exercises import logged_exercises
# from src.routine_exercise import routine_exercise


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
    ''' Allow the user to select a routine to log'''
    routine_id = request.form.get('routine_droplist', 'error')
    routine = routines.get_routine(routine_id)
    return redirect(f'/log_workout/{routine.routine_name}/{routine.routine_id}')

@app.get('/log_workout/<routine_name>/<routine_id>')
def log_workout(routine_name, routine_id):
    ''' Allow the user to log a workout'''
    routine_exercises = routines.get_exercises_by_routine_id(routine_id)
    attributes = {}
    for exercise in routine_exercises:
        attributes_list = exercises.get_exercise_attributes(exercise.exercise_id)
        print(attributes_list)
        attributes[exercise.exercise_id] = attributes_list
    return render_template('log.html', routine=routine_exercises, attributes=attributes, routine_name=routine_name, routine_id=routine_id)

@app.post('/log_workout/<routine_name>/<routine_id>')
def save_workout(routine_name, routine_id):
    ''' Save the user's workout '''
    print(request.form)
    for key, value in request.form.items():
        print(f"{key}: {value}")

    form_data = request.form
    log_date = form_data.get('log_date', 'error')
    log_time = form_data.get('log_time', 'error')
    exercise_data = {} 
    for key, value in form_data.items():
        parts = key.split('_')
        if len(parts) == 3 and parts[0] == 'exercise':
            exercise_id = int(parts[1])
            attribute = parts[2]
            if exercise_id not in exercise_data:
                exercise_data[exercise_id] = {}
            exercise_data[exercise_id][attribute] = value
    for exercise_id, data in exercise_data.items():
        # print(f"exercise_id: {exercise_id}, data: {data}")
        # print(exercise_id, log_date, log_time, data['sets'], data['reps'], data['weight'], data['height'], data['speed'], data['distance'], data['time'])
        # for exercise_id, data in exercise_data.items():
        # print(f"exercise_id: {exercise_id}, data: {data}")
        SENTINEL = None
        sets = data.get('sets', SENTINEL)
        reps = data.get('reps', SENTINEL)
        weight = data.get('weight', SENTINEL)
        height = data.get('height', SENTINEL)
        speed = data.get('speed', SENTINEL)
        distance = data.get('distance', SENTINEL)
        time = data.get('time', SENTINEL)
        exercises.log_exercise(exercise_id, log_date, log_time, sets, reps, weight, height, speed, distance, time)
        # exercises.log_exercise(exercise_id, log_date, log_time, data['sets'], data['reps'], data['weight'], data['height'], data['speed'], data['distance'], data['time'])
    return redirect('/')

@app.post('/log')
def save_log():
    ''' Save the user's workout '''
    return render_template('routine_select.html', routines=routines.get_all_routines())

@app.get('/log_bodyweight')
def log_bodyweight():
    ''' Allow the user to log their bodyweight '''
    return render_template('log_bodyweight.html')

@app.post('/log_bodyweight')
def save_bodyweight():
    ''' Save the user's bodyweight '''
    date = request.form.get('date', 'error')
    weight = request.form.get('weight', 'error')
    print(f"date: {date}, bodyweight: {weight}")
    bodyweights.add_bodyweight(weight, date)
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return redirect('/error')

# DON'T FORGET THAT CARDIO HAS INCLINE
# Create a name field for exercises that auto completes or auto generates exercise options
# Allow the user to be able to log in and immediately choose how simple or complex they want the app to be
# What do you do when you need to log an exercise session? that isn't a routine?