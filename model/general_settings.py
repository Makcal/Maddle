from sqlalchemy import Column, Integer, ForeignKey, Boolean


class GeneralSettings:
    __tablename__ = 'general_settings'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    confirm_remittances = Column(Boolean, default=False)
    reset_filters = Column(Boolean, default=True)
