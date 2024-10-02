from src.core.database import db
from src.core.auth.user import User

def list_users():
    issues = User.query.all()

    return issues

def create_user(**kwargs):
    issue = User(**kwargs)
    db.session.add(issue)
    db.session.commit()

    return issue

def find_user_by_email_and_password(email,password):
    user = User.query.filter_by(email=email,password=password).first()

    return user