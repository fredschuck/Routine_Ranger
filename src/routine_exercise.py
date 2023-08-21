from src.models import db, RoutineExercise

class RoutinesExercises:
    '''This class contains methods to interact with the RoutineExercise model'''
    
    def get_all_routine_exercises(self):
        '''Returns a list of all routine exercise objects'''
        all_routine_exercises = RoutineExercise.query.all()
        return all_routine_exercises
    
    def get_exercises_by_routine_id(self, routine_id):
        '''Returns a list of exercises that are in a routine'''
        exercises = RoutineExercise.query.filter_by(routine_id=routine_id).all()
        return exercises
    
routine_exercise = RoutinesExercises()