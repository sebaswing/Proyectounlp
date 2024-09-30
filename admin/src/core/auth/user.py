from datetime import datetime
from src.core.database import db

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    password= db.Column(db.String(255),nullable=False)
    email = db.Column(db.String(255),nullable=False)
    issues = db.relationship("Issue", back_populates="user")
    inserted_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate = datetime.now)

    def __repr__(self):
        return f"<user #{self.id} email= {self.email}"