from src.models import db, Exercise

class Exercises:

    def get_exercise(self, exercise_id):
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        return exercise

    def get_all_exercises(self):
        exercises = Exercise.query.all()
        return exercises

    def add_exercise(self, exercise_name):
        new_exercise = Exercise(exercise_name)
        db.session.add(new_exercise)
        db.session.commit()
        return new_exercise

    def update_exercise(self, exercise_id, exercise_name):
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        exercise.exercise_name = exercise_name
        db.session.commit()
        return exercise

    def delete_exercise(self, exercise_id):
        exercise = Exercise.query.filter_by(exercise_id=exercise_id).first()
        db.session.delete(exercise)
        db.session.commit()
        return exercise
    
exercises = Exercises()