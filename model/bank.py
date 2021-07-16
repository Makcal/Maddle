from sqlalchemy import Column, ForeignKey, Numeric

from common import Model


class BankAccount(Model):
    __tablename__ = 'bank'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    currency = Column(
        ForeignKey("currencies.name", onupdate="CASCADE", ondelete="SET NULL"),
        nullable=False,
        primary_key=True
    )
    account = Column(Numeric(20, 9), nullable=False, default=0)
