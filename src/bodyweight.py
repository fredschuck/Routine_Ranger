from src.models import db, Bodyweight

class Bodyweights:
    ''' This class contains methods for interacting with the Bodyweight model '''

    def get_all_bodyweights(self):
        ''' Returns a list of all bodyweight objects '''
        all_bodyweights = Bodyweight.query.all()
        return all_bodyweights
    
    def get_bodyweight(self, bodyweight_id):
        ''' Returns a bodyweight object based on the bodyweight_id '''
        bodyweight = Bodyweight.query.filter_by(bodyweight_id=bodyweight_id).first()
        return bodyweight
    
    def add_bodyweight(self, bodyweight, bodyweight_date):
        ''' Adds a new bodyweight to the database '''
        print("You've entered the add_bodyweight method")
        new_bodyweight = Bodyweight(bodyweight, bodyweight_date)
        db.session.add(new_bodyweight)
        db.session.commit()
        return new_bodyweight
    
    def edit_bodyweight(self, bodyweight_id, bodyweight):
        ''' Updates a bodyweight in the database '''
        bodyweight = Bodyweight.query.filter_by(bodyweight_id=bodyweight_id).first()
        bodyweight.bodyweight = bodyweight
        db.session.commit()
        return bodyweight
    
    def delete_bodyweight(self, bodyweight_id):
        ''' Deletes a bodyweight from the database '''
        bodyweight = Bodyweight.query.filter_by(bodyweight_id=bodyweight_id).first()
        db.session.delete(bodyweight)
        db.session.commit()
        return bodyweight
    
bodyweights = Bodyweights()
