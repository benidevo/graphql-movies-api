from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime

from models.db import db


class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = db.Column(db.String(100))
    genre = db.Column(db.String(50))
    year = db.Column(db.Integer())
    rating = db.Column(db.Float())
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime)

    def __init__(self, title, genre, year, rating):
        self.title = title
        self.genre = genre
        self.year = year
        self.rating = rating

    def __repr__(self):
        return f'{self.title} - {self.year}'
    
    def json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'genre': self.genre,
            'year': self.year,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at) if self.updated_at else None
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()    
    