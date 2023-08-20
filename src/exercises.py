from src.models import db, Exercise

class Exercises:
    '''This class contains methods for interacting with the Exercise model'''

    def get_exercise(self, exercise_id):
        '''Returns an exercise object based on the exercise_id'''
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        return exercise

    def get_all_exercises(self):
        '''Returns a list of all exercise objects'''
        all_exercises = Exercise.query.all()
        return all_exercises

    def add_exercise(self, exercise_name):
        '''Adds a new exercise to the database'''
        new_exercise = Exercise(exercise_name)
        db.session.add(new_exercise)
        db.session.commit()
        return new_exercise

    def update_exercise(self, exercise_id, exercise_name):
        '''Updates an exercise in the database'''
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        exercise.exercise_name = exercise_name
        db.session.commit()
        return exercise

    def delete_exercise(self, exercise_id):
        '''Deletes an exercise from the database'''
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        db.session.delete(exercise)
        db.session.commit()
        return exercise
    
exercises = Exercises()