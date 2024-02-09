from sqlalchemy import Column, ForeignKey, Identity, Integer
from models.user import User
from db import db


class Viewer(User):
    __tablename__ = 'viewers'
    __mapper_args__ = {
        'polymorphic_identity': 'viewers',
    }

    mutable_fields = [
        "first_name",
        "last_name",
        "nickname",
        "avatar",
        "viewed_games_count",
        # "best_gamer_id",
    ]

    id = Column(None, ForeignKey('users.id'), primary_key=True)
    viewed_games_count = Column(Integer, nullable=False, default=0)

    # best_gamer_id = Column(None, ForeignKey('gamers.id'))
    # best_gamer = db.relationship("Gamer", primaryjoin="Viewer.best_gamer_id==Gamer.id", back_populates="fans", lazy='dynamic')

