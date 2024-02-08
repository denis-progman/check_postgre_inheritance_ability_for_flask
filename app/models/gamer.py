from sqlalchemy import Column, ForeignKey, Identity, Integer
from datetime import datetime
from app.models.user import User
from .main_model import MainModel
from db import db


class Gamer(User):
    __tablename__ = 'gamers'
    __mapper_args__ = {
        'polymorphic_identity': 'gamers',
        "polymorphic_on": "type"
    }

    mutable_fields = [
        "first_name",
        "last_name",
        "nickname",
        "avatar",
        "best_score"
    ]

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    best_score = Column(Integer, nullable=False, default=0)
