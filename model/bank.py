from sqlalchemy import Column, ForeignKey, Numeric

from common import Model


class BankAccount(Model):
    __tablename__ = 'bank'

    user_id = Column(
        ForeignKey('users.vk_id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True
    )
    currency = Column(
        ForeignKey('currencies.id', onupdate='CASCADE', ondelete='CASCADE'),
        primary_key=True
    )
    balance = Column(Numeric(20, 9), nullable=False, default=0)

    def __repr__(self):
        return 'BankAccount(' \
            'user_id={0.user_id}, ' \
            'currency={0.currency}, ' \
            'balance={0.balance}' \
        ')'.format(self)
