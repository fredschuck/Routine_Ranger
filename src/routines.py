from src.models import db, Routine, RoutineExercise

class Routines:
    '''This class contains methods for interacting with the Routine model'''

    def get_routine(self, routine_id):
        '''Returns a routine object based on the routine_id'''
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        return routine

    def get_all_routines(self):
        '''Returns a list of all routine objects'''
        all_routines = Routine.query.all()
        return all_routines

    def add_routine(self, routine_name):
        '''Adds a new routine to the database'''
        new_routine = Routine(routine_name)
        db.session.add(new_routine)
        db.session.commit()
        return new_routine
    
    def add_exercise_to_routine(self, routine_id, exercise_id):
        '''Links an exercise to a routine'''
        new_routine_exercise = RoutineExercise(routine_id, exercise_id)
        db.session.add(new_routine_exercise)
        db.session.commit()
        return new_routine_exercise #should it return the exercise instance?

    def update_routine(self, routine_id, routine_name):
        '''Updates a routine in the database'''
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        routine.routine_name = routine_name
        db.session.commit()
        return routine

    def delete_routine(self, routine_id):
        '''Deletes a routine from the database'''
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        db.session.delete(routine)
        db.session.commit()
        return routine
    
routines = Routines()