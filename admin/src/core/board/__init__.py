from src.core.database import db
from src.core.board.issue import Issue

def list_issues():
    issues = Issue.query.all()

    return issues

def create_issue(**kwargs):
    issue = Issue(**kwargs)
    db.session.add(issue)
    db.session.commit()

    return issue