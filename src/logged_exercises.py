from src.models import db, LoggedExercises

class LoggedExercise:
    '''This class contains methods to interact with the LoggedExercise model'''
    
    def get_logged_exercise(self, log_id):
        '''Returns a logged exercise object based on the logged_exercise_id'''
        logged_exercise = LoggedExercises.query.filter_by(log_id=log_id).first()
        return logged_exercise
    
    def get_all_logged_exercises(self):
        '''Returns a list of all logged exercise objects'''
        all_logged_exercises = LoggedExercises.query.all()
        return all_logged_exercises
    
    def log_exercise(self, exercise_id, log_date, log_time, sets, reps, weight, height, speed, distance, time):
        '''Logs a new exercise to the database'''
        new_logged_exercise = LoggedExercises(exercise_id, log_date, log_time, sets, reps, weight, height, speed, distance, time)
        db.session.add(new_logged_exercise)
        db.session.commit()
        return new_logged_exercise
    
    def update_logged_exercise(self, log_id, exercise_id, log_date, log_time, sets, reps, weight, height, speed, distance, time):
        '''Updates a logged exercise in the database'''
        logged_exercise = LoggedExercises.query.filter_by(log_id=log_id).first()
        logged_exercise.exercise_id = exercise_id
        logged_exercise.log_date = log_date
        logged_exercise.log_time = log_time
        logged_exercise.sets = sets
        logged_exercise.reps = reps
        logged_exercise.weight = weight
        logged_exercise.height = height
        logged_exercise.speed = speed
        logged_exercise.distance = distance
        logged_exercise.time = time
        db.session.commit()
        return logged_exercise
    
    def delete_logged_exercise(self, log_id):
        '''Deletes a logged exercise from the database'''
        logged_exercise = LoggedExercises.query.filter_by(log_id=log_id).first()
        db.session.delete(logged_exercise)
        db.session.commit()
        return logged_exercise
    
logged_exercises = LoggedExercise()