from sqlalchemy import Column, Integer

from common import Model


class User(Model):
    __tablename__ = 'users'

    id = Column('vk_id', Integer, primary_key=True)
    new_transactions = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return 'User(' \
            'id={0.id}, ' \
            'new_transactions={0.new_transactions}' \
        ')'.format(self)
