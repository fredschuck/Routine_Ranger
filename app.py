import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv


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


routine_list = {
    'Back': ['Deadlift', 'Pull Ups', 'Hammer Curls'],
    'Chest': ['Bench Press', 'Cardio'],
}
exercise_list = {}
body_weight = {}


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
    routine_list[f'{routine}'] = []
    return redirect('/')

@app.get('/create_exercise')
def create_exercise():
    return render_template('create_exercise.html', routines=routine_list)

@app.post('/add_exercise')
def add_exercise():
    exercise = request.form.get('exercise_name', 'error')
    exercise_list[f'{exercise}'] = []
    routine = request.form.get('routine_droplist', 'error')
    routine_list[f'{routine}'].append(f'{exercise}')
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/error')

@app.get('/log')
def log():
    return render_template('routine_select.html', routines=routine_list)

@app.post('/log_select')
def log_select():
    routine = request.form.get('routine_droplist', 'error')
    return redirect(f'/log_workout/{routine}')

@app.get('/log_workout/<routine>')
def log_workout(routine):
    for key, value in routine_list.items():
        if key == routine:
            return render_template('log.html', routine=value)
    return redirect('/error')

@app.post('/log')
def save_log():
    return render_template('routine_select.html', routines=routine_list)

@app.get('/log_bodyweight')
def log_bodyweight():
    return render_template('log_bodyweight.html')


# DON'T FORGET THAT CARDIO HAS INCLINE
# Create a name field for exercises that auto completes or auto generates exercise options
# Allow the user to be able to log in and immediately choose how simple or complex they want the app to be