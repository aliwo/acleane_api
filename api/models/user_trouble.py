from sqlalchemy import Column, ForeignKey, Integer
from libs.database.types import Base


class UserTrouble(Base):
    __tablename__ = 'user_troubles'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), index=True)
    trouble_id = Column(Integer, ForeignKey('troubles.id', ondelete='SET NULL'), index=True)

    def json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'trouble_id': self.trouble_id,
        }
