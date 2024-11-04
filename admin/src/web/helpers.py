from flask import current_app

def avatar_url(avatar):
    client=current_app.storage.client
    config = current_app.config

    if avatar is None:
        return default_avatar_url()

    return client.presigned_get_object("grupo00",avatar) #esta funcion sirve para usar una url pre-firmada para acceder a un archivo en minio

def default_avatar_url():
    protocol = "https" if current_app.config.get("MINIO_SECURE") else "http"
    return f"{protocol}://{current_app.config.get('MINIO_SERVER')}/grupo00/public/default.png" 