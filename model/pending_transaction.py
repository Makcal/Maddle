from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime

from common import Model
from util.time import get_msk_time


class PendingTransaction(Model):
    __tablename__ = 'pending_transactions'

    user_id = Column(
        ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True
    )
    currency = Column(
        ForeignKey('currencies.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True
    )
    time = Column(
        DateTime,
        nullable=False,
        default=get_msk_time,
        onupdate=get_msk_time
    )
    destination = Column(Integer, nullable=False)
    message = Column(String(255), onupdate=None)

    def __repr__(self):
        return 'PendingTransaction(' \
            'user_id={0.user_id}, ' \
            'currency={0.currency}, ' \
            'time={0.time}, ' \
            'destination={0.destination}, ' \
            'message={0.message}' \
        ')'.format(self)
