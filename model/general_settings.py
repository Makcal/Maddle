from sqlalchemy import Column, ForeignKey, Boolean

from common import Model


class GeneralSettings(Model):
    __tablename__ = 'general_settings'

    user_id = Column(
        ForeignKey("users.vk_id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True
    )
    confirm_remittances = Column(Boolean, default=False)
    reset_filters = Column(Boolean, default=True)

    def __repr__(self):
        return 'GeneralSettings(' \
            'user_id={0.user_id}, ' \
            'confirm_remittances={0.confirm_remittances}, ' \
            'reset_filters={0.reset_filters}' \
        ')'.format(self)
