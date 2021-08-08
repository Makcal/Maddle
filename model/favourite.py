from sqlalchemy import Column, Integer, ForeignKey

from common import Model


class Favourite(Model):
    __tablename__ = 'favourites'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    favourite_id = Column(Integer, primary_key=True)

    def __repr__(self):
        return 'Favourite(' \
            'user_id={0.user_id}, ' \
            'favourite_id={0.favourite_id}' \
        ')'.format(self)
