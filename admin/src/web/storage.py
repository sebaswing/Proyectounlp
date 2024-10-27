from minio import Minio

class Storage:
    def __init__(self, app=None):
        self.client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        "inicializa el cliente de minIO y le adjunta al contexto de la aplicacion"
        minio_server = app.config.get('MINIO_SERVER')
        access_key = app.config.get('MINIO_ACCESS_KEY')
        secret_key = app.config.get('MINIO_SECRET_KEY')
        secure = app.config.get('MINIO_SECURE', False)

        # inicializa el cliente de minIO
        self._client = Minio(
            minio_server, 
            access_key=access_key, 
            secret_key=secret_key, 
            secure=secure
            )
        
        app.storage = self

        return app
    
    @property
    def client(self):
        "propiedad para obtener el cliente de minIO"
        return self._client
    
    @client.setter
    def client(self, value):
        "propiedad setter para reasignar el cliente de minIO"
        self._client = value

storage=Storage()