from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import TEXT
from sqlalchemy.orm import relationship

from libs.database.types import Base


class UserRoutine(Base):
    __tablename__ = 'user_routines'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    routine_id = Column(Integer, ForeignKey('routines.id', ondelete='SET NULL'), index=True)
    routine = relationship('Routine', lazy='selectin')
    amount = Column(TEXT)
    name = Column(TEXT) # 생성 당시의 routine 의 name 을 물려받아야 합니다.

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'routine_id': self.routine_id,
            'routine_name': self.routine.name,
            'amount': self.amount,
        }
