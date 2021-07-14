from sqlalchemy import Column, Integer, String, ForeignKey


class ReportAttachment:
    __tablename__ = 'bug_attachments'

    id = Column(Integer, primary_key=True)
    report_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
    )
    link = Column(String(500))
