from sqlalchemy import Column, String, Numeric, SmallInteger

from common import Model


class Coin(Model):
    __tablename__ = "currencies"

    id = Column(SmallInteger, primary_key=True)
    name = Column(String(31), nullable=False, unique=True)
    factor = Column(Numeric(18, 12), nullable=False)
    unit_multiplicity = Column(
        SmallInteger,
        nullable=False,
        default=3
    )
