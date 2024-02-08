from models import Gamer
from sqlalchemy import select, desc
from db import db


class GamerService:
    def get_by(field = None, field_value = None, from_number = None, count = None):
        clauses = []
        if not field == None:
            clauses.append(Gamer.__dict__[field] == field_value)

        stmt = select(Gamer).order_by(desc(Gamer.id)).slice(from_number, count)

        response = {}
        for row in db.session.execute(stmt):
            response[row.Gamer.id] = row.Gamer.toDict()
        return response

    def get_by_id(id):
        return __class__.get_by("id", id)[int(id)]

    def create(request_body):
        new_one = Gamer()

        for field_name in new_one.mutable_fields:
            setattr(new_one, field_name, request_body.get(field_name, None))
        
        db.session.add(new_one)
        db.session.commit()
        return __class__.get_by_id(new_one.id)

    def update(id, request_body):
        the_one = Gamer.query.get(id)

        for field_key, field_value in request_body.items():
            setattr(the_one, field_key, field_value)
        db.session.commit()

        return __class__.get_by_id(id)


    def delete(id):
        the_one = Gamer.query.get(id)
        if the_one == None:
            return ('Object(id:{}) is not found!').format(id)

        db.session.delete(the_one)
        db.session.commit()
        return ('Object(id:{}) deleted successfully!').format(id)
