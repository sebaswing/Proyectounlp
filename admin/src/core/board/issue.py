from datetime import datetime
from src.core.database import db

class Issue(db.Model):
    __tablename__="issues"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),nullable=False)
    title = db.Column(db.String(100),nullable=False)
    description = db.Column(db.Text,nullable=False)
    status = db.Column(db.String(20),nullable=False,default="new")
    user_id = db.Column (db.Integer, db.ForeignKey("users.id"))
    user = db.relationship ("User", back_populates="issues")
    inserted_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate = datetime.now)

    def __repr__(self):
        return f"<Issue #{self.id} title = '{self.title}' status='{self.status}'>"