from sqlalchemy import text, Index
from sqlalchemy import func, UniqueConstraint, CheckConstraint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)