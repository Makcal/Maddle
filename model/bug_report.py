from sqlalchemy import Column, Integer, ForeignKey, Text

from common import Model


class Report(Model):
    __tablename__ = 'bug_reports'

    id = Column(Integer, primary_key=True)
    reporter = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="SET NULL")
    )
    message = Column(Text)

    def __repr__(self):
        return 'Report(' \
            'id={0.id}, ' \
            'reporter={0.reporter}, ' \
            'message={0.message}' \
        ')'.format(self)
