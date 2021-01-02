from datetime import datetime

from sqlalchemy import Integer, Column, ForeignKey, orm
from sqlalchemy.dialects.mysql import TEXT, DATETIME, CHAR, INTEGER, BOOLEAN, TIMESTAMP, DECIMAL, JSON
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref

from libs.database.types import Base
from libs.datetime_helper import DateTimeHelper


class User(Base):
    __tablename__ = 'users'
    email = Column(TEXT)
    name = Column(TEXT)
    gender = Column(CHAR(10))
    age = Column(Integer)
    registed = Column(BOOLEAN)

    def json(self, **kwargs):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'registered': self.registed,
        }