from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

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