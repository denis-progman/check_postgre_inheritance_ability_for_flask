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


    def createUser(request_body):
        new_user = User()

        for field_name in new_user.mutable_fields:
            setattr(new_user, field_name, request_body.get(field_name, None))

        db.session.add(new_user)
        db.session.commit()
        return __class__.get_user_by_id(new_user.id)