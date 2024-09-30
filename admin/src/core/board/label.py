from datetime import datetime
from src.core.database import db

class Label(db.Model):
    __tablename__="labels"

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=True)
    color = db.Column(db.String(20),nullable=False)
    inserted_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate = datetime.now)

    def __repr__(self):
        return f"<label  #{self.id} title= {self.title}"