from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import TEXT

from libs.database.types import Base


class UserRoutine(Base):
    __tablename__ = 'user_routines'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    routine_id = Column(Integer, ForeignKey('routines.id', ondelete='SET NULL'), index=True)
    amount = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'routine_id': self.routine_id,
            'amount': self.amount,
        }
