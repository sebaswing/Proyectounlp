
def list_issues():
    issues =[
        {
            "id": 1,
            "email": "example1@example.com",
            "title": "no funciona el login",
            "description": "The requested page could not be found on the server.",
            "status": "Open"
        },
        {
            "id": 2,
            "email": "example2@example.com",
            "title": "no se encuentra la persona",
            "description": "The server encountered an internal error and was unable to complete your request.",
            "status": "new"
        },
        {
            "id": 3,
            "email": "example3@example.com",
            "title": "la aplicacion no responde",
            "description": "You do not have permission to access this resource.",
            "status": "Pending"
        }
    ]
    return issues

