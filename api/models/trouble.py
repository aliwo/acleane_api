from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.mysql import TEXT

from libs.database.types import Base


class Trouble(Base):
    '''
    "사전정보 입력" 에서 "피부고민" 을 나타냅니다.
    '''
    __tablename__ = 'troubles'
    name = Column(TEXT)

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
        }
