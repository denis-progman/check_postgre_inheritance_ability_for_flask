from sqlalchemy import Column, ForeignKey, Identity, Integer
from models.gamer import Gamer


class Loser(Gamer):
    __tablename__ = 'losers'
    __mapper_args__ = {
        'polymorphic_identity': 'losers',
    }

    mutable_fields = [
        "first_name",
        "last_name",
        "nickname",
        "avatar",
        "best_score",
        "lost_games_count",
    ]

    id = Column(None, ForeignKey('gamers.id'), primary_key=True)
    lost_games_count = Column(Integer, nullable=False, default=0)
