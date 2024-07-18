from sqlalchemy import Identity
from datetime import datetime
from models.main_model import MainModel
from db import db

class User(MainModel, db.Model):
    __tablename__ = 'users'

    __mapper_args__ = {
        "polymorphic_identity": "users",
        "polymorphic_on": "type",
    }

    mutable_fields = [
        "login",
        # "date_of_birth",
        "user_name",
        "avatar",
        "google_id"
    ]
    
    
# Auto Generated Fields:
    id = db.Column(db.Integer(), Identity(), primary_key=True, nullable=False, unique=True,)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    type = db.Column(db.String(100))

# Input by User Fields:
    login = db.Column(db.String(100), nullable=True, unique=True)
    # date_of_birth = db.Column(db.DateTime, nullable=True)
    user_name = db.Column(db.String(100), nullable=True)
    middle_name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(256))
    google_id = db.Column(db.String(), unique=True)
    # apple_id = db.Column(db.String(), nullable=True, unique=True)

    # @validates('time_per_unit')
    # def empty_string_to_null(self, key, value):
    #     if isinstance(value, str) and value == '':
    #         return None
    #     else:
    #         return value

    # @classmethod
    # def __declare_last__(cls):
    #     ValidateString(Item.name, False, True, "The name type must be string")
    #     ValidateNumber(Item.price, True, "The price type must be number")
    #     ValidateURL(Item.image_link, True, True, "The image link is not valid")
