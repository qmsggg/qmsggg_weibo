# -*- coding: utf-8 -*-

from application.extensions import db
from datetime import datetime

__all__ = ['UserInfo']


class UserInfo(db.Model):
    """data model"""
    __tablename__ = 'userinfo'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), nullable=False)
    passwd = db.Column(db.String(255), nullable=False)
    register_time = db.Column(db.Date, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<UserInfo '%s'>" % self.user_name

    def store(self):
        """save to database"""

        db.session.add(self)
        db.session.commit()

    def delete(self):
        """delete data"""

        db.session.delete(self)
        db.session.commit()