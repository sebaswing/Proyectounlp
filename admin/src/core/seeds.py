from src.core import board

def run():

    print ("Creando datos...")

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

    print ("Datos Creados...")