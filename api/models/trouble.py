from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import TEXT

from libs.database.types import Base


class Trouble(Base):
    __tablename__ = 'troubles'
    name = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
