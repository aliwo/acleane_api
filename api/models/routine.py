from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL

from libs.database.types import Base


class Routine(Base):
    __tablename__ = 'routines'
    from_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    to_user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    rate = Column(DECIMAL(10, 3))

    def json(self):
        return {
            'id': self.id,
            'rate': self.rate
        }
