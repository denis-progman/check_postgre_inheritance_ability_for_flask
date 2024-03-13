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
        return __class__.get_users_by("id", user_id)[int(user_id)]
    
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user == None:
            return ('User with Id "{}" is not found!').format(user_id)

        db.session.delete(user)
        db.session.commit()
        return ('User with Id "{}" deleted successfully!').format(user_id)