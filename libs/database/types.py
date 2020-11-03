from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import types


class Base:
    '''
    https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/mixins.html

    TODO: default 에 lambda 를 넣었을 때 실제로 동작하는지 확인해 보기
    https://stackoverflow.com/questions/23332393/default-value-with-primary-key-sqlalchemy
    https://docs.sqlalchemy.org/en/14/core/defaults.html#context-sensitive-default-functions
    '''
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=lambda: datetime.now())

    def json(self, **kwargs):
        return {}

Base = declarative_base(cls=Base)


class AcleaneTypes:


    class TextTuple(types.TypeDecorator):
        '''
        db 에 들어갈 때에는 , 를 포함한 문자열로 들어가며
        db 에서 나올 때에는 튜플로 빠져나오는 자료형입니다.

        주의! 증강 타입은 mutability 를 인식하지 못합니다!
        http://docs.sqlalchemy.org/en/latest/core/custom_types.html
        따라서 리스트가 아닌 튜플을 사용했습니다.

        주의! 콤마가 들어있는 문자열을 튜플 안에 집어넣지 마시오
        '''
        impl = types.TEXT

        def process_bind_param(self, value, dialect):
            return ','.join(map(str, value)) if value else ''

        def process_result_value(self, value, dialect):
            return tuple(item for item in value.split(',')) if value else ()


    class IntTuple(types.TypeDecorator):
        '''
        db로부터 나올 때에는 Integer 로 이루어진 튜플!
        '''
        impl = types.TEXT

        def process_bind_param(self, value, dialect):
            return ','.join(map(str, value)) if value else ''

        def process_result_value(self, value, dialect):
            return tuple(int(item) for item in value.split(',')) if value else ()


    class TextDate(types.TypeDecorator):

        impl = types.DATE

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%Y-%m-%d').date()

        def process_result_value(self, value, dialect):
            return value


    class TextTime(types.TypeDecorator):

        impl = types.TIME

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%H:%M:%S').time()

        def process_result_value(self, value, dialect):
            return value


    class TextDateTime(types.TypeDecorator):

        impl = types.DATETIME

        def process_bind_param(self, value, dialect):
            return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')

        def process_result_value(self, value, dialect):
            return value

