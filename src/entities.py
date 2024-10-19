from .db import db
from datetime import datetime


class Email(db.Model):
    __tablename__ = 'emails_blacklist'

    email = db.Column(db.String(255), primary_key=True)
    app_id = db.Column(db.String(255), nullable=False)
    ip = db.Column(db.String(255), nullable=False)
    reason = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    

    def __repr__(self):
        return f'<Email {self.email}>'