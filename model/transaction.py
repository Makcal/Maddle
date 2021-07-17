from sqlalchemy import Column, Integer, ForeignKey, String, Numeric, DateTime

from common import Model


class Transaction(Model):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    sender = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False
    )
    destination = Column(Integer, nullable=False)
    time = Column(DateTime, nullable=False)
    currency = Column(
        ForeignKey("currencies.name", onupdate="CASCADE", ondelete="SET NULL")
    )
    amount = Column(Numeric(15, 3), nullable=False)
    message = Column(String(255))
