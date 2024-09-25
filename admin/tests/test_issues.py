from src.core import board

def test_issues():

    issues = board.list_issues()
    assert "no funciona el login" == issues[0]["title"]

def test_issues_len():
    issues = board.list_issues()
    assert 3 == len(issues)