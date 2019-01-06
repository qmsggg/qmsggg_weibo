# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, Date
from application.extensions import Base, session
from datetime import datetime

__all__ = ['User']

class User(Base):
    """data model"""
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(255), nullable=False)
    passwd = Column(String(255), nullable=False)
    register_time = Column(Date, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<User '%s'>" % self.user_name

    def store(self):
        """save to database"""

        session.add(self)
        session.commit()
        session.close()

    def delete(self):
        """delete data"""

        session.delete(self)
        session.commit()
        session.close()