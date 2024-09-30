from src.core import board
from src.core import auth

def run():

    print ("Creando usuarios...")

    user1 = auth.create_user(
    password="password123",
    email="user1@example.com"
    )

    user2 = auth.create_user(
        password="securePass456",
        email="user2@example.com"
    )

    user3 = auth.create_user(
        password="pass789",
        email="user3@example.com"
    )

    user4 = auth.create_user(
        password="superSecret!321",
        email="user4@example.com"
    )

    print ("Creando issues...")

    issue1 = board.create_issue(
        email= "example1@example.com",
        title= "no muestra pagina",
        description= "The requested page could not be found on the server.",
        status = "Open"
        )
        
    issue2 = board.create_issue(
        email="example2@example.com",
        title="error en el server",
        description="The server encountered an internal error and was unable to complete your request.",
        status="Resolved"
    )

    issue3 = board.create_issue(
        email="example3@example.com",
        title="prohibido el paso",
        description="You do not have permission to access this resource.",
        status="Pending"
    )

    board.assign_user(issue1,user1)
    board.assign_user(issue2,user2)
    board.assign_user(issue3,user3)

    # Asignar las etiquetas (labels) sin inserted_at ni updated_at

    print ("Datos labels...")
    
    label_1 = board.create_label(
        title="Bug",
        description="Issues related to software bugs.",
        color="#FF0000"
    )

    label_2 = board.create_label(
        title="Feature",
        description="Requests for new features or enhancements.",
        color="#00FF00"
    )

    label_3 = board.create_label(
        title="Documentation",
        description="Improvements or updates to project documentation.",
        color="#0000FF"
    )

    label_4 = board.create_label(
        title="Priority",
        description="Indicates the issue has high priority.",
        color="#FFFF00"
    )

    board.assign_labels(issue1,[label_1,label_2])
    board.assign_labels(issue2,[label_3,label_4])
    board.assign_labels(issue3,[label_1,label_4])

    print ("Datos Creados...")