from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, BOOLEAN, TEXT, DECIMAL
from sqlalchemy.orm import relationship
from api.models.routine_amount_relation import RoutineAmountRelation
from libs.database.types import Base


class Routine(Base):
    __tablename__ = 'routines'
    name = Column(TEXT)
    amounts = relationship('Amount', secondary=RoutineAmountRelation.__table__)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
