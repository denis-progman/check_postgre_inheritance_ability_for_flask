from models import User
from sqlalchemy import select, desc
from db import db


class UserService:
    def get_users_by(field = None, field_value = None, from_number = None, count = None):

        statement  = select(User).where(getattr(User, field) == field_value)

        response = {}
        for row in db.session.execute(statement):
            response[User.__name__.lower()] = row.User.toDict()            
        return response

    def get_user_by_id(user_id):
        return __class__.get_users_by("id", user_id)

    def create_user(request_body):

        response = __class__.get_users_by('google_id', request_body['google_id'])

        if not response:                
            new_user = User()

            for field_name in new_user.mutable_fields:
                setattr(new_user, field_name, request_body.get(field_name, None))
            
            db.session.add(new_user)
            db.session.commit()
            return __class__.get_user_by_id(new_user.id)
        else:
            return response

    def update_user(user_id, request_body):
        user = User.query.get(user_id)

        for field_key, field_value in request_body.items():
            setattr(user, field_key, field_value)
        db.session.commit()

        return __class__.get_user_by_id(user_id)


    def delete_user(user_id):
        user = User.query.get(user_id)
        if user == None:
            return ('User with Id "{}" is not found!').format(user_id)

        db.session.delete(user)
        db.session.commit()
        return ('User with Id "{}" deleted successfully!').format(user_id)
