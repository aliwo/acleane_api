from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, TEXT, DATETIME

from libs.database.types import Base


class Skip(Base):
    __tablename__ = 'skips'
    name = Column(TEXT)
    date = Column(DATETIME)
    trouble_id = Column(Integer, ForeignKey('troubles.id', ondelete='SET NULL'), index=True)


    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
