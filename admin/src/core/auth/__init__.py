from src.core.bcrypt import bcrypt
from src.core.database import db
from src.core.auth.user import User

PERMISSIONS={
    "admin":[
        "user_index",
        "user_show",
        "user_new",
        "user_edit",
        "user_create",
        "user_update",    
        "user_delete",
        "issue_index",
        "issue_show",
        "issue_new",
        "issue_create",
        "issue_edit",
        "issue_update",
        "issue_delete",
    ],
    "standard":[
        "issue_index",
        "issue_show",
        "issue_new",
        "issue_create",
        "issue_edit",
        "issue_update",
        "issue_delete",
    ]
}

def get_permissions(user):
    return PERMISSIONS[user.role]

def list_users():
    issues = User.query.all()
    return issues

def create_user(**kwargs):
    hashed_Pass = bcrypt.generate_password_hash(kwargs["password"].encode("utf-8"))
    kwargs["password"] = hashed_Pass.decode("utf-8")
    issue = User(**kwargs)
    db.session.add(issue)
    db.session.commit()

    return issue

def find_user_by_email_and_password(email):

    user = User.query.filter_by(email=email).first()  # Corrige aquí para usar User

    return user

def check_user(email,password):

    user = find_user_by_email_and_password(email=email)

    if user and bcrypt.check_password_hash(user.password,password):
        return user

    return None