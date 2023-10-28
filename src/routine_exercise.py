from src.models import db, RoutineExercise, Exercise

class RoutinesExercises:
    '''This class contains methods to interact with the RoutineExercise model'''
    
    def get_all_routine_exercises(self):
        '''Returns a list of all routine exercise objects'''
        all_routine_exercises = RoutineExercise.query.all()
        return all_routine_exercises
    
    # def get_exercises_by_routine_id(self, routine_id):
    #     '''Returns a list of exercises that are in a routine'''
    #     exercise_ids = RoutineExercise.query.filter_by(routine_id=routine_id).with_entities(RoutineExercise.exercise_id).all() #returns tuples
    #     exercise_ids_list = [exercise_id[0] for exercise_id in exercise_ids]
    #     exercises = Exercise.query.filter(Exercise.exercise_id.in_(exercise_ids_list)).all()
    #     return exercises
    
routine_exercise = RoutinesExercises()