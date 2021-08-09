from sqlalchemy.orm import Session
from sqlalchemy import Column, ForeignKey, Numeric

from common import Model
from .transaction import Transaction
from .pending_transaction import PendingTransaction
from .coins import COIN_CLASSES, Coin
from exc import EmptyBankAccountError, UnknownCurrencyError
from util.logging import log


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

    def __init__(self, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        try:
            self.currency_api: Coin = COIN_CLASSES[self.currency]()
        except KeyError:
            raise UnknownCurrencyError(self.currency)

    def replenish(self, amount, *, session: Session):
        url = self.currency_api.get_payment_url(amount)

        trans = session.get(PendingTransaction, (self.user_id, self.currency))
        if trans is None:
            trans = PendingTransaction(user_id=self.user_id,
                                       currency=self.currency,
                                       destination=0)
            session.add(trans)
        else:
            trans.destination = 0

        return url

    def withdraw(self, amount, *, session: Session):
        if self.balance == 0:
            raise EmptyBankAccountError(self.user_id)

        amount = min(amount, self.balance)
        self.currency_api.send_money(self.user_id, amount)
        self.balance -= amount
        # It's guaranteed that money would be sent
        # because target and money have already been fixed in db

        trans = Transaction(sender=self.user_id,
                            destination=0,
                            amount=-amount,
                            currency=self.currency)
        session.add(trans)
        log(f'User {self.user_id} has withdrawn {amount} {self.currency}s')

        return amount
