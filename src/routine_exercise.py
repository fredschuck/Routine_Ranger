from src.models import db, RoutineExercise

class RoutinesExercises:
    '''This class contains methods to interact with the RoutineExercise model'''
    
    def get_all_routine_exercises(self):
        '''Returns a list of all routine exercise objects'''
        all_routine_exercises = RoutineExercise.query.all()
        return all_routine_exercises
    
    def get_routine_exercises_by_routine_id(self, routine_id):
        '''Returns a list of routine exercise objects based on the routine_id'''
        routine_exercises = RoutineExercise.query.filter_by(routine_id=routine_id).all()
        return routine_exercises
    
    def Link_routine_exercise(self, routine_id, exercise_id):
        '''Links an exercise to a routine'''
        new_routine_exercise = RoutineExercise(routine_id, exercise_id)
        db.session.add(new_routine_exercise)
        db.session.commit()
        return new_routine_exercise
    
routine_exercise = RoutinesExercises()