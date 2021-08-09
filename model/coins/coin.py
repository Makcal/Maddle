from abc import ABC, ABCMeta, abstractmethod

from sqlalchemy import Column, String, Numeric, SmallInteger, select
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.exc import NoResultFound

from common import Model
from .coin_account import CoinAccount
from exc import UnknownCurrencyError


class _CoinMeta(DeclarativeMeta, ABCMeta):
    pass


class Coin(Model, ABC, metaclass=_CoinMeta):
    __tablename__ = 'coins'
    __abstract__ = True

    id = Column(SmallInteger, primary_key=True)
    name = Column(String(31), nullable=False, unique=True)
    factor = Column(Numeric(18, 12), nullable=False)
    unit_multiplicity = Column(
        SmallInteger,
        nullable=False,
        default=3
    )

    def __init__(self, *args, **kwargs):
        super(Coin, self).__init__(*args, **kwargs)
        self.account = self.init_account()

    def __repr__(self):
        return '{0.__class__.__name__}(' \
            'id={0.id}, ' \
            'name={0.name}, ' \
            'factor={0.factor}, ' \
            'unit_multiplicity={0.unit_multiplicity}' \
        ')'.format(self)

    @classmethod
    def load(cls, session):
        try:
            return session.execute(
                select(cls).where(cls.name == cls.get_name())
            ).scalar_one()
        except NoResultFound:
            raise UnknownCurrencyError(cls.get_name())

    @staticmethod
    @abstractmethod
    def get_name():
        pass

    @abstractmethod
    def init_account(self) -> CoinAccount:
        return CoinAccount(360092594, 'token')

    @abstractmethod
    def get_accounts_data(self, *ids):
        pass

    @abstractmethod
    def create_payment_url(self, to_id, amount, free_amount=False):
        pass

    @abstractmethod
    def get_payment_url(self, amount, free_amount=False):
        pass

    @abstractmethod
    def send_money(self, to_id, amount):
        pass

    @abstractmethod
    def get_transactions(self, count=None, offset=0):
        pass

    def callback(self):
        pass

    def longpoll(self):
        pass
