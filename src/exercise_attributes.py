from src.models import db, ExerciseAttributes, Routine, RoutineExercise
from src.routine_exercise import routine_exercise

class ExerciseAttribute:
    '''This class contains methods for interacting with the ExerciseAttributes model'''

    def get_attributes(self):
        '''Returns a list of all exercise attributes'''
        attributes = ExerciseAttributes.query.all()
        return attributes
        
    def add_attributes(self, exercise_id, sets, reps, weight, height, speed, distance, time):
        '''Adds new exercise attributes to the database'''
        new_attributes = ExerciseAttributes(exercise_id, sets, reps, weight, height, speed, distance, time)
        db.session.add(new_attributes)
        db.session.commit()
        return new_attributes
    
    # def get_attributes_by_routine_id(self, routine_id): #Move this to routines.py? Is this even needed?
    #     '''Returns attributes of all exercises based on the routine_id'''
    #     attributes = {}
    #     routine = routine_exercise.get_exercises_by_routine_id(routine_id)
    #     for exercise in routine:
    #         attributes[exercise.exercise_id] = ExerciseAttributes.query.filter_by(exercise_id=exercise.exercise_id).first()
    #     return attributes
    
exercise_attributes = ExerciseAttribute()