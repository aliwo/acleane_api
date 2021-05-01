from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import TEXT, DATE

from libs.database.types import Base


class Picture(Base):
    __tablename__ = 'pictures'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    url = Column(TEXT)

    def __init__(self, **kwargs):
        super(Picture, self).__init__(**kwargs)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'url': self.url,
        }
