from sqlalchemy import Column, Integer, ForeignKey, Text

from common import Model


class Report(Model):
    __tablename__ = 'bug_reports'

    id = Column(Integer, primary_key=True)
    reporter = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="SET NULL")
    )
    message = Column(Text)
