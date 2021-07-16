from sqlalchemy import Column, Integer, ForeignKey

from common import Model


class Favourite(Model):
    __tablename__ = 'favourites'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    favourite_id = Column(Integer, primary_key=True)
