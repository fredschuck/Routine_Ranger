from src.models import db, ExerciseAttributes

class ExerciseAttribute:
    '''This class contains methods for interacting with the ExerciseAttributes model'''

    def get_attributes(self):
        '''Returns a list of all exercise attributes'''
        attributes = ExerciseAttributes.query.all()
        return attributes
    
    def get_attributes_by_id(self, exercise_id):
        '''Returns exercise attributes based on the exercise_id'''
        attributes = ExerciseAttributes.query.filter_by(exercise_id=exercise_id).first()
        return attributes
    
    def add_attributes(self, exercise_id, sets, reps, weight, height, speed, distance, time):
        '''Adds new exercise attributes to the database'''
        new_attributes = ExerciseAttributes(exercise_id, sets, reps, weight, height, speed, distance, time)
        db.session.add(new_attributes)
        db.session.commit()
        return new_attributes
    
exercise_attributes = ExerciseAttribute()