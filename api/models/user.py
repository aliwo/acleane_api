from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, orm
from sqlalchemy.dialects.mysql import TEXT, CHAR

from libs.database.types import Base, AcleaneTypes
from libs.datetime_helper import DateTimeHelper


class User(Base):
    __tablename__ = 'users'
    email = Column(TEXT)
    name = Column(TEXT)
    gender = Column(CHAR(10))
    age = Column(Integer)
    troubles = Column(AcleaneTypes.TextTuple)

    def json(self, **kwargs):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'troubles': self.troubles,
        }