from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import CHAR, TEXT, DATETIME

from libs.database.types import Base


class Amount(Base):
    __tablename__ = 'amounts'
    name = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
