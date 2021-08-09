from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime

from common import Model
from util.time import get_msk_time


class Transaction(Model):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    sender = Column(
        ForeignKey('users.vk_id', onupdate='CASCADE', ondelete='CASCADE'),
        nullable=False
    )
    destination = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False, default=get_msk_time)
    currency = Column(
        ForeignKey('currencies.id', onupdate='CASCADE', ondelete='SET NULL'),
        nullable=False
    )
    amount = Column(Numeric(15, 3), nullable=False)
    message = Column(String(255))

    def __repr__(self):
        return 'Transaction(' \
            'id={0.id}, ' \
            'sender={0.sender}, ' \
            'destination={0.destination}, ' \
            'time={0.time}, ' \
            'currency={0.currency}, ' \
            'amount={0.amount}, ' \
            'message={0.message}' \
        ')'.format(self)
