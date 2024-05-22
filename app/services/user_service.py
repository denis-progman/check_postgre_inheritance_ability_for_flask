from models.user import User
from sqlalchemy import select, desc
from db import db

class UserService:
    def get_all_users():

        stmt = select(User).order_by(desc(User.id))

        response = {}
        for row in db.session.execute(stmt):
            response[row.User.id] = row.User.toDict()
        return response


    def create_user(request_body):
        new_user = User()

        for field_name in new_user.mutable_fields:
            setattr(new_user, field_name, request_body.get(field_name, None))

        db.session.add(new_user)
        db.session.commit()
        return __class__.get_user_by_id(new_user.id)
    
<<<<<<< HEAD
=======
    def update_user(user_id, request_body):
        user = User.query.get(user_id)

        for field_key, field_value in request_body.items():
            setattr(user, field_key, field_value)
        db.session.commit()

        return __class__.get_user_by_id(user_id)
    
>>>>>>> bb8bfb8 (issue: checking bad request)
    def get_users_by(field = None, field_value = None, from_number = None, count = None):
        clauses = []
        if not field == None:
            clauses.append(User.__dict__[field] == field_value)

        stmt = select(User).order_by(desc(User.id)).slice(from_number, count)

        response = {}
        for row in db.session.execute(stmt):
            response[row.User.id] = row.User.toDict()
        return response

    def get_user_by_id(user_id):
<<<<<<< HEAD
        return __class__.get_users_by("id", user_id)[int(user_id)]
=======
        return __class__.get_users_by("id", user_id)
    
    def get_user_by_google_id(google_id):
        return __class__.get_users_by("google_id", google_id)
>>>>>>> bb8bfb8 (issue: checking bad request)
    
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user == None:
            return ('User with Id "{}" is not found!').format(user_id)

        db.session.delete(user)
        db.session.commit()
        return ('User with Id "{}" deleted successfully!').format(user_id)