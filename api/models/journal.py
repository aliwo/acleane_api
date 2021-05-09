from sqlalchemy import Column, ForeignKey, Integer, TEXT
from sqlalchemy.dialects.mysql import DATE
from sqlalchemy.orm import relationship

from libs.database.types import Base


class Journal(Base):
    __tablename__ = 'journals'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    routine_id = Column(Integer, ForeignKey('routines.id', ondelete='CASCADE'), nullable=False)
    routine = relationship('Routine', lazy='selectin')
    name = Column(TEXT)
    date = Column(DATE)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'routine_id': self.routine_id,
            'routine_name': self.routine.name,
            'date': self.date.strftime('%Y-%m-%d')
        }
