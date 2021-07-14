from sqlalchemy import Column, Integer, ForeignKey, Text


class Report:
    __tablename__ = 'bug_reports'

    id = Column(Integer, primary_key=True)
    reporter = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="SET NULL")
    )
    message = Column(Text)
