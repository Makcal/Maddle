from sqlalchemy import Column, ForeignKey, Boolean

from common import Model


class NotificationsSettings(Model):
    __tablename__ = 'notifications_settings'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    transactions = Column(Boolean, default=True)
    requests = Column(Boolean, default=True)
    market_news = Column(Boolean, default=True)
    mailing = Column(Boolean, default=True)
