from sqlalchemy import Column, ForeignKey, Integer
from libs.database.types import Base


class RoutineAmountRelation(Base):
    __tablename__ = 'routine_amount_relations'
    routine_id = Column(Integer, ForeignKey('routines.id', ondelete='SET NULL'), index=True)
    amount_id = Column(Integer, ForeignKey('amounts.id', ondelete='SET NULL'), index=True)

    def json(self):
        return {
            'id': self.id,
        }
