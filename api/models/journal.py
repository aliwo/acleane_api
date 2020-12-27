from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import DATE
from libs.database.types import Base


class Journal(Base):
    __tablename__ = 'journals'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    routine_id = Column(Integer, ForeignKey('routines.id', ondelete='CASCADE'), nullable=False)
    date = Column(DATE)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'routine_id': self.routine_id,
            'date': self.date.strftime('%Y-%m-%d')
        }
