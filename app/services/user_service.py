from exceptions.fatal_error import FatalError
from models import User
from sqlalchemy import select
from db import db


class UserService:
    def get_users_by(field = None, field_value = None, from_number = None, count = None):

        statement  = select(User).where(getattr(User, field) == field_value)

        users = []
        for row in db.session.execute(statement):
            users.append(row.User.toDict())    

        return users
    
    def get_user_by_id(user_id):
        return __class__.get_users_by("id", user_id)[0]
    
    def create_update_user_by(unique_user_field_name, user_data):
        users = __class__.get_users_by(unique_user_field_name, user_data[unique_user_field_name])
        amount_of_users = len(users)

        if amount_of_users == 0:
            user = User()
        elif amount_of_users == 1:
            user = users[0]
        else:
            raise FatalError(f'Error! {amount_of_users} users have been found by the unique field "{unique_user_field_name}"')


        for field_name in user.mutable_fields:
            setattr(user, field_name, user_data.get(field_name, None))
        
        db.session.add(user)
        db.session.commit()

        return __class__.get_user_by_id(user.id)

    def update_user_by_id(user_id, request_body):
        user = User.query.get(user_id)

        for field_key, field_value in request_body.items():
            setattr(user, field_key, field_value)
        db.session.commit()

        return __class__.get_user_by_id(user_id)


    def delete_user_by_id(user_id):
        user = User.query.get(user_id)
        if user == None:
            return ('User with Id "{}" is not found!').format(user_id)

        db.session.delete(user)
        db.session.commit()
        return ('User with Id "{}" deleted successfully!').format(user_id)
    
