from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

routine_list = {
    # 'Chest': ['Bench Press', 'Incline Bench Press', 'Decline Bench Press', 'Dumbbell Flyes', 'Cable Flyes'],
    # 'Back': ['Deadlift', 'Bent Over Row', 'Pull Ups', 'Lat Pulldown', 'Seated Cable Row']
} # Contains all routines as dictionary and stores exercises as a list
exercise_list = {}


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
    ### delete later ############
    for x in routine_list:
        print(x)
        for y in routine_list[x]:
            print(y)
    #############################
    return redirect('/')

@app.get('/create_exercise')
def create_exercise():
    return render_template('create_exercise.html', routines=routine_list)

@app.post('/add_exercise')
def add_exercise():
    exercise = request.form.get('exercise_name', 'error')
    exercise_list[f'{exercise}'] = []
    routine = request.form.get('routine_name', 'error')
    routine_list[f'{routine}'].append(f'{exercise}')
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/error')

@app.get('/log')
def log_workout():
    return render_template('log.html', routines=routine_list)

