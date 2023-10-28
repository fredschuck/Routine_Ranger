from src.models import db, Exercise, ExerciseAttributes

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
    
    def get_exercise_attributes(self, exercise_id):
        '''Returns exercise attributes based on the exercise_id'''
        attributes = ExerciseAttributes.query.filter_by(exercise_id=exercise_id).first()

        if attributes:
            true_attributes = []
            for column in ExerciseAttributes.__table__.columns:
                if getattr(attributes, column.name):
                    true_attributes.append(column.name)
            return true_attributes
        else:
            return []

    def add_exercise(self, exercise_name):
        '''Adds a new exercise to the database'''
        new_exercise = Exercise(exercise_name)
        db.session.add(new_exercise)
        db.session.commit()
        return new_exercise

    def edit_exercise(self, exercise_id, exercise_name):
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