from src.models import db, Routine, Exercise, RoutineExercise, Bodyweight, User

class Routine:
    
    def __init__(self):
        pass

    def get_routine(self, routine_id):
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        return routine

    def get_routines(self):
        routines = Routine.query.all()
        return routines

    def add_routine(self, routine_name):
        new_routine = Routine(routine_name)
        db.session.add(new_routine)
        db.session.commit()
        return new_routine

    def update_routine(self, routine_id, routine_name):
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        routine.routine_name = routine_name
        db.session.commit()
        return routine

    def delete_routine(self, routine_id):
        routine = Routine.query.filter_by(routine_id=routine_id).first()
        db.session.delete(routine)
        db.session.commit()
        return routine
    
routine = Routine()